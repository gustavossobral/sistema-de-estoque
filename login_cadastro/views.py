from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User 
from django.contrib import auth, messages

def login(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )

        if usuario is not None:
            auth.login(request,usuario)
            return redirect('mostrar_estoque')
        else:
            return redirect('login')
    return render(request,'login_cadastro/login.html')#, {'form':form})

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():

            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha_1 = form['senha_1'].value()
            senha_2 = form['senha_2'].value()

            if senha_1 != senha_2:
                messages.error(request, 'As senhas não coincidem.')
                return redirect('cadastro')

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Nome de usuário já existe.')
                return redirect('cadastro')

            if User.objects.filter(email=email).exists():
                messages.error(request, 'E-mail já está em uso.')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha_1,
            )
            usuario.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('login')
        else:
            messages.error(request, 'Erro no formulário. Verifique os dados.')
    else:
        form = CadastroForms()

    return render(request, 'login_cadastro/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request,'Logout efetuado com sucesso!')
    return redirect('login')