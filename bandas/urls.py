from django.urls import path
from . import views

app_name = 'bandas'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registo/', views.registo_view, name='registo'),
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('albuminfo/<int:album_id>/', views.albuminfo_view, name='albuminfo'),
    path('musicainfo/<int:musica_id>/', views.musicainfo_view, name='musicainfo'),
    path('bandalbuns/<int:banda_id>/', views.bandalbuns_view, name='bandalbuns'),
]
