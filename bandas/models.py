from django.db import models

class Musica(models.Model):
    titulo = models.CharField(max_length=100)
    album = models.ForeignKey('Album', on_delete=models.CASCADE, related_name='musicas')
    duracao = models.DurationField()
    link_spotify = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.titulo

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='bandas/', null=True, blank=True)

    def __str__(self):
        return self.nome

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    banda = models.ForeignKey('Banda', on_delete=models.CASCADE, related_name='albuns')
    lancamento = models.DateField()
    capa = models.ImageField(upload_to='capas/', null=True, blank=True)

    def __str__(self):
        return self.titulo
