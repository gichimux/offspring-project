# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-22 04:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190722_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_product',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Supplier'),
        ),
    ]
