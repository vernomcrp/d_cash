from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import redirect
from payin.models import PayIn
from requestdoc.forms import InvoiceForm, ProductForm
from requestdoc.models import Invoice, RequestDoc, Product
from datetime import datetime
import random
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from user_detail.models import ConsumerDetail
import logging

logger = logging.getLogger(__name__)


def login_view(request):
    context = {}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                logger.info("logged user=%s, is_officier=%s" % (user, user.userdetail.is_officer()))
                return redirect('/requestdoc/request_menu/')

            else:
                return HttpResponse('disabled account')
        else:
            return HttpResponse('login error')
    else:

        return render(request, 'requestdoc/login.html', context)


def logout_view(request):
    logging_out_user = request.user.username
    logout(request)
    return render(request, 'requestdoc/logout_page.html', {'logging_out_user': logging_out_user})


@login_required(login_url='/requestdoc/login')
def request_document_view_without_license(request):
    return render(request, 'requestdoc/request_view_without_license.html', {})


@login_required(login_url='/requestdoc/login')
def precheck(request):
    if request.method == 'GET':
        if request.user.userdetail.is_officer():
            return render(request, 'requestdoc/find_consumer.html', {'logged_in_user': request.user})
    else:
        request_tax_no = request.POST.get('tax-no', None)

        try:
            consumer = ConsumerDetail.objects.get(tax_number=request_tax_no)
        except ConsumerDetail.DoesNotExist:
            return render(request, 'requestdoc/find_consumer.html', {
                'logged_in_user': request.user,
                'error': 'Consumer with TaxNo %s is invalid' % request_tax_no
            })

        request.session['request_user_id'] = consumer.owner.id

    return redirect('requestdoc.views.request_document_view')


def get_request_user(request):
    logged_in_user = request.user
    if logged_in_user.userdetail.is_officer():
        request_user_id = request.session.get('request_user_id')
        request_user = User.objects.get(id=request_user_id)
    else:
        request_user = logged_in_user
    return request_user, logged_in_user


@login_required(login_url='/requestdoc/login')
def request_document_view(request):
    request_user, logged_in_user = get_request_user(request)
    context = {
        'consumer': request_user.consumerdetail_set.all()[0] if len(request_user.consumerdetail_set.all()) else None,
        'logged_in_user': logged_in_user
    }
    if request.method == 'GET':
        context.update({'form': InvoiceForm()})

    elif request.method == 'POST':
        form = InvoiceForm(request.POST, request.FILES)
        if form.is_valid():
            invoice_no = form.cleaned_data['invoice_no']
            invoice_date = form.cleaned_data['invoice_date']
            invoice_file = form.cleaned_data['invoice_file']
            location_x = form.cleaned_data['location_x']
            location_y = form.cleaned_data['location_y']
            factory_outside = form.cleaned_data['factory_outside']
            factory_outside_location = form.cleaned_data['factory_outside_location']

            request_doc = RequestDoc()
            request_doc.request_user = request_user
            request_doc.request_doc_number = '{0:010}'.format(random.randint(1, 100000))
            request_doc.save()

            current_invoice = Invoice()
            current_invoice.request_doc = request_doc
            current_invoice.invoice_no = invoice_no
            current_invoice.invoice_date = invoice_date
            current_invoice.invoice_file = invoice_file
            current_invoice.location_x = location_x
            current_invoice.location_y = location_y
            current_invoice.factory = factory_outside
            current_invoice.factory_location = factory_outside_location

            current_invoice.save()

            request.session['request_doc_id'] = request_doc.id
            request.session['invoice_id'] = current_invoice.id
            # request.session['request_user_id'] = request_user.id

            return HttpResponseRedirect(reverse('requestdoc.views.request_identify_good'))
        else:
            context.update({'form': form})

    return render(request, 'requestdoc/request_view.html', context)


def get_current_time():
    return datetime.today()


@login_required(login_url='/requestdoc/login')
def complete_request_process(request):
    context = {}

    if request.method == 'POST':
        request_doc_no = request.POST.get('request_doc_no', None)
        request_doc_obj = RequestDoc.objects.get(request_doc_number=request_doc_no)

        payin = PayIn()
        payin.request_document = request_doc_obj
        payin.created_date = get_current_time()
        if request.user.userdetail.is_officer():
            payin.paid = True
        payin.save()

        return render(request, 'requestdoc/complete_request_process.html', context)
    else:
        return HttpResponseNotFound()


@login_required(login_url='/requestdoc/login')
def request_identify_good(request):
    request_doc_id = request.session.get('request_doc_id', None)
    invoice_id = request.session.get('invoice_id', None)
    context = {
        'logged_in_user': request.user,
    }
    if request_doc_id and invoice_id:
        if request.method == 'GET':

            invoice = Invoice.objects.get(id=invoice_id)
            context.update({
                'request_doc': RequestDoc.objects.get(id=request_doc_id),
                'form': ProductForm(),
                'products': invoice.product_set.all()
            })
        elif request.method == 'POST':

            form = ProductForm(request.POST)
            if form.is_valid():
                license_no = form.cleaned_data['license_no']
                standard_industrial_no = form.cleaned_data['standard_industrial_no']
                standard_name = form.cleaned_data['standard_name']
                product_name = form.cleaned_data['product_name']
                quantity = form.cleaned_data['quantity']
                unit = form.cleaned_data['unit']

                product = Product()
                product.invoice_id = invoice_id
                product.license_no = license_no
                product.standard_industrial_no = standard_industrial_no
                product.standard_name = standard_name
                product.product_name = product_name
                product.quantity = quantity
                product.unit = unit

                product.save()

                return HttpResponseRedirect('/requestdoc/request_identify_good/')
            else:
                invoice = Invoice.objects.get(id=invoice_id)
                context.update({
                    'request_doc': RequestDoc.objects.get(id=request_doc_id),
                    'form': form,
                    'products': invoice.product_set.all()
                })

                return render(request, 'requestdoc/request_product_view.html', context)
        else:
            return HttpResponseNotFound()
        return render(request, 'requestdoc/request_product_view.html', context)


@login_required(login_url='/requestdoc/login')
def list_request_document_status(request):
    if request.method == 'GET':
        if request.user.userdetail.is_officer():
            request_docs = RequestDoc.objects.all()
        else:
            request_docs = RequestDoc.objects.filter(request_user=request.user)
        filtered_docs = filter(__find_matched_payin, request_docs)
        return render(request, 'requestdoc/request_document_status.html',
                      {'items': filtered_docs, 'logged_in_user': request.user})


def __find_matched_payin(request_doc):
    # TODO this is suck, please refactor
    payins = PayIn.objects.filter(request_document=request_doc)
    return True if len(payins) else False


@login_required(login_url='/requestdoc/login')
def request_menu(request):
    if request.method == 'GET':
        return render(request, 'requestdoc/request_menu.html', {'logged_in_user': request.user})


@login_required(login_url='/requestdoc/login')
def approve_request_document(request):
    if request.method == 'GET':
        filtered_docs = filter(__find_matched_payin, RequestDoc.objects.all())
        return render(request, 'requestdoc/approve_request_document.html',
                      {'items': filtered_docs, 'logged_in_user': request.user})

    elif request.method == 'POST':
        payin_id = request.POST.get('approve_payin_id', None)
        if payin_id:
            payin = PayIn.objects.get(id=payin_id)
            payin.approve = True
            payin.approved_date = datetime.today()
            payin.save()
            return redirect('/requestdoc/approve_document/')
        else:
            print 'Cannot get payin id from frontend'
