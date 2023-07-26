from django.shortcuts import render
from .models import Nosotros

def nosotros(request):
    nosotros_info = Nosotros.objects.first()  
    return render(request, 'nosotros/nosotros.html', {'nosotros_info': nosotros_info})
