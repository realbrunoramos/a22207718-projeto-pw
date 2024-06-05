from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'novaapp'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('aboutme/', views.aboutme_view, name='aboutme'),
    path('myworks/', views.myworks_view, name='myworks'),
]