# Generated by Django 2.1.7 on 2019-04-15 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0002_auto_20190415_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablefield',
            name='index_number',
            field=models.IntegerField(unique=True, verbose_name='Порядковый номер'),
        ),
    ]