from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
    )
from .models import Post

# Create your views here.
class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post


class PostDetailView(DetailView):
    template_name= "posts/detail.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title",
        "subtitle",
        "body",
        "author"
        ]

class PostUpdateView(UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ['title', 'subtitle', 'body']

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = "http://127.0.0.1:8000/posts/"