# Generated by Django 3.1.1 on 2020-12-19 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfinance', '0023_auto_20200912_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balances',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='location',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='payment_meta',
            field=models.JSONField(null=True),
        ),
    ]
