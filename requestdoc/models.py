from django.contrib.auth.models import User
from django.db import models


class RequestDoc(models.Model):
    request_user = models.ForeignKey(User)
    request_doc_number = models.CharField(max_length=10)


class Invoice(models.Model):
    request_doc = models.ForeignKey(RequestDoc)
    invoice_no = models.CharField(max_length=50, verbose_name="Invoice Number")
    invoice_date = models.DateField(verbose_name="Invoice Date")
    invoice_file = models.FileField()
    location_x = models.CharField(max_length=10, verbose_name="x")
    location_y = models.CharField(max_length=10, verbose_name="y")
    factory = models.CharField(max_length=150, verbose_name="Factory Name")
    factory_location = models.TextField(max_length=300, verbose_name="Factory Location")


class Product(models.Model):
    invoice = models.ForeignKey(Invoice)
    license_no = models.CharField(max_length=20)
    standard_industrial_no = models.CharField(max_length=20)
    standard_name = models.CharField(max_length=100)
    product_name = models.TextField(max_length=300)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=30)
