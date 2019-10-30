from django.db import models

# Create your models here.
class Registro_hora_extra(models.Model):
    motivo = models.CharField(max_length=100)

    def __str__(self):
        return self.motivo

