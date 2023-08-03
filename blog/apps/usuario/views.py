from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import Group

class RegistrarUsuario(CreateView):
    template_name = 'usuario/registro.html'
    form_class = RegistroUsuarioForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Registro exitoso. Inicie sesión')
        group = Group.objects.get(name='Registrado')
        self.object.groups.add(group)
        return redirect ('apps.usuario:login')
    
class LoginUsuario(LoginView):
    template_name  = 'usuario/login.html'

    def get_success_url(self):
        messages.success(self.request, 'Login exitoso')

        return reverse('index')
    
class LogoutUsuario(LogoutView):

    def get_success_url(self):
        messages.success(self.request, 'Logout exitoso')

        return reverse('index')
