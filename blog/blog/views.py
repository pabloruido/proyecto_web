from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from apps.posts.models import Post
from django.views.generic import ListView

def index(request):
    return render(request, 'index.html')

# def PostRecentListView(request):
#     posts = Post.objects.all().order_by('-fecha')[0:3]
#     template = 'index.html'
#     contexto = {
#         'posts_recientes':
#     }
