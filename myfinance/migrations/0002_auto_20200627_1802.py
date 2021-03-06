# Generated by Django 3.0.7 on 2020-06-27 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfinance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='orig_desc',
            new_name='orig_descr',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='updated_desc',
            new_name='updated_descr',
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfinance.Budget')),
            ],
        ),
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfinance.Category'),
        ),
    ]
