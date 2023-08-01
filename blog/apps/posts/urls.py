from django.urls import path
from .views import PostListView, PostDetailView, ComentarioUpdateView, ComentarioDeleteView,ComentarioCreateView
from . import views

app_name = 'apps.posts'

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:id>/', PostDetailView.as_view(), name = 'post_individual'),
    path('comentario/editar/<int:pk>/', ComentarioUpdateView.as_view(), name='comentario_editar'),
    path('comentario/eliminar/<int:pk>/', ComentarioDeleteView.as_view(), name='comentario_eliminar'),
    path('comentario/agregar/<int:id>/', ComentarioCreateView.as_view(), name='comentario_agregar'),
    path('crear/', views.crear_post, name='crear_post'),
    path('editar/<int:pk>/', views.editar_post, name='editar_post'),
    path('buscar/', views.buscar_post, name='buscar'),
    
]
