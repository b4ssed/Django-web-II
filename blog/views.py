from django.shortcuts import render
from django.views.generic import ListView, DetailView

# blog/views.py
from django.views.generic import ListView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
