from django.db import models

# Create your models here.
class Artist(models.Model):
    artisticName = models.CharField(max_length=30)
    bandName = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.artisticName}'