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
                ('consumer_name', models.TextField(max_length=100, verbose_name=b'Consumer Name')),
                ('address', models.TextField(max_length=300, verbose_name=b'Consumer Address')),
                ('tax_number', models.CharField(max_length=50, verbose_name=b'Consumer Tax Number')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(default=b'C', max_length=1, choices=[(b'O', b'Officer'), (b'C', b'Consumer')])),
                ('owner', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
