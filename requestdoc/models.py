from django.contrib.auth.models import User
from django.db import models

class RequestDoc(models.Model):
    request_user = models.ForeignKey(User)
    request_doc_number = models.CharField(max_length=10)
