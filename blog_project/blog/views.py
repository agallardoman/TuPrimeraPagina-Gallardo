from django.shortcuts import render, redirect
from .models import Post, Categoria, Comentario
from .forms import PostForm, ComentarioForm, CategoriaForm
from django.db.models import Q

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'crear_post.html', {'form': form})

def buscar_post(request):
    if 'query' in request.GET:
        query = request.GET['query']
        posts = Post.objects.filter(Q(titulo__icontains=query) | Q(contenido__icontains=query))
    else:
        posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

