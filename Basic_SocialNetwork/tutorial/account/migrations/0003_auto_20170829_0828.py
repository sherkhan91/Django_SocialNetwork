# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 08:28
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_userprofile_image'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('London', django.db.models.manager.Manager()),
            ],
        ),
    ]
