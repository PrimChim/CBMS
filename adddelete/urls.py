from .views import add
from django.urls import path


urlpatterns = [
    path('add/', add, name='add'),
]