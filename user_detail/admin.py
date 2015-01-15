from django.contrib import admin

# Register your models here.
from user_detail.models import Invoice, ConsumerDetail

admin.site.register(Invoice)
admin.site.register(ConsumerDetail)