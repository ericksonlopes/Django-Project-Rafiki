from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Post


@login_required(login_url='login')
def home(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def my_post(request):
    posts = Post.objects.all()
    return render(request, 'rafiki_home/my_post.html', {'posts': posts})
