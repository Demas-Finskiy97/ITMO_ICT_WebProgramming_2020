# Generated by Django 3.0.4 on 2020-04-20 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0005_auto_20200420_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datein',
            field=models.DateField(default='2013.12.11'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='dateout',
            field=models.DateField(default='2013.12.12'),
        ),
    ]
