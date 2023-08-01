from django.urls import path
from . import views

app_name = 'apps.nosotros'

urlpatterns = [
    path('nosotros/', views.nosotros, name='nosotros'),
]