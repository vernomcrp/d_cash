from django.contrib.auth.models import User
from django.db import models
from requestdoc.models import RequestDoc


class ConsumerDetail(models.Model):
    owner = models.ForeignKey(User)
    request_doc = models.ForeignKey(RequestDoc)
    address = models.TextField(max_length=300, verbose_name="Consumer Address")
    tax_number = models.CharField(max_length=50, verbose_name="Consumer Tax Number")



