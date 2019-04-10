# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-10 14:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='detail',
            field=tinymce.models.HTMLField(blank=True, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe8\xaf\xa6\xe6\x83\x85'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(max_length=20, verbose_name=b'\xe5\x95\x86\xe5\x93\x81SPU\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='image',
            field=models.ImageField(upload_to=b'goods', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe8\xb7\xaf\xe5\xbe\x84'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='sku',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsSKU', verbose_name=b'\xe5\x95\x86\xe5\x93\x81'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='goodssku',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='goodssku',
            name='desc',
            field=models.CharField(max_length=256, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe7\xae\x80\xe4\xbb\x8b'),
        ),
        migrations.AlterField(
            model_name='goodssku',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name=b'\xe5\x95\x86\xe5\x93\x81SPU'),
        ),
        migrations.AlterField(
            model_name='goodssku',
            name='image',
            field=models.ImageField(upload_to=b'goods', verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='goodssku',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0'),
        ),
        migrations.AlterField(
            model_name='goodssku',
            name='name',
            field=models.CharField(max_length=20, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='goodssku',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe4\xbb\xb7\xe6\xa0\xbc'),
        ),
        migrations.AlterField(
            model_name='goodssku',
            name='sales',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe9\x94\x80\xe9\x87\x8f'),
        ),
        migrations.AlterField(
            model_name='goodssku',
            name='status',
            field=models.SmallIntegerField(choices=[(0, b'\xe4\xb8\x8b\xe7\xba\xbf'), (1, b'\xe4\xb8\x8a\xe7\xba\xbf')], default=1, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe7\x8a\xb6\xe6\x80\x81'),
        ),
        migrations.AlterField(
            model_name='goodssku',
            name='stock',
            field=models.IntegerField(default=1, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\xba\x93\xe5\xad\x98'),
        ),
        migrations.AlterField(
            model_name='goodssku',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsType', verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe7\xa7\x8d\xe7\xb1\xbb'),
        ),
        migrations.AlterField(
            model_name='goodssku',
            name='unite',
            field=models.CharField(max_length=20, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x8d\x95\xe4\xbd\x8d'),
        ),
        migrations.AlterField(
            model_name='goodssku',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='goodstype',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='goodstype',
            name='image',
            field=models.ImageField(upload_to=b'type', verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe7\xb1\xbb\xe5\x9e\x8b\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='goodstype',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0'),
        ),
        migrations.AlterField(
            model_name='goodstype',
            name='logo',
            field=models.CharField(max_length=20, verbose_name=b'\xe6\xa0\x87\xe8\xaf\x86'),
        ),
        migrations.AlterField(
            model_name='goodstype',
            name='name',
            field=models.CharField(max_length=20, verbose_name=b'\xe7\xa7\x8d\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='goodstype',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='indexgoodsbanner',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='indexgoodsbanner',
            name='image',
            field=models.ImageField(upload_to=b'banner', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='indexgoodsbanner',
            name='index',
            field=models.SmallIntegerField(default=0, verbose_name=b'\xe5\xb1\x95\xe7\xa4\xba\xe9\xa1\xba\xe5\xba\x8f'),
        ),
        migrations.AlterField(
            model_name='indexgoodsbanner',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0'),
        ),
        migrations.AlterField(
            model_name='indexgoodsbanner',
            name='sku',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsSKU', verbose_name=b'\xe5\x95\x86\xe5\x93\x81'),
        ),
        migrations.AlterField(
            model_name='indexgoodsbanner',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='indexpromotionbanner',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='indexpromotionbanner',
            name='image',
            field=models.ImageField(upload_to=b'banner', verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='indexpromotionbanner',
            name='index',
            field=models.SmallIntegerField(default=0, verbose_name=b'\xe5\xb1\x95\xe7\xa4\xba\xe9\xa1\xba\xe5\xba\x8f'),
        ),
        migrations.AlterField(
            model_name='indexpromotionbanner',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0'),
        ),
        migrations.AlterField(
            model_name='indexpromotionbanner',
            name='name',
            field=models.CharField(max_length=20, verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='indexpromotionbanner',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='indexpromotionbanner',
            name='url',
            field=models.CharField(max_length=256, verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe9\x93\xbe\xe6\x8e\xa5'),
        ),
        migrations.AlterField(
            model_name='indextypegoodsbanner',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='indextypegoodsbanner',
            name='display_type',
            field=models.SmallIntegerField(choices=[(0, b'\xe6\xa0\x87\xe9\xa2\x98'), (1, b'\xe5\x9b\xbe\xe7\x89\x87')], default=1, verbose_name=b'\xe5\xb1\x95\xe7\xa4\xba\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
        migrations.AlterField(
            model_name='indextypegoodsbanner',
            name='index',
            field=models.SmallIntegerField(default=0, verbose_name=b'\xe5\xb1\x95\xe7\xa4\xba\xe9\xa1\xba\xe5\xba\x8f'),
        ),
        migrations.AlterField(
            model_name='indextypegoodsbanner',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0'),
        ),
        migrations.AlterField(
            model_name='indextypegoodsbanner',
            name='sku',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsSKU', verbose_name=b'\xe5\x95\x86\xe5\x93\x81SKU'),
        ),
        migrations.AlterField(
            model_name='indextypegoodsbanner',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsType', verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
        migrations.AlterField(
            model_name='indextypegoodsbanner',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
