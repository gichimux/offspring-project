# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-08-06 08:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_supplier_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requested_supply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=20)),
                ('time', models.DateTimeField(null=True)),
                ('status', models.BooleanField(default=False)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Supplier')),
            ],
        ),
    ]
