# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_detail', '0004_userdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumerdetail',
            name='request_doc',
        ),
    ]
