from django.db import models

from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    description = models.TextField(null=True, blank=True)
    favourited_photos = models.ManyToManyField(
        verbose_name='Избранные фото',
        to='gallery.Photo',
        through='gallery.Favourite',
        related_name='favourited_users'
        )
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
    
    def __str__(self) -> str:
        return self.name
