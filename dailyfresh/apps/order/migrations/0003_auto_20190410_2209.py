# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-10 14:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20171113_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordergoods',
            name='comment',
            field=models.CharField(default=b'', max_length=256, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba'),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='count',
            field=models.IntegerField(default=1, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe6\x95\xb0\xe7\x9b\xae'),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0'),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.OrderInfo', verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95'),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe4\xbb\xb7\xe6\xa0\xbc'),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='sku',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsSKU', verbose_name=b'\xe5\x95\x86\xe5\x93\x81SKU'),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='addr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Address', verbose_name=b'\xe5\x9c\xb0\xe5\x9d\x80'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='order_id',
            field=models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95id'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='order_status',
            field=models.SmallIntegerField(choices=[(1, b'\xe5\xbe\x85\xe6\x94\xaf\xe4\xbb\x98'), (2, b'\xe5\xbe\x85\xe5\x8f\x91\xe8\xb4\xa7'), (3, b'\xe5\xbe\x85\xe6\x94\xb6\xe8\xb4\xa7'), (4, b'\xe5\xbe\x85\xe8\xaf\x84\xe4\xbb\xb7'), (5, b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90')], default=1, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe7\x8a\xb6\xe6\x80\x81'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_method',
            field=models.SmallIntegerField(choices=[(1, b'\xe8\xb4\xa7\xe5\x88\xb0\xe4\xbb\x98\xe6\xac\xbe'), (2, b'\xe5\xbe\xae\xe4\xbf\xa1\xe6\x94\xaf\xe4\xbb\x98'), (3, b'\xe6\x94\xaf\xe4\xbb\x98\xe5\xae\x9d'), (4, b'\xe9\x93\xb6\xe8\x81\x94\xe6\x94\xaf\xe4\xbb\x98')], default=3, verbose_name=b'\xe6\x94\xaf\xe4\xbb\x98\xe6\x96\xb9\xe5\xbc\x8f'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='total_count',
            field=models.IntegerField(default=1, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe6\x95\xb0\xe9\x87\x8f'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe6\x80\xbb\xe4\xbb\xb7'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='trade_no',
            field=models.CharField(default=b'', max_length=128, verbose_name=b'\xe6\x94\xaf\xe4\xbb\x98\xe7\xbc\x96\xe5\x8f\xb7'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='transit_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe8\xbf\x90\xe8\xb4\xb9'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7'),
        ),
    ]
