from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from user_detail.models import ConsumerDetail


@login_required
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

        user = User.objects.create_user(username, password, email)
        user.save()

        consumer_detail = ConsumerDetail()
        consumer_detail.owner_id = user.id
        consumer_detail.consumer_name = consumer_name
        consumer_detail.address = address
        consumer_detail.tax_number = tax_number

        consumer_detail.save()
        request.session['request_user_id'] = user.id
        return HttpResponseRedirect(reverse('requestdoc.views.request_document_view'))

