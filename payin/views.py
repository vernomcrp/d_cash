from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from barcode import generate

import os
from requestdoc.models import RequestDoc
from d_cash.settings import STATIC_ROOT


@login_required(login_url='/requestdoc/login')
def display_payin(request, request_doc_id):
    if request.method == 'GET':
        if request.user.userdetail.is_officer():
            request_user_id = request.session.get('request_user_id', None)
            if not request_user_id:
                return render(
                    request,
                    'error.html',
                    {
                        'error': {
                            'topic': 'Cannot Check PayIn Document',
                            'detail':'You must be a Owner of PayIn Document'
                        }
                    }
                )
            request_user = User.objects.get(id=request_user_id)
        else:
            request_user = request.user

        consumer_detail = request_user.consumerdetail_set.all()[0]

        detail = {
            'company_name': consumer_detail.consumer_name,
            'address': consumer_detail.address,
            'tax_number': consumer_detail.tax_number
        }

        rdoc = RequestDoc.objects.get(request_user=request_user, request_doc_number=request_doc_id)
        filename = generate_barcode(rdoc.request_doc_number, filename=os.path.join(STATIC_ROOT, 'example_svg'))
        return render(request, 'payin/payin_print_ready.html',
                      {'filename': filename, 'detail': detail, 'logged_in_user': request.user})


def generate_barcode(data, filename='example.svg'):
    return generate('EAN13', data, output=filename)
