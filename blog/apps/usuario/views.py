from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

class RegistrarUsuario(CreateView):
    template_name = 'usuario/registro.html'
    form_class = RegistroUsuarioForm

    def form_valid(self, form):
        messages.success(self.request, 'Registro exitoso. Inicie sesión')
        form.save()

        return redirect ('apps.usuario:registro')
    
class LoginUsuario(LoginView):
    template_name  = 'usuario/login.html'

    def get_success_url(self):
        messages.success(self.request, 'Login exitoso')

        return reverse('apps.usuario:login')
    
class LogoutUsuario(LogoutView):
    template_name = 'usuario/logout.html'

    def get_success_url(self):
        messages.success(self.request, 'Logout exitoso')

        return reverse('apps.usuario:logout')