from django.urls import path, include
from rest_framework import routers
from api.views import PhotoApiView


router = routers.DefaultRouter()
router.register('photo', PhotoApiView)

urlpatterns = [
    path('', include(router.urls)),
    path('photo/<int:pk>/tofav/', PhotoApiView.as_view({'get': 'photo_to_favorite'})),
    path('photo/<int:pk>/fromfav/', PhotoApiView.as_view({'get': 'photo_from_favorite'})),
]
