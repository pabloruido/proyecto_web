from django import forms
from .models import Comentario, Post

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']



class PostForm(forms.ModelForm):
    nueva_categoria = forms.CharField(label='Nueva Categoría', max_length=30, required=False)
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'texto', 'categoria', 'imagen']

