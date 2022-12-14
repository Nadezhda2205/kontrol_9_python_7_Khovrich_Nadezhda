from rest_framework import serializers
from gallery.models import Photo

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        exclude = ('created_at', 'signature')
