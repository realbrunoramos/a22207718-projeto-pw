from django.shortcuts import render, redirect
from django.contrib.auth import models, authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return render(request, 'authentication/user.html')
        else:
            return render(request, 'authentication/login.html', {
                'mensagem':'Credenciais inválidas'
            })
    return render(request, 'authentication/login.html')

def logout(request):
    logout(request)
    return redirect('authentication:login_view') 

def signin(request):
    if request.method == 'POST':
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        messages.success(request, 'Conta criada com sucesso! Faça login para continuar.')
        return redirect('authentication:login_view')
    return render(request, 'authentication/signin.html')

def recover_password(request):
    if request.method == 'POST':
        messages.success(request, 'Um e-mail de recuperação de senha foi enviado para o seu endereço.')
        return redirect('authentication:login_view')
    return render(request, 'authentication/recover_password.html')
