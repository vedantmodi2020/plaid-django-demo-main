# Generated by Django 3.1.5 on 2022-05-15 10:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfinance', '0029_auto_20210220_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 15, 5, 13, 27, 500015)),
        ),
    ]
