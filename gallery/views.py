from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from gallery.models import Photo
from gallery.forms import PhotoForm


class PhotoListView(ListView):
    template_name: str = 'gallery/photo_list.html'
    model = Photo
    context_object_name = 'photos'
    

class PhotoDetailView(DetailView):
    template_name = 'gallery/photo_detail.html'
    model = Photo
    context_object_name = 'photo'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     photo_form = PhotoForm()
    #     context['comment_form'] = photo_form
    #     return context


class PhotoCreateView(CreateView):
    template_name = 'gallery/photo_create.html'
    model = Photo
    fields = ['photo', 'signature']
    success_url = '/'

    def form_valid(self, form):
        self.object: Photo = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        return super().form_valid(form)
