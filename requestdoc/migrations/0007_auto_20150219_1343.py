# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requestdoc', '0006_product_hs_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='factory',
            field=models.CharField(help_text=b'Outside Country', max_length=150, null=True, verbose_name=b'Factory Name', blank=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='factory_location',
            field=models.TextField(help_text=b'Outside Country', max_length=300, null=True, verbose_name=b'Factory Location', blank=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_file',
            field=models.FileField(null=True, upload_to=b'/home/vernom/d_cash/static/invoice_files/%Y/%m/%d', blank=True),
        ),
    ]
