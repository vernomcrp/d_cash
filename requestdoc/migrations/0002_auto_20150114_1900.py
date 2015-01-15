# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('requestdoc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestdoc',
            name='request_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
