from django.db import models
from datetime import date

class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.nome

class Artigo(models.Model):
    titulo = models.CharField(max_length=200, null=True, blank=True)
    conteudo = models.TextField(null=True, blank=True)  
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True) 
    autor = models.CharField(max_length=100, null=True, blank=True)
    data_publicacao = models.DateField(default=date.today)

    def __str__(self):
        return self.titulo
