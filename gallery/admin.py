from django.contrib import admin
from gallery.models import Photo, Favourite


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['photo', 'signature', 'author', 'created_at']
    ordering = ['-created_at']


class FavouritAdmin(admin.ModelAdmin):
    list_display = ['photo', 'accounts']


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Favourite, FavouritAdmin)

