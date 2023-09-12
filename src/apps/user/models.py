from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.models import AbstractUser
from src.apps.cars.choices import Currency , Number 
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField("Email", unique=True)
    avatar = models.ImageField(
        "Аватарка",
          upload_to="user/images/", 
          null=True,blank=True
          )
    mobile = models.CharField("Номер телефона", max_length=15, null=True,blank=True)
    favorites_list = models.ManyToManyField("cars.Car",max_length=255)
    currency = models.CharField("валюта" , max_length=11 , choices=Currency.choices , default= Currency.USD)
    # hide_number = models.CharField("Номер телефона" , max_length=11 , choices=Number.choices ,null=True)


    objects = UserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
