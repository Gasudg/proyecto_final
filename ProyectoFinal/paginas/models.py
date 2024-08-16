from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField

class Pagina(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=100)
    cuerpo = RichTextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField(default=timezone.now)
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)  # Solo admins pueden subir imágenes

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('pagina_detalle', kwargs={'pk': self.pk})