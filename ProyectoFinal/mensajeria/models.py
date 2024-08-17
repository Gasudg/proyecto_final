from django.db import models
from django.contrib.auth.models import User
from paginas.models import Pagina  # Importa el modelo de página

class Comentario(models.Model):
    pagina = models.ForeignKey(Pagina, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.pagina.titulo}"
