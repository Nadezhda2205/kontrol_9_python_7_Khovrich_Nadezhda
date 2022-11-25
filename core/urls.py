from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from accounts.views import IndexView, LoginView, logout_view, RegisterView, AccountDetailView, AccountUpdateView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('<str:slug>', AccountDetailView.as_view(), name='account_detail'),
    path('<str:slug>/update', AccountUpdateView.as_view(), name='account_update'),

    path('api/', include('api.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
