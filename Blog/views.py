
from django.shortcuts import render
from .models import BlogPost


# Create your views here.

def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'home.html')

def post_detail(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    return render(request, 'post_detail.html')