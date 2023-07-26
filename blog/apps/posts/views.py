from typing import Any, Dict
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comentario
from .forms import ComentarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseForbidden


class PostListView(ListView):
    model = Post
    template_name = "posts/posts.html"
    context_object_name = "posts"
    

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_individual.html"
    context_object_name = "posts"
    pk_url_kwarg = "id"
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        context['comentarios'] = Comentario.objects.filter(posts_id=self.kwargs['id'])
        return context
    
    def post (self, request, *args, **kwargs):
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.posts_id = self.kwargs['id']
            comentario.save()
            return redirect ('apps.posts:post_individual', id=self.kwargs['id'])
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
        
class ComentarioCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentarios/agregar_comentario.html'
    
    def get_success_url(self):
        post_id = self.kwargs['id']
        return reverse('apps.posts:post_individual', kwargs={'id': post_id})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_id'] = self.kwargs['id']
        return context

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.posts_id = self.kwargs ['id']
        return super().form_valid(form)
    


class ComentarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentarios/editarComentario.html'

    def get_success_url(self):
        return reverse('apps.posts:post_individual', kwargs={'id': self.object.posts_id})

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(usuario=self.request.user)
    

class ComentarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = 'comentarios/eliminarComentario.html'
    
    def get_success_url(self):
        return reverse('apps.posts:post_individual', kwargs={'id': self.object.posts_id})

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(usuario=self.request.user)
    
from django.views.generic.edit import DeleteView

class ComentarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = 'comentarios/eliminarComentario.html'
    
    def get_success_url(self):
        return reverse('apps.posts:post_individual', kwargs={'id': self.object.posts_id})

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(usuario=self.request.user)