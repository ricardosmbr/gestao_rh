from django.db import models
from apps.funcionarios.models import Funcionario

# Create your models here.
class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario,on_delete=models.CASCADE)
    def __str__(self):
        return self.descricao
