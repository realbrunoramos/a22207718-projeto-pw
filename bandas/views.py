from bandas.models import Album, Banda, Musica
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse

def login_view(request):
    return redirect('authentication/login')

def registo_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('pagina_inicial')
    else:
        form = UserCreationForm()
    return render(request, 'bandas/registo.html', {'form': form})


def albuminfo_view(request, album_id):
    album = Album.objects.get(id=album_id)
    context = {
        'album': album,
        'musicas': album.musicas.all(),
    }
    return render(request, "bandas/albumInfo.html", context)

def musica_favorita(request):
    return render(request, 'bandas/musica_favorita.html')

def pagina_inicial(request):
    bandas = Banda.objects.all().order_by('-nome')
    context = {'bandas': bandas}
    return render(request, 'bandas/paginaInicial.html', context)

def bandas_json_view(request):
    bandas = Banda.objects.all()
    bandas_nomes = [banda.nome for banda in bandas]
    return JsonResponse({'bandas': bandas_nomes})

def musicainfo_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    context = {'musica': musica}
    return render(request, 'bandas/musicaInfo.html', context)


def bandalbuns_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    albuns = banda.albuns.all()
    numMusics = 0
    for album in albuns:
        numMusics += album.musicas.count()
    context = {
        'banda': banda,
        'albuns': albuns,
        'numAlbuns': len(albuns),
        'numMusicas': numMusics,
    }
    return render(request, "bandas/bandaAlbuns.html", context)
