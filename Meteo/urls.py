from django.urls import path
from . import views

app_name = 'Meteo'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registo/', views.registo_view, name='registo'),
    path('', views.home, name='home'),
    path('next_days/', views.fiveDays, name='fiveDays'),
]
