from .models import Post
from django.shortcuts import render
from django.views.generic import ListView

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'

