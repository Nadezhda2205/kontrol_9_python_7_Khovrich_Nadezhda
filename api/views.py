from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse

from gallery.models import Photo
from api.serializers import PhotoSerializer


class PhotoApiView(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def photo_to_favorite(self, request, *args, **kwargs):
        photo_by_pk = self.get_object()
        user_from_request = request.user
        user_from_request.favourited_photos.add(photo_by_pk)
        return JsonResponse({'key': 'aaaaa'})
    
    def photo_from_favorite(self, request, *args, **kwargs):
        photo_by_pk = self.get_object()
        user_from_request = request.user
        user_from_request.favourited_photos.remove(photo_by_pk)
        return JsonResponse({'key': 'aaaaa'})
