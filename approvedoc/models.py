from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#from registration.models import RequestForm

'''
class ApproveRecord(models.Model):
    invoice_data = models.TextField()
    allow_in_id = models.TextField(max_length=20)
    is_check_db = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    approver = models.ForeignKey(User, unique=True)
    is_approved = models.BooleanField(default=False)
    approved_date = models.DateTimeField(auto_now_add=True)
    register_data = models.OneToOneField(RequestForm)
    '''
