from django.db import models


# Create your models here.

class GameCategory(models.Model):
    slug = models.SlugField(unique=True, verbose_name='Category slug')
    name = models.CharField(max_length=50, verbose_name='Category name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Game category'
        verbose_name_plural = 'Game categories'


class Game(models.Model):
    category = models.ForeignKey(GameCategory, on_delete=models.PROTECT, verbose_name='Category name')
    slug = models.SlugField(unique=True, verbose_name='Game slug')
    name = models.CharField(max_length=50, verbose_name='Game name')
    description = models.TextField(verbose_name='Game description')
    image = models.ImageField(default='None/no-image.png', upload_to='images/%Y/%m/%d', verbose_name='Game image')
    pub_date = models.DateTimeField(verbose_name='Game publication date')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Post title')
    content = models.TextField(verbose_name='Post content')
    game = models.ForeignKey(Game, on_delete=models.PROTECT, verbose_name='Game')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Post publication time')
    last_update = models.DateTimeField(auto_now=True, verbose_name='Post last updated time')
    in_archive = models.BooleanField(default=False, verbose_name='Post is in archive')

    def __str__(self):
        return f'{self.id}. {self.title}'
