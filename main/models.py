from django.db import models

# Create your models here.

class Users(models.Model):
    ''''Данные о Пользователях'''
    email    = models.EmailField('email')
    phone    = models.IntegerField('phone')
    name     = models.CharField('Name', max_length=100)
    surname  = models.CharField('Surname', max_length=100)
    password = models.CharField('password', max_length=100)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name        = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class List(models.Model):
    ''''Данные о Задачах'''
    user_id     = models.ForeignKey(Users, on_delete=models.CASCADE)
    title       = models.CharField('Заголовок Задачи', max_length=100)
    description = models.TextField('Текст задачи')
    author      = models.CharField('Имя автора', max_length=100)
    date        = models.DateField('Дата задачи')

    def __str__(self):
        return f'{self.title}, {self.description}'

    class Meta:
        verbose_name        = 'Задача'
        verbose_name_plural = 'Задачи'


class Complete(models.Model):
    ''''Данные о Задачах'''
    user_id     = models.ForeignKey(Users, on_delete=models.CASCADE)
    title       = models.CharField('Заголовок Задачи', max_length=100)
    description = models.TextField('Текст задачи')
    author      = models.CharField('Имя автора', max_length=100)
    date        = models.DateField('Дата задачи')

    def __str__(self):
        return f'{self.title}, {self.description}'

    class Meta:
        verbose_name        = 'Выполненно'
        verbose_name_plural = 'Выполненные'

