# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_detail', '0001_initial'),
    ]

    operations = [
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
                ('invoice', models.ForeignKey(to='user_detail.Invoice')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
