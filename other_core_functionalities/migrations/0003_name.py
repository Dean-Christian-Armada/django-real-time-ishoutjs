# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other_core_functionalities', '0002_bookmark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=None, max_length=100)),
                ('middle_name', models.CharField(default=None, max_length=100)),
                ('last_name', models.CharField(default=None, max_length=100)),
            ],
        ),
    ]
