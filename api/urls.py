from django.urls import path, include
from rest_framework import routers
from api.views import PhotoApiView


router = routers.DefaultRouter()
router.register('posts', PhotoApiView)

urlpatterns = [
    path('', include(router.urls)),
    path('photo/<int:pk>/favourite/', PhotoApiView.as_view({'get': 'liked_users'})),
    path('posts/<int:pk>/fromfavorite/', PhotoApiView.as_view({'get': 'commented_users'})),
]
