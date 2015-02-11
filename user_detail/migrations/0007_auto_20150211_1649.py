# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_detail', '0006_consumerdetail_consumer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='role',
            field=models.CharField(default=b'C', max_length=1, choices=[(b'O', b'Officer'), (b'C', b'Consumer')]),
        ),
    ]
