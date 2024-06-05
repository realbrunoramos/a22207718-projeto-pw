from django.shortcuts import render, redirect
from .models import Curso,disciplina,projeto



def login_view(request):
    return redirect('authentication/login')

def intro_view(request):
    cursos = Curso.objects.all()
    context = {
        'cursos': cursos
    }
    return render(request, 'curso/intro.html', context)


def todasDisciplinas_view(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    disciplinas = disciplina.objects.all()
    return render(request, 'curso/todasDisciplinas.html', {'curso': curso, 'disciplinas': disciplinas})


def disciplina_details(request, disciplina_id):
    disciplina1 = disciplina.objects.get(id=disciplina_id)
    projetos = disciplina1.projetos.all()
    return render(request, 'curso/disciplina_details.html', {'disciplina': disciplina1, 'projetos': projetos})

def project_details(request, project_id):
    project = projeto.objects.get(id=project_id)
    return render(request, 'curso/project_details.html', {'project': project})

def projetos_view(request):
    projetos = projeto.objects.all().order_by('ano')
    return render(request, 'curso/projetos.html', {'projetos': projetos})

