from django.contrib import admin
from gallery.models import Photo, Favourites

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['photo', 'signature', 'author', 'created_at']
    ordering = ['-created_at']


class FavouritAdmin(admin.ModelAdmin):
    list_display = ['photo', 'author', 'photo']


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Favourites, FavouritAdmin)