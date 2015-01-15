from django.contrib.auth.models import User
from django.db import models
from requestdoc.models import RequestDoc


class ConsumerDetail(models.Model):
    owner = models.ForeignKey(User)
    request_doc = models.ForeignKey(RequestDoc)
    address = models.TextField(max_length=300, verbose_name="Consumer Address")
    tax_number = models.CharField(max_length=50, verbose_name="Consumer Tax Number")


class Invoice(models.Model):
    consumer = models.ForeignKey(User)
    invoice_no = models.CharField(max_length=50, verbose_name="Invoice Number")
    invoice_date = models.DateField(verbose_name="Invoice Date")
    invoice_file = models.FileField()
    location_x = models.CharField(max_length=10, verbose_name="x")
    location_y = models.CharField(max_length=10, verbose_name="y")
    factory = models.CharField(max_length=150, verbose_name="Factory Name")
    factory_location = models.TextField(max_length=300, verbose_name="Factory Location")
