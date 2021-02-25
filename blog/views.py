from django.db import models
from django.shortcuts import render
from blog.models import Post

# Create your views here.
def blog(request):
    posts=Post.objects.all()
    return render(request,'blog/template/blog/blog.html', {'posts': posts})