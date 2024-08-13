from django.db import models

class Pagina(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='paginas/')
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo
