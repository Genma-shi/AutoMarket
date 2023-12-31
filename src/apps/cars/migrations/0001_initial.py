# Generated by Django 4.2.4 on 2023-09-05 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500, null=True, verbose_name='Описание')),
                ('year', models.PositiveIntegerField(verbose_name='Год выпуска')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('body_type', models.CharField(choices=[('sedan', 'седан'), ('hatchback', 'хэтчбек'), ('SUV', 'внедорожник'), ('coupe', 'купе'), ('universal', 'универсал'), ('crossover', 'кроссовер'), ('minivan', 'минивен'), ('truck', 'грузовик')], max_length=13, verbose_name='Тип кузова')),
                ('engine', models.CharField(choices=[('petrol', 'бензин'), ('diesel', 'дизель'), ('hybrid', 'гибрид'), ('electric fuel', 'электро')], max_length=13, verbose_name='топливо')),
                ('views_count', models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')),
                ('mileage', models.PositiveIntegerField(default=0, help_text='Км', verbose_name='Пробег')),
                ('drive', models.CharField(choices=[('front wheel', 'передний'), ('rear', 'задний привод'), ('four wheel', 'полный привод')], max_length=20, verbose_name='привод')),
                ('gearbox', models.CharField(choices=[('machine', 'автомат'), ('tiptronic', 'типтроник'), ('mechanics', 'механика'), ('variable speed', 'вариатор'), ('robot', 'робот')], max_length=15, verbose_name='коробка передач')),
                ('engine_capacity', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Объем двигателя л')),
                ('ruletype', models.CharField(choices=[('right', 'правый'), ('left', 'левый')], default='left', max_length=5, verbose_name='Тип руля')),
                ('color', models.CharField(choices=[('white', 'белый'), ('red', 'красный'), ('blue', 'синий'), ('black', 'черный'), ('silver', 'серебристый'), ('gray', 'серый'), ('green', 'зеленый'), ('yellow', 'желтый'), ('orange', 'оранжевый'), ('brown', 'коричневый'), ('gold', 'золотистый'), ('pink', 'розовый'), ('beige', 'бежевый'), ('violet', 'фиолетовый'), ('burgundy', 'бордовый')], max_length=15, verbose_name='цвет автомобиля')),
                ('condition', models.CharField(choices=[('excellent', 'отличное'), ('good', 'хорошее'), ('average', 'среднее'), ('satisfactory', 'удовлетворительное'), ('needs repair', 'требует ремонт'), ('emergency', 'аварийное')], max_length=21, verbose_name='состояние')),
                ('customs_cleared', models.CharField(choices=[('cleared by customs', 'расстаможен'), ('not cleared', 'не расстаможен')], max_length=25, verbose_name='расстаможен')),
                ('vin_code', models.CharField(blank=True, choices=[('yes', 'есть VIN-код'), ('no', 'нет VIN-код')], default=False, max_length=5, verbose_name='наличие вин кода')),
                ('currency', models.CharField(choices=[('USD', 'В долларах'), ('KGZ', 'В сомах')], default='USD', max_length=11, verbose_name='валюта')),
            ],
        ),
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Марка')),
            ],
        ),
        migrations.CreateModel(
            name='Special_notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Особенные приметы')),
            ],
        ),
        migrations.CreateModel(
            name='CarPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cars/images/', verbose_name='Изображение')),
                ('is_main', models.BooleanField(default=False, verbose_name='Главное фото')),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='cars.car')),
            ],
            options={
                'verbose_name_plural': 'Car image',
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Модель')),
                ('cars', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='models', to='cars.carmake')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='mark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carmake', verbose_name='Марка'),
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carmodel', verbose_name='Модель'),
        ),
    ]
