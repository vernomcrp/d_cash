# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requestdoc', '0004_auto_20150117_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayIn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('approve', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField()),
                ('approved_date', models.DateTimeField()),
                ('request_document', models.OneToOneField(to='requestdoc.RequestDoc')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
