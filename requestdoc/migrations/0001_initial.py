# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_detail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestDoc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('request_doc_number', models.CharField(max_length=10)),
                ('request_user', models.ForeignKey(to='user_detail.ConsumerDetail')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
