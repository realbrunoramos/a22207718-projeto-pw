from django.shortcuts import render


def aboutme_view(request):
    return render(request, "novaapp/aboutme.html")

def index_view(request):
    return render(request, "novaapp/index.html")

def myworks_view(request):
    return render(request, "novaapp/myworks.html")