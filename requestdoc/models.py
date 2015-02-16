from django.contrib.auth.models import User
from django.db import models

import os
from d_cash.settings import STATIC_ROOT


class RequestDoc(models.Model):
    request_user = models.ForeignKey(User)
    request_doc_number = models.CharField(max_length=10, null=True, blank=True)

    def __unicode__(self):
        return u'Request Document No. (%s)' % (self.request_doc_number if self.request_doc_number else 'Not Assign')


class Invoice(models.Model):
    request_doc = models.ForeignKey(RequestDoc)
    invoice_no = models.CharField(max_length=50, verbose_name="Invoice Number")
    invoice_date = models.DateField(verbose_name="Invoice Date")
    invoice_file = models.FileField(null=True, blank=True,
                                    upload_to=os.path.join(STATIC_ROOT) + '/invoice_files/%Y/%m/%d')
    location_x = models.CharField(max_length=10, verbose_name="x", null=True, blank=True)
    location_y = models.CharField(max_length=10, verbose_name="y", null=True, blank=True)
    factory = models.CharField(max_length=150,
                               verbose_name="Factory Name",
                               help_text='Outside Country',
                               null=True, blank=True)
    factory_location = models.TextField(max_length=300,
                                        verbose_name="Factory Location",
                                        null=True, blank=True,
                                        help_text='Outside Country')

    def __unicode__(self):
        return u'Invoice No. (%s), Invoice Date (%s)' % (self.invoice_no, self.invoice_date)


class Product(models.Model):
    invoice = models.ForeignKey(Invoice)
    license_no = models.CharField(max_length=20)
    standard_industrial_no = models.CharField(max_length=20)
    standard_name = models.CharField(max_length=100)
    product_name = models.TextField(max_length=300)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=30)
    hs_code = models.CharField(max_length=50)

    def __unicode__(self):
        return 'Invoice No. (%s), License No. (%s), Product Name (%s) %s %s (hsCode %s)' % \
               (self.invoice.invoice_no, self.license_no, self.product_name, self.quantity, self.unit, self.hs_code)
