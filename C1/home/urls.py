from django.urls import path
from .views import home, user, hello, age

urlpatterns = [
   path('', home, name='home'),
   path('user/', user, name='user'),
   path('hello/<str:name>', hello, name='hello'),
   path('age/<int:age>', age, name='age'),
]
