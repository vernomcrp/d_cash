from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from requestdoc.forms import InvoiceForm, ProductForm
from requestdoc.models import Invoice, RequestDoc, Product


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/requestdoc/request/')

            else:
                return HttpResponse('disabled account')
        else:
            return HttpResponse('login error')
    else:

        return render(request, 'requestdoc/login.html', {})


def logout_view(request):
    logout(request)


@login_required
def request_document_view(request):
    context = {}
    user = request.user
    if request.method == 'GET':
        context.update({
            'consumer': user.consumerdetail_set.all()[0],
            'form': InvoiceForm()
        })

    elif request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice_no = form.cleaned_data['invoice_no']
            invoice_date = form.cleaned_data['invoice_date']
            invoice_file = form.cleaned_data['invoice_file']
            location_x = form.cleaned_data['location_x']
            location_y = form.cleaned_data['location_y']
            factory_outside = form.cleaned_data['factory_outside']
            factory_outside_location = form.cleaned_data['factory_outside_location']

            request_doc = RequestDoc()
            request_doc.request_user = user
            request_doc.request_doc_number = "989898989"
            request_doc.save()

            current_invoice = Invoice()
            current_invoice.request_doc = request_doc
            current_invoice.invoice_no = invoice_no
            current_invoice.invoice_date = invoice_date
            current_invoice.invoice_file = None
            current_invoice.location_x = location_x
            current_invoice.location_y = location_y
            current_invoice.factory = factory_outside
            current_invoice.factory_location = factory_outside_location

            current_invoice.save()

            request.session['request_doc_id'] = request_doc.id
            request.session['invoice_id'] = current_invoice.id

            return HttpResponseRedirect('/requestdoc/request_identify_good/')

    return render(request, 'requestdoc/request_view.html', context)


def request_identify_good(request):
    context = {}
    request_doc_id = request.session.get('request_doc_id', None)
    invoice_id = request.session.get('invoice_id', None)
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

        return render(request, 'requestdoc/request_product_view.html', context)