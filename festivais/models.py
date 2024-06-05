from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Localizacao(models.Model):
    cidade = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.cidade}, {self.pais}"

class Festival(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE, related_name='festivais')
    bandas = models.ManyToManyField(Banda, related_name='festivais')
    link_festival = models.URLField(null=True, blank=True)
    foto = models.ImageField(upload_to='festivais/', null=True, blank=True)

    def __str__(self):
        return self.nome

