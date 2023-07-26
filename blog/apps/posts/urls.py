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
    
]
