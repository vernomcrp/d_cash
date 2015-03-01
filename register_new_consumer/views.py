from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.urlresolvers import reverse
from django.http import Http404
from user_detail.models import ConsumerDetail, UserDetail


def registration_page(request):
    if request.method == 'GET':
        # Create user form
        return render(
            request, 'registration/registration_page.html',
            {'logged_in_user': request.user}
        )
    elif request.method == 'POST':
        data = request.POST
        username = data.get('username', None)
        password = data.get('password', None)
        email = data.get('email', None)
        consumer_name = data.get('consumer_name', None)
        address = data.get('address', None)
        tax_number = data.get('tax_number', None)

        error = {
            'username': None,
            'email': None,
            'tax_no': None
        }

        if len(User.objects.filter(username=username)) > 0:
            error['username'] = 'Username %s is valid' % username

        if len(User.objects.filter(email=email)) > 0:
            error['email'] = 'Email %s is valid' % email

        if len(ConsumerDetail.objects.filter(tax_number=tax_number)) > 0:
            error['tax_no'] = 'Tax No %s is valid' % tax_number

        if None not in error.values():
            return render(
                request, 'registration/registration_page.html',
                {'logged_in_user': request.user, 'error': error}
            )

        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError as e:
            raise Http404(e)

        user.save()
        consumer_detail = ConsumerDetail()
        consumer_detail.owner_id = user.id
        consumer_detail.consumer_name = consumer_name
        consumer_detail.address = address
        consumer_detail.tax_number = tax_number

        consumer_detail.save()

        user_detail = UserDetail()
        user_detail.owner_id = user.id
        user_detail.role = 'C'

        user_detail.save()

        if not request.user.is_anonymous():
            request.session['request_user_id'] = user.id
            return HttpResponseRedirect(reverse('requestdoc.views.request_document_view'))
        else:
            return HttpResponseRedirect(reverse('requestdoc.views.login_view'))

