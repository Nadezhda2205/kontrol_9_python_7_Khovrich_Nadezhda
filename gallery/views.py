from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from gallery.models import Photo
from gallery.forms import PhotoForm, PhotoUpdateForm


class PhotoListView(ListView):
    template_name: str = 'gallery/photo_list.html'
    model = Photo
    context_object_name = 'photos'
    
    

class PhotoDetailView(DetailView):
    template_name = 'gallery/photo_detail.html'
    model = Photo
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.groups.filter(name='photo_edit').exists():
            context['has_edit_permission'] = True
        if self.request.user.groups.filter(name='photo_del').exists():
            context['has_del_permission'] = True
        return context

class PhotoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'gallery/photo_create.html'
    model = Photo
    form_class = PhotoForm
    success_url = '/'

    def form_valid(self, form):
        self.object: Photo = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        return super().form_valid(form)

class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'gallery/photo_update.html'

    form_class = PhotoUpdateForm
    model = Photo
    context_object_name = 'photos'

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not (self.get_object().author == request.user or request.user.groups.filter(name='photo_edit').exists()):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)   

    def dispatch(self, request, *args, **kwargs):
        if not (self.get_object().author == request.user or request.user.groups.filter(name='photo_del').exists()):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)



