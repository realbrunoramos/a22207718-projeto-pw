# noobsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

urlpatterns = [
    path('index/', views.index_view),
    path('about/', views.about_view),
    path('contact/', views.contact_view),
    path('products/', views.products_view),
]