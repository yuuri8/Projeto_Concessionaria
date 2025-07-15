from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Veiculo
from .forms import VeiculoForm
from django.contrib.auth.decorators import login_required
from veiculos.decorators import permissao_requerida
from django.db.models import ProtectedError
from django.contrib import messages


# Create your views here.
@login_required
def lista_veiculos(request):
    return render(request, 'veiculos/lista_veiculos.html', {'veiculos': Veiculo.objects.all()})

@login_required
def novo_veiculo(request):
    form = VeiculoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/veiculos/')
    return render(request, 'veiculos/cadastro_veiculo.html', {'form': form, 'titulo': 'Novo Veículo'})

@login_required
def editar_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    form = VeiculoForm(request.POST or None, request.FILES or None, instance=veiculo)
    if form.is_valid():
        form.save()
        return redirect('/veiculos/')
    return render(request, 'veiculos/cadastro_veiculo.html', {'form': form, 'titulo': 'Editar Veículo'})

@login_required
@permissao_requerida('admin')
def deletar_veiculo(request, id):
    try:
        Veiculo.objects.filter(id=id).delete()
        messages.success(request, 'Veículo deletado com sucesso.')
    except ProtectedError:
        messages.error(request, 'Não é possível excluir este veículo pois ele está associado a uma venda.')
    return redirect('/veiculos/')

@login_required
def detalhes_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    return render(request, 'veiculos/detalhes_veiculo.html', {'veiculo': veiculo})