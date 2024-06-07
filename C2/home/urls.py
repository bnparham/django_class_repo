from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home-page'),
    path('<str:name>', home, name='home-page-2'),
]
