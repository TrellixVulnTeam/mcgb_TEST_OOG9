# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-02 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0018_auto_20180402_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Event_ID',
            field=models.IntegerField(unique=True),
        ),
    ]
