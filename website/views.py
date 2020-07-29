from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# @login_required(login_url='login')
def home(request):
    return render(request, 'index.html')
