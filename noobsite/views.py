from django.shortcuts import render

# noobsite/views.py
from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def about_view(request):
    return HttpResponse("Bem-vindo à página Sobre nós!")

def contact_view(request):
    return HttpResponse("Entre em contato conosco através do e-mail: contato@noobsite.com")

def products_view(request):
    products = ["Produto 1", "Produto 2", "Produto 3"]
    products_str = ", ".join(products)
    return HttpResponse(f"Nossos produtos disponíveis: {products_str}")