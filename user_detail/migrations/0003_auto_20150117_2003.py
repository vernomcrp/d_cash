# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_detail', '0002_consumerdetail_request_doc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='consumer',
        ),
        migrations.DeleteModel(
            name='Invoice',
        ),
    ]
