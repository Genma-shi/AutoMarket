# Generated by Django 4.2.4 on 2023-09-09 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spare_part', '0003_alter_carpartimage_car_part_alter_carpartimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='carpart',
            name='vendor_code',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
