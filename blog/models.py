from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField('Название', max_length=100, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Author(models.Model):
    name = models.CharField('Имя', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Blog(models.Model):
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    authors = models.ManyToManyField(Author)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
