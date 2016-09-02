# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-21 21:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscriptions', '0002_auto_20160721_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_id', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('NEW', 'New un-initialized payment transaction'), ('TOKEN_REQ', 'Token requested'), ('PMT_APPROV', 'Payment approved'), ('PMT_CANCELLED', 'Payment cancelled by user'), ('PMT_MAX_ATTEMPT', 'Payment max attempts'), ('PMT_EXPIRED', 'Payment token expired')], default='NEW', max_length=16)),
                ('reference_id', models.CharField(blank=True, max_length=50, unique=True)),
                ('reference_date', models.DateTimeField(auto_now_add=True)),
                ('transaction_id', models.CharField(default='', max_length=13)),
                ('transaction_date', models.DateTimeField(blank=True, null=True)),
                ('token', models.CharField(default='', max_length=48)),
                ('token_date', models.DateTimeField(blank=True, null=True)),
                ('amount', models.IntegerField(default=-1)),
                ('reconciliation', models.IntegerField(default=-1)),
                ('name', models.CharField(default='', max_length=60)),
                ('account_expiration_date', models.DateField(blank=True, null=True)),
                ('account_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='accounts.AccountType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['transaction_date'],
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionRate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subscription_id', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, default='')),
                ('description_html', models.TextField(blank=True, default='')),
                ('one_month', models.IntegerField(default=0)),
                ('three_month', models.IntegerField(default=0)),
                ('six_month', models.IntegerField(default=0)),
                ('twelve_month', models.IntegerField(default=0)),
                ('account_type', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='subscription_rate', to='accounts.AccountType')),
            ],
            options={
                'ordering': ['account_type'],
                'verbose_name': 'Subscription Rate',
                'verbose_name_plural': 'Subscription Rates',
            },
        ),
    ]