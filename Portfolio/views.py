from django.shortcuts import render, redirect


def meByme(request):
    return render(request, 'Portfolio/meByme.html')

def home(request):
    return render(request, 'Portfolio/home.html')

def WebWizardry(request):
    return render(request, 'Portfolio/WebWizardry.html')

def automation(request):
    return render(request, 'Portfolio/automation.html')

def projects(request):
    return render(request, 'Portfolio/projects.html')
