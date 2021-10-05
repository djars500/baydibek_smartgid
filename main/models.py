from django.db import models
from django.urls import reverse


class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Create your models here.
class Category(models.Model):
    name = models.CharField('Название', max_length=255)
    slug = models.SlugField(max_length=255)
    img = models.ImageField(upload_to='', default=0, blank=True, null=True)
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detailView', args=[self.slug])


class MediaCategory(models.Model):
    name = models.CharField('Название', max_length=255)
    slug = models.SlugField(max_length=255)
    img = models.ImageField(upload_to='', default=0, blank=True, null=True)


    class Meta:
        verbose_name = 'Медия категория'
        verbose_name_plural = 'Медиа категории'
        ordering = ['name']

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('mediaCategory_detailView', args=[self.slug])


class Posts(models.Model):
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    slug = models.SlugField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    img = models.ImageField(upload_to='', default=0, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse('post', args=[self.slug])

class PostMedia(models.Model):
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    slug = models.SlugField(max_length=255)
    media_category = models.ForeignKey(MediaCategory, on_delete=models.CASCADE, verbose_name='Категория')
    img = models.ImageField(upload_to='', default=0, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Пост Медиа'
        verbose_name_plural = 'Посты Медии'

    def get_absolute_url(self):
        return reverse('media_post', args=[self.slug])


class News(models.Model):
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    slug = models.SlugField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    date = models.DateField(auto_created=False)
    img = models.ImageField(upload_to='', default=0, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


