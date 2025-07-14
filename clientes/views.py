from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError
from django.contrib import messages

@login_required
def lista_clientes(request):
    return render(request, 'clientes/clientes_lista.html', {'clientes': Cliente.objects.all()})

@login_required
def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/clientes_form.html', {'form': form})

@login_required
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        form =ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/clientes_form.html', {'form': form, 'cliente': cliente})

@login_required
def deletar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    try:
        cliente.delete()
        messages.success(request, 'Cliente deletado com sucesso.')
    except ProtectedError:
        messages.error(request, 'Não é possível excluir este cliente pois ele possui vendas associadas.')
    return redirect('listar_clientes')

@login_required
def detalhes_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'clientes/clientes_detalhe.html', {'cliente': cliente})