
from django.urls import path
from . import views


app_name = 'curso'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.intro_view, name='intro_view'),
    path('curso/<int:curso_id>/', views.todasDisciplinas_view, name='disciplinas'),
    path('projetos/', views.projetos_view, name='projetos_view'),
    path('disciplina/<int:disciplina_id>/', views.disciplina_details, name='disciplina_details'),
    path('project/<int:project_id>/', views.project_details, name='project_details'),

]