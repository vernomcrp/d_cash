from django.db import models

# Create your models here.
from user_detail.models import Invoice


class Product(models.Model):
    invoice = models.ForeignKey(Invoice)
    license_no = models.CharField(max_length=20)
    standard_industrial_no = models.CharField(max_length=20)
    standard_name = models.CharField(max_length=100)
    product_name = models.TextField(max_length=300)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=30)
