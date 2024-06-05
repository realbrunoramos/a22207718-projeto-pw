from django.urls import path
from . import views


app_name='artigos'
urlpatterns = [
    path('', views.lista_artigos, name='lista_artigos'),
    path('login/', views.login_view, name='login'),
    path('artigo/<int:artigo_id>/', views.detalhes_artigo, name='detalhes_artigo'),
]
