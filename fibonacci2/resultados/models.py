from django.db import models
import uuid

# Create your models here.
class Resultado(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    numero_entrada = models.TextField()
    secuencia = models.TextField()

    def __str__(self):
        return self.id