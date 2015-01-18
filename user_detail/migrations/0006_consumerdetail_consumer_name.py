# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_detail', '0005_remove_consumerdetail_request_doc'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumerdetail',
            name='consumer_name',
            field=models.TextField(default='Consumer Name', max_length=100, verbose_name=b'Consumer Name'),
            preserve_default=False,
        ),
    ]
