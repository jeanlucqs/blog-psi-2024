from django.shortcuts import render
from .models import Post

def index(request):
    return render(request, "index.html")

def help(request):
    return render(request, "help.html")

def sexuais(request):
    posts = Post.objects.all()
    context = {
        "posts" : posts,
    }
    return render(request, "sexuais.html", context)

def post(request, id):
    postagem = Post.objects.get(id = id)
    context = {
        "post" : postagem
    }
    print(postagem.carac)
    return render(request, "post.html", context)