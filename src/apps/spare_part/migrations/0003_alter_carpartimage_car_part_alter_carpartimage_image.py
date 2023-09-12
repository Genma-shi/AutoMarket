# Generated by Django 4.2.4 on 2023-09-09 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spare_part', '0002_remove_carpart_manufacturer_carpart_views_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpartimage',
            name='car_part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='part_photos', to='spare_part.carpart'),
        ),
        migrations.AlterField(
            model_name='carpartimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='car_part/images/', verbose_name='Изображение'),
        ),
    ]