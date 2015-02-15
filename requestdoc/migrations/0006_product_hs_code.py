# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requestdoc', '0005_auto_20150214_0448'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hs_code',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
