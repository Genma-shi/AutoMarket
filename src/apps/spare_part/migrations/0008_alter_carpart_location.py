# Generated by Django 4.2.4 on 2023-09-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spare_part', '0007_alter_carpart_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpart',
            name='location',
            field=models.URLField(verbose_name='Адрес'),
        ),
    ]
