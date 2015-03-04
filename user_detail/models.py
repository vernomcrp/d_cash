from django.contrib.auth.models import User
from django.db import models
from requestdoc.models import RequestDoc


class ConsumerDetail(models.Model):
    owner = models.ForeignKey(User)
    consumer_name = models.TextField(max_length=100, verbose_name='Consumer Name')
    address = models.TextField(max_length=300, verbose_name="Consumer Address")
    tax_number = models.CharField(max_length=50, verbose_name="Consumer Tax Number")

    def __unicode__(self):
        return u'%s, Tax No. (%s)' % (self.consumer_name, self.tax_number)


ROLES = (
    ('O', 'Officer'),
    ('C', 'Consumer'),
    ('V', 'High Officer')
)


class UserDetail(models.Model):
    owner = models.OneToOneField(User)
    role = models.CharField(max_length=1, choices=ROLES, default='C')

    def __unicode__(self):
        return u'%s is Officer (%s)' % (self.owner.username, self.is_officer())

    def is_officer(self):
        return True if self.role == 'O' or self.role == 'V' else False

    def is_high_officer(self):
        return True if self.role == 'V' else False