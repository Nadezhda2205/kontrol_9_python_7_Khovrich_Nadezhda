from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from accounts.views import LoginView, logout_view, RegisterView, AccountDetailView, AccountUpdateView
from gallery.views import PhotoListView, PhotoDetailView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PhotoListView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    
    path('<str:slug>', AccountDetailView.as_view(), name='account_detail'),
    path('<str:slug>/update', AccountUpdateView.as_view(), name='account_update'),

    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('photo/add/', PhotoCreateView.as_view(), name='photo_create'),
    path('photo/edit/<int:pk>', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/delete/<int:pk>', PhotoDeleteView.as_view(), name='photo_delete'),

    path('api/', include('api.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
