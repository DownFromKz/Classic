from django.contrib.auth.models import User
from django.db import models

class Services(models.Model):
    name = models.CharField(max_length=150,verbose_name='Название')
    price = models.IntegerField(verbose_name='Стоимость')

    class Meta:
        verbose_name = 'услугу'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название продукта')
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    path_image = models.TextField(verbose_name='Путь к файлу с изображением')
    # models.Im

    class Meta:
        verbose_name = 'товары'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    path_image = models.TextField(verbose_name='Путь к файлу с изображением')
    speciality = models.CharField(max_length=150)
    services = models.ManyToManyField(Services)

    class Meta:
        verbose_name = 'сотрудников'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}, {self.user.username}'

class Record(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Специалист')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')
    date_record = models.DateTimeField(verbose_name='Дата и время записи')
    service = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='Услуга')

    class Meta:
        verbose_name = 'записи'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f'{self.service.name}, {self.employee.user.first_name}, {self.user.first_name}'

