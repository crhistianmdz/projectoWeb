from django.db import models
from django.shortcuts import render
from blog.models import Post, Categoria

# Create your views here.
def blog(request):
    posts=Post.objects.all()
    return render(request,'blog/template/blog/blog.html', {'posts': posts})

def categoria(request,categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request,'blog/template/blog/categoria.html', {'categoria':categoria, "posts":posts})