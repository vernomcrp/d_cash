from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required
def display_payin(request):
    '''
    Display payin which ready for print
    :param request:
    :return:
    '''
    context = {}
    if request.method == 'GET':


        return render(request, 'payin/payin_print_ready.html', context)
