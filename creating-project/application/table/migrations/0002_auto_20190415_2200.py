# Generated by Django 2.1.7 on 2019-04-15 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablefield',
            name='width',
            field=models.IntegerField(default=1, verbose_name='Ширина'),
        ),
    ]
