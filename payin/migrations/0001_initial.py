# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requestdoc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayIn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('paid', models.BooleanField(default=False)),
                ('approve', models.BooleanField(default=False)),
                ('approved_date', models.DateTimeField(null=True, blank=True)),
                ('barcode_location', models.TextField(max_length=200, null=True, blank=True)),
                ('created_date', models.DateTimeField()),
                ('request_document', models.OneToOneField(to='requestdoc.RequestDoc')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
