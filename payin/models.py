from django.db import models


class PayIn(models.Model):
    request_document = models.OneToOneField('requestdoc.RequestDoc')
    paid = models.BooleanField(default=False)
    approve = models.BooleanField(default=False)
    approved_date = models.DateTimeField(null=True, blank=True)
    final_approve = models.BooleanField(default=False)
    final_approved_date = models.DateTimeField(null=True, blank=True)
    barcode_location = models.TextField(null=True, blank=True, max_length=200)
    created_date = models.DateTimeField()

    def __unicode__(self):
        return 'Request Document No. (%s), Request Date (%s), ' \
               'Is Approved (%s), Approved Date (%s), ' \
               'Is Final Approved (%s), Final Approved Date (%s), ' \
               'Is Paid (%s), '\
               'Barcode Location (%s)' % (
                   self.request_document.request_doc_number, self.created_date,
                   self.approve, self.approved_date,
                   self.final_approve, self.final_approved_date,
                   self.paid,
                   self.barcode_location
               )