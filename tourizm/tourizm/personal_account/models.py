from django.db import models
from django.contrib.auth.models import User


class Db_user(models.Model):
    first_name = models.CharField(max_length=50, null=True, verbose_name='Имя')
    second_name = models.CharField(max_length=50, null=True, verbose_name='Фамилия')
    email_user = models.CharField(max_length=50, null=True, verbose_name='Почта')
    phone_user = models.CharField(max_length=50, null=True, verbose_name='Телефон')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Личный кабинет каждого пользователя'
        verbose_name_plural = 'Личный кабинет каждого пользователя'