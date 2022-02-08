from django.shortcuts import render
# from .models import Instapic


# Create your views here.
def home(request):
    return render(request, 'home.html')

def user(request):
    return render(request, 'user.html')

def post(request):
    return render(request, 'post.html')

def each(request):
    return render(request, 'each.html')

def like(request):
    return render(request, 'like.html')

def save(request):
    return render(request, 'save.html')
