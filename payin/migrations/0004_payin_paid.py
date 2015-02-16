# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payin', '0003_payin_barcode_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='payin',
            name='paid',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
