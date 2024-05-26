from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib import messages, auth
from django.contrib.auth.models import User

def login(request):
    form = LoginForms()

    if request.method == "POST":
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form["nome_login"].value()
            senha = form["senha"].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha,
        )

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f"{nome} logado com sucesso !")
            return redirect("index")
        
        else:
            messages.error(request, "Algo deu errado, verifique suas informaçoes .")
            return redirect("login")

    return render(request, "usuarios/login.html", {"form": form})


def cadastro(request):
    form = CadastroForms()

    if request.method == "POST":
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form['senha'].value() != form['confirma_senha'].value():
                messages.error(request, "As senhas nao conferem !")
                return redirect("cadastro")
            
            nome = form["nome_usuario"].value()
            email = form["email"].value()
            senha = form["senha"].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, "Usuario ja existente !")
                return redirect("cadastro")
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, f"Cadastro efetuado com sucesso ! Faça Login ")
            return redirect("login")
            
    return render(request, "usuarios/cadastro.html", {"form": form})


def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado !")
    return redirect('login')