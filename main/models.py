from django.db import models

# Create your models here.


class List(models.Model):
    ''''Данные о Задачах'''
    title = models.CharField('Заголовок Задачи', max_length=100)
    description = models.TextField('Текст задачи')
    author = models.CharField('Имя автора', max_length=100)
    date = models.DateField('Дата задачи')

    def __str__(self):
        return f'{self.title}, {self.description}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Complete(models.Model):
    ''''Данные о Задачах'''
    title = models.CharField('Заголовок Задачи', max_length=100)
    description = models.TextField('Текст задачи')
    author = models.CharField('Имя автора', max_length=100)
    date = models.DateField('Дата задачи')

    def __str__(self):
        return f'{self.title}, {self.description}'

    class Meta:
        verbose_name = 'Выполненно'
        verbose_name_plural = 'Выполненные'