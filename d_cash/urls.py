from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^requestdoc/login/$', 'requestdoc.views.login_view'),
    url(r'^requestdoc/request/$', 'requestdoc.views.request_document_view'),
    url(r'^requestdoc/request_without_license/$', 'requestdoc.views.request_document_view_without_license'),
    url(r'^requestdoc/request_identify_good/$', 'requestdoc.views.request_identify_good'),
    url(r'^requestdoc/complete_request_process/$', 'requestdoc.views.complete_request_process'),
    url(r'^requestdoc/request_menu/$', 'requestdoc.views.request_menu'),
    url(r'^requestdoc/request_document_status/$', 'requestdoc.views.list_request_document_status'),
    url(r'^requestdoc/approve_document/$', 'requestdoc.views.approve_request_document'),
    url(r'^payin/print/(?P<request_doc_id>\d+)/$', 'payin.views.display_payin')

)
