from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Post


# @login_required(login_url='login')
def home(request):
    posts = Post.objects.all()
    return render(request, 'rafiki_home/home.html', {'posts': posts})


@login_required(login_url='login')
def my_post(request):
    posts = Post.objects.filter(user=request.user.id)
    return render(request, 'rafiki_home/my_post.html', {'posts': posts})


@login_required(login_url='login')
def create_post(request):
    pass