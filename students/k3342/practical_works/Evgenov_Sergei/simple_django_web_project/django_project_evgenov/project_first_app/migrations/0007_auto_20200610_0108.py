# Generated by Django 3.0.5 on 2020-06-09 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0006_auto_20200610_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='home_address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nationality',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='passport_data',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
