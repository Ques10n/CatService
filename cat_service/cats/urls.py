from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import CatViewSet, UserCreate, index

router = DefaultRouter()
router.register('cats', CatViewSet, basename='cats')


urlpatterns = [
    path('register/', UserCreate.as_view(), name='auth_register'),
    path('', include(router.urls)),
    re_path('auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.authtoken')),
    re_path('chat/', index),
]
