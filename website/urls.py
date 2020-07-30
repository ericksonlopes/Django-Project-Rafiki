from django.urls import path
from .views import home, my_post

urlpatterns = [
    path('', home, name='home'),
    path('mypost/', my_post, name='my_post')
]
