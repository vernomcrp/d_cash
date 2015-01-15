# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requestdoc', '0002_auto_20150114_1900'),
        ('user_detail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumerdetail',
            name='request_doc',
            field=models.ForeignKey(default=None, to='requestdoc.RequestDoc'),
            preserve_default=False,
        ),
    ]
