# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-18 14:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(default='karen', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='House_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('serial', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=200)),
                ('product_color', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(default=0)),
                ('size', models.CharField(max_length=3)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Distributor'),
        ),
        migrations.AddField(
            model_name='house_product',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product'),
        ),
        migrations.AddField(
            model_name='house_product',
            name='warehouse',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Distributor'),
        ),
        migrations.AddField(
            model_name='category',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Sub_Category'),
        ),
    ]
