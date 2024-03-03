from django.db import models

class Product(models.Model):
    image = models.ImageField(upload_to='images/', verbose_name='Изображение товара/услуги')
    description = models.TextField(verbose_name='Описание товара/услуги')
