from django.contrib.auth.models import User
from django.db import models


class RequestDoc(models.Model):
    request_user = models.ForeignKey(User)
    request_doc_number = models.CharField(max_length=10, null=True, blank=True)

    def __unicode__(self):
        return u'req. document no. (%s)' % (self.request_doc_number if self.request_doc_number else 'not assign')


class Invoice(models.Model):
    request_doc = models.ForeignKey(RequestDoc)
    invoice_no = models.CharField(max_length=50, verbose_name="Invoice Number")
    invoice_date = models.DateField(verbose_name="Invoice Date")
    invoice_file = models.FileField(null=True, blank=True)
    location_x = models.CharField(max_length=10, verbose_name="x", null=True, blank=True)
    location_y = models.CharField(max_length=10, verbose_name="y", null=True, blank=True)
    factory = models.CharField(max_length=150, verbose_name="Factory Name", null=True, blank=True)
    factory_location = models.TextField(max_length=300, verbose_name="Factory Location", null=True, blank=True)

    def __unicode__(self):
        return u'inv no. (%s), date (%s)' % (self.invoice_no, self.invoice_date)


class Product(models.Model):
    invoice = models.ForeignKey(Invoice)
    license_no = models.CharField(max_length=20)
    standard_industrial_no = models.CharField(max_length=20)
    standard_name = models.CharField(max_length=100)
    product_name = models.TextField(max_length=300)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=30)

    def __unicode__(self):
        return 'inv no. (%s), license no. (%s), prod. name (%s) %s %s' % \
               (self.invoice.invoice_no, self.license_no, self.product_name, self.quantity, self.unit)
