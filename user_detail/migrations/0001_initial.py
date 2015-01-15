# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumerDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.TextField(max_length=300, verbose_name=b'Consumer Address')),
                ('tax_number', models.CharField(max_length=50, verbose_name=b'Consumer Tax Number')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('invoice_no', models.CharField(max_length=50, verbose_name=b'Invoice Number')),
                ('invoice_date', models.DateField(verbose_name=b'Invoice Date')),
                ('invoice_file', models.FileField(upload_to=b'')),
                ('location_x', models.CharField(max_length=10, verbose_name=b'x')),
                ('location_y', models.CharField(max_length=10, verbose_name=b'y')),
                ('factory', models.CharField(max_length=150, verbose_name=b'Factory Name')),
                ('factory_location', models.TextField(max_length=300, verbose_name=b'Factory Location')),
                ('consumer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
