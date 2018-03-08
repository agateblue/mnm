# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-03-08 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instances', '0005_auto_20170501_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='last_week_logins',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instance',
            name='last_week_registrations',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instance',
            name='last_week_statuses',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
