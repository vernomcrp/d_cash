# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requestdoc', '0002_auto_20150114_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('invoice_no', models.CharField(max_length=50, verbose_name=b'Invoice Number')),
                ('invoice_date', models.DateField(verbose_name=b'Invoice Date')),
                ('invoice_file', models.FileField(upload_to=b'')),
                ('location_x', models.CharField(max_length=10, null=True, verbose_name=b'x', blank=True)),
                ('location_y', models.CharField(max_length=10, null=True, verbose_name=b'y', blank=True)),
                ('factory', models.CharField(max_length=150, null=True, verbose_name=b'Factory Name', blank=True)),
                ('factory_location', models.TextField(max_length=300, null=True, verbose_name=b'Factory Location', blank=True)),
                ('request_doc', models.ForeignKey(to='requestdoc.RequestDoc')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license_no', models.CharField(max_length=20)),
                ('standard_industrial_no', models.CharField(max_length=20)),
                ('standard_name', models.CharField(max_length=100)),
                ('product_name', models.TextField(max_length=300)),
                ('quantity', models.IntegerField()),
                ('unit', models.CharField(max_length=30)),
                ('invoice', models.ForeignKey(to='requestdoc.Invoice')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='requestdoc',
            name='request_doc_number',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
