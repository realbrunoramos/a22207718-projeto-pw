from django.urls import path
from . import views

app_name = 'Portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('meByme/', views.meByme, name='meByme'),
    path('WebWizardry/', views.WebWizardry, name='WebWizardry'),
    path('automation/', views.automation, name='automation'),
    path('projects/', views.projects, name='projects'),
]
