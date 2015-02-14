# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payin', '0002_auto_20150211_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='payin',
            name='barcode_location',
            field=models.TextField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
