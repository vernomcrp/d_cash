from django.contrib.auth.models import User
from django.db import models
from requestdoc.models import RequestDoc


class ConsumerDetail(models.Model):
    owner = models.ForeignKey(User)
    request_doc = models.ForeignKey(RequestDoc)
    address = models.TextField(max_length=300, verbose_name="Consumer Address")
    tax_number = models.CharField(max_length=50, verbose_name="Consumer Tax Number")

    def __unicode__(self):
        return u'req. document no. (%s)' % self.request_doc.


ROLES = (
    ('O', 'Officer'),
    ('C', 'Consumer')
)


class UserDetail(models.Model):
    owner = models.OneToOneField(User)
    role = models.CharField(max_length=1, choices=ROLES)