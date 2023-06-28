from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.template.defaultfilters import slugify

from classroom.models import Lesson

from accounts.validations import (
    empty_field,
    registered_account,
    different_passwords,
    password_greater_than_eight,
)


def signup(request):
    template_name = 'accounts/signup.html'
    if request.method == 'POST':
        nome = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        error_count = 0
        if empty_field(nome):
            messages.error(request, 'Campo nome é obrigratório!')
            error_count += 1
        if empty_field(email):
            messages.error(request, 'Campo email é obrigratório!')
            error_count += 1
        if registered_account(nome, email):
            messages.error(request, 'Usuário já é cadastrado!')
            error_count += 1
        if empty_field(password):
            messages.error(request, 'Campo senha é obrigratório!')
            error_count += 1
        if different_passwords(password, password_confirm):
            messages.error(request, 'As senhas devem ser iguais!')
            error_count += 1
        if not password_greater_than_eight(password, password_confirm):
            messages.error(request, 'A senha deve ter no minimo 8 caracteres')
            error_count += 1
        if error_count > 0:
            return redirect('signup')
        else:
            user = User.objects.create_user(
                username=nome, email=email, password=password
            )
            user.is_active = True
            user.is_staff = True
            user.user_permissions
            user.save()
            messages.success(
                request, f'Usuário {user.username} cadastrado com sucesso!'
            )
            return redirect('login')
    else:
        return render(request, template_name)


def login(request):
    template_name = 'accounts/login.html'
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if empty_field(email) or empty_field(password):
            messages.error(request, 'Todos os campos são obrigatórios!')
            return redirect('login')

        if User.objects.filter(email=email).exists():
            nome = (
                User.objects.filter(email=email)
                .values_list('username', flat=True)
                .get()
            )
            user = auth.authenticate(
                request=request, username=nome, password=password
            )

            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('dashboard')

    return render(request, template_name)


def dashboard(request):
    template_name = 'accounts/dashboard.html'
    if not request.user.is_authenticated:
        messages.error(
            request, "Realize login para acessar a página 'Minhas Salas'!"
        )
        return redirect('login')

    lesson = Lesson.objects.filter(autor=request.user.id).order_by('criado_em')

    dados = {'lesson': lesson}

    return render(request, template_name, dados)


def logout(request):
    auth.logout(request)
    messages.success(
        request,
        'Sessão encerrada! Obrigado por passar algum tempo de qualidade com o Write A Class'
    )
    return redirect('login')
