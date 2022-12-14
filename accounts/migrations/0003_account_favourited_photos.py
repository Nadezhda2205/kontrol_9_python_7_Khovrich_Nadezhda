# Generated by Django 4.1.3 on 2022-11-26 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_remove_favourite_author_favourite_accounts'),
        ('accounts', '0002_alter_account_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='favourited_photos',
            field=models.ManyToManyField(related_name='favourited_users', through='gallery.Favourite', to='gallery.photo', verbose_name='Избранные фото'),
        ),
    ]
