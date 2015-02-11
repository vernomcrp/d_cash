from django.db import models

# Create your models here.


class PayIn(models.Model):
    request_document = models.OneToOneField('requestdoc.RequestDoc')
    approve = models.BooleanField(default=False)
    created_date = models.DateTimeField()
    approved_date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return 'req. doc no (%s), approved (%s)' % (self.request_document.request_doc_number, self.approve)