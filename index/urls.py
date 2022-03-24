from django.urls import URLPattern, path
from .views import index, plantilla

urlpatterns = [
    path('', index, name='index'),
    path('plantilla/', plantilla, name='plantilla'),
]