from django.urls import path
from . import views


app_name= "festivais"
urlpatterns = [
    path('', views.lista_festivais, name='lista_festivais'),
    path('festivais/<int:festival_id>/', views.detalhes_festival, name='detalhes_festival'),
]
