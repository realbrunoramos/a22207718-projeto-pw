from django.shortcuts import render, get_object_or_404, redirect
from .models import Artigo

def login_view(request):
    return redirect('authentication/login')

def lista_artigos(request):
    artigos = Artigo.objects.all()
    return render(request, 'artigos/lista_artigos.html', {'artigos': artigos})

def detalhes_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, pk=artigo_id)
    return render(request, 'artigos/detalhes_artigo.html', {'artigo': artigo})
