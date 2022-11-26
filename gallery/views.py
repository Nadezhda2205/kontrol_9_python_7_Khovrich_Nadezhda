from django.shortcuts import render
from django.views.generic import ListView
from accounts.models import Account

from gallery.models import Photo


class PhotoListView(ListView):
    template_name: str = 'gallery/list_photo.html'
    model = Photo
    context_object_name = 'photos'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            return context
        print(self.request.user.is_authenticated)
        user: Account = self.request.user
        subscriptions = user.subscriptions.all()
        posts = Photo.objects.all()
        subscriptions_posts = posts.filter(author__in = subscriptions)
        context['photo'] = subscriptions_posts

        return context

