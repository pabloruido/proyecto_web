from typing import Any, Dict
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comentario, Categoria
from .forms import ComentarioForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from django.http import HttpResponseForbidden
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.db.models import Q

def puede_postear(user):
    return user.is_superuser or user.has_perm('posts.puede_crear_post')

def puede_editar(user):
    return puede_postear(user)

def puede_eliminar(user):
    return puede_postear(user)

class PostListView(ListView):
    model = Post
    template_name = "posts/posts.html"
    context_object_name = "posts"
    
    def get_queryset(self):
        queryset = super().get_queryset()

        # Obtener parámetros de filtrado de la URL
        categoria_id = self.request.GET.get('categoria')
        orden_antiguedad = self.request.GET.get('antiguedad')
        orden_alfabetico = self.request.GET.get('alfabetico')

        # Aplicar filtros
        if categoria_id:
            queryset = queryset.filter(categoria__id=categoria_id)

        if orden_antiguedad == 'asc':
            queryset = queryset.order_by('publicado')
        elif orden_antiguedad == 'desc':
            queryset = queryset.order_by('-publicado')

        if orden_alfabetico == 'asc':
            queryset = queryset.order_by('titulo')
        elif orden_alfabetico == 'desc':
            queryset = queryset.order_by('-titulo')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()

        context['puede_crear_post'] = puede_postear(self.request.user)
        
        
        return context


@login_required
@user_passes_test(puede_postear)
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            nueva_categoria = form.cleaned_data.get('nueva_categoria', '')
            if nueva_categoria:
                categoria_existente = Categoria.objects.filter(nombre=nueva_categoria).first()
                if not categoria_existente:
                    nueva_categoria_obj = Categoria(nombre=nueva_categoria)
                    nueva_categoria_obj.save()
                    form.instance.categoria = nueva_categoria_obj
                else:
                    form.instance.categoria = categoria_existente
            post = form.save(commit=False)
            post.publicado = timezone.now()
            post.save()
            messages.success(request, 'El post se ha creado correctamente.')
            return redirect('apps.posts:post_individual', id=post.id)
    else:
        form = PostForm()
    return render(request, 'posts/crear_post.html', {'form': form})


@login_required
@user_passes_test(puede_editar)
def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('apps.posts:post_individual', id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/editar_post.html', {'form': form})

@login_required
@user_passes_test(puede_eliminar)
def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        messages.success(request, 'El post se ha eliminado correctamente.')
        return redirect('apps.posts:posts')

    return render(request, 'posts/eliminar_post.html', {'post': post})


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

        context['puede_crear_post'] = puede_postear(self.request.user)
        context['puede_editar_post'] = puede_editar(self.request.user)
        context['puede_eliminar_post'] = puede_eliminar(self.request.user)
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
    




def buscar_post(request):
    query = request.GET.get('query')
    posts = Post.objects.all()
    
    if query:
        posts = posts.filter(
            Q(titulo__icontains=query) |
            Q(subtitulo__icontains=query) |
            Q(texto__icontains=query) |
            Q(categoria__nombre__icontains=query))
        
    no_results = not bool(posts) 
    
    context = {
        'query': query,
        'posts': posts,
        'no_results': no_results,
    }
    
    if no_results:
        context['posts'] = Post.objects.all()
    
    return render(request, 'posts/resultado_busqueda.html', context)
