from django.contrib.auth.models import User
from django.db import models

UNPAID = 'U'
PAID = 'P'

REQUEST_FORM_STATUS = (
    (UNPAID, 'unpaid'),
    (PAID, 'paid')
)

# Create your models here.


class Registration(models.Model):
    pass


class RequestForm(models.Model):
    request_user = models.ForeignKey(User, unique=True)
    request_description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=REQUEST_FORM_STATUS, max_length=1, default=UNPAID)
