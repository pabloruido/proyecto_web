from django.db import models

# Create your models here.

class Nosotros (models.Model):
    titulo = models.CharField (max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(null=True, blank=True, upload_to='media', default='static/post_default.png')

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Nosotros'   
        verbose_name_plural = 'Nosotros'
