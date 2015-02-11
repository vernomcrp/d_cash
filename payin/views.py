from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from barcode import generate

# Create your views here.
from requestdoc.models import RequestDoc


@login_required
def display_payin(request, request_doc_id):
    if request.method == 'GET':
        user = request.user

        consumer_detail = user.consumerdetail_set.all()[0]

        detail = {
            'company_name': consumer_detail.consumer_name,
            'address': consumer_detail.address,
            'tax_number': consumer_detail.tax_number
        }

        rdoc = RequestDoc.objects.get(request_user=user, request_doc_number=request_doc_id)
        filename = generate_barcode(rdoc.request_doc_number, filename='example.svg')
        return render(request, 'payin/payin_print_ready.html', {'filename': 'example.svg', 'detail': detail})


def generate_barcode(data, filename='example.svg'):
    return generate('EAN13', data, output=filename)
