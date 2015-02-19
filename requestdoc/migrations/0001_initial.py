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
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('invoice_no', models.CharField(max_length=50, verbose_name=b'Invoice Number')),
                ('invoice_date', models.DateField(verbose_name=b'Invoice Date')),
                ('invoice_file', models.FileField(null=True, upload_to=b'/home/siraset/MyProjects/d_cash/static/invoice_files/%Y/%m/%d', blank=True)),
                ('location_x', models.CharField(max_length=10, null=True, verbose_name=b'x', blank=True)),
                ('location_y', models.CharField(max_length=10, null=True, verbose_name=b'y', blank=True)),
                ('factory', models.CharField(help_text=b'Outside Country', max_length=150, null=True, verbose_name=b'Factory Name', blank=True)),
                ('factory_location', models.TextField(help_text=b'Outside Country', max_length=300, null=True, verbose_name=b'Factory Location', blank=True)),
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
                ('hs_code', models.CharField(max_length=50)),
                ('invoice', models.ForeignKey(to='requestdoc.Invoice')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RequestDoc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('request_doc_number', models.CharField(max_length=10, null=True, blank=True)),
                ('request_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='invoice',
            name='request_doc',
            field=models.ForeignKey(to='requestdoc.RequestDoc'),
            preserve_default=True,
        ),
    ]
