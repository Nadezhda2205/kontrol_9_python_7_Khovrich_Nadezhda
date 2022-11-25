from django.db import models

from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
    
    def __str__(self) -> str:
        return self.name
