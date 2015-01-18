from django.contrib import admin

from requestdoc.models import RequestDoc, Invoice, Product


class RequestDocAdmin(admin.ModelAdmin):
    #Todo plan something here
    pass

admin.site.register(RequestDoc, RequestDocAdmin)
admin.site.register(Invoice)
admin.site.register(Product)