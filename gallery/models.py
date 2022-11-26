from django.db import models
from django.contrib.auth import get_user_model


class Photo(models.Model):
    photo = models.ImageField(verbose_name='Фото', upload_to='photo')
    signature = models.CharField(verbose_name='Подпись', null=False, blank=False, max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(), 
        related_name= 'author', 
        null=False, 
        blank=False,
        on_delete=models.CASCADE
        )

    class Meta():
        ordering = ['-created_at']


class Favourite(models.Model):
    photo = models.ForeignKey(
        verbose_name='Фотография',
        to='gallery.Photo',
        related_name='photos',
        null=False,
        blank=False,
        on_delete=models.CASCADE
        )
    accounts = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        related_name='favourites',
        null=False,
        blank=False,
        on_delete=models.CASCADE
        )

    created_at = models.DateTimeField(auto_now_add = True)

    class Meta():
        ordering = ['created_at']

