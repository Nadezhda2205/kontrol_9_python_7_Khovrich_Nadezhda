from django import forms
from gallery.models import Photo


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('photo', 'signature')

class PhotoUpdateForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('signature', )
        