from django.urls import path
from .views import my_post, home

urlpatterns = [
    path('', home, name='home'),
    path('mypost/', my_post, name='my_post')
]
