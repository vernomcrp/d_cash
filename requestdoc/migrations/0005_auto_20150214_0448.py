# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requestdoc', '0004_auto_20150117_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_file',
            field=models.FileField(null=True, upload_to=b'/home/siraset/MyProjects/d_cash/static/invoice_files/%Y/%m/%d', blank=True),
        ),
    ]
