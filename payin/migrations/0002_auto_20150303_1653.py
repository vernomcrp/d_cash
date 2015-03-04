# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payin',
            name='final_approve',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='payin',
            name='final_approved_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
