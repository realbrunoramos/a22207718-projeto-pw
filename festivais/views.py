from django.shortcuts import render
from .models import Festival

def lista_festivais(request):
    festivais = Festival.objects.all()
    return render(request, 'festivais/festivais.html', {'festivais': festivais})

def detalhes_festival(request, festival_id):
    festival = Festival.objects.get(id=festival_id)
    bandas = festival.bandas.all()
    return render(request, 'festivais/festival.html', {'festival': festival, 'bandas': bandas})
