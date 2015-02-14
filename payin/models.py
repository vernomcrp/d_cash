from django.db import models


class PayIn(models.Model):
    request_document = models.OneToOneField('requestdoc.RequestDoc')
    approve = models.BooleanField(default=False)
    created_date = models.DateTimeField()
    approved_date = models.DateTimeField(null=True, blank=True)
    barcode_location = models.TextField(null=True, blank=True, max_length=200)

    def __unicode__(self):
        return 'Request Document No. (%s), Request Date (%s), ' \
               'Is Approved (%s), Approved Date (%s), ' \
               'Barcode Location (%s)' % (
                   self.request_document.request_doc_number, self.created_date,
                   self.approve, self.approved_date,
                   self.barcode_location
               )