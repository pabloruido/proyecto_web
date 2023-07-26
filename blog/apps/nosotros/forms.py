from django import forms
from .models import Nosotros

class NosotrosForm(forms.ModelForm):
    class Meta:
        model = Nosotros
        fields = ('titulo', 'descripcion', 'imagen')