from django.contrib import admin

# Register your models here.
from user_detail.models import ConsumerDetail, UserDetail

admin.site.register(ConsumerDetail)
admin.site.register(UserDetail)