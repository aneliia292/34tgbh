from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('test/', index, name='text'),
    path('image/', imageView, name='image'),
]