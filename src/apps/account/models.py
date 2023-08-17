from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    email = models.EmailField("Email", unique=True)
    avatar = models.ImageField(null=True,blank=True)
        # "Аватарка",
        #   upload_to="user/images/", 
        #   null=True,blank=True
        #   )
    mobile = models.CharField("Номер телефона", max_length=15, null=True,blank=True)
    favorites_list = models.ManyToManyField("cars.Car",max_length=255)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
