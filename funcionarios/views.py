from django.shortcuts import render, redirect, get_object_or_404
from .models import Funcionario
from .forms import FuncionarioForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from .decorators import permissao_requerida
from django.db.models import ProtectedError

@login_required
def home(request):
    return render(request, 'dashboard.html')

@login_required
@permissao_requerida('admin')
def listar_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionarios/funcionarios_lista.html', {'funcionarios': funcionarios})


@login_required
def criar_funcionario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        permissao = request.POST.get('permissao')

        if not all([nome, email, senha, permissao]):
            messages.error(request, "Todos os campos são obrigatórios.")
            return redirect('criar_funcionario')

        if User.objects.filter(username=nome).exists():
            messages.error(request, "Já existe um usuário com esse e-mail.")
            return redirect('criar_funcionario')

        user = User.objects.create_user(username=nome, email=email, password=senha)

        # AQUI dá erro se o modelo não estiver certo
        Funcionario.objects.create(
            usuario=user,
            nome=nome,
            permissao=permissao
        )

        return redirect('listar_funcionarios')

    return render(request, 'funcionarios/funcionarios_form.html', {})


@login_required
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

@login_required
def deletar_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    usuario = funcionario.usuario
    try:
        funcionario.delete()
        usuario.delete()
        messages.success(request, 'Funcionário deletado com sucesso.')
    except ProtectedError:
        messages.error(request, 'Não é possível excluir este funcionário pois ele possui vendas associadas.')
    return redirect('listar_funcionarios')

@login_required
def detalhes_funcionarios(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    return render(request, 'funcionarios/funcionarios_detalhe.html', {'funcionario': funcionario})



    