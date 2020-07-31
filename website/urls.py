from django.urls import path
from .views import my_post, home, create_post

urlpatterns = [
    path('', home, name='home'),
    path('mypost/', my_post, name='my_post'),
    path('create/', create_post, name='create')
]
