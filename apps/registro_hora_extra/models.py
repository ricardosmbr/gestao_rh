from django.db import models
from apps.funcionarios.models import Funcionario

# Create your models here.
class Registro_hora_extra(models.Model):
    motivo = models.CharField(max_length=100)
    hora_extra = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    def __str__(self):
        return self.motivo

