from django.shortcuts import render, redirect, get_object_or_404
from .models import Funcionario
from .forms import FuncionarioForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required

def home(request):
    return render(request, 'dashboard.html')

def listar_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionarios/funcionarios_lista.html', {'funcionarios': funcionarios})

def criar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/funcionarios/')
    else:
        form = FuncionarioForm()
    return render(request, 'funcionarios/funcionarios_form.html', {'form': form})

def editar_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    if request.method == 'POST':
        form =FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('listar_funcionarios')
    else:
        form = FuncionarioForm(instance=funcionario)
    return render(request, 'funcionarios/funcionarios_form.html', {'form': form, 'funcionario': funcionario})

def deletar_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    funcionario.delete()
    return redirect('listar_funcionarios')

def detalhes_funcionarios(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    return render(request, 'funcionarios/funcionarios_detalhe.html', {'funcionario': funcionario})
    