# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-11 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20170811_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='full_name',
            field=models.CharField(default='', editable=False, max_length=300),
            preserve_default=False,
        ),
    ]