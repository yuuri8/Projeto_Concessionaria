from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Veiculo
from .forms import VeiculoForm

# Create your views here.
def lista_veiculos(request):
    return render(request, 'veiculos\lista_veiculos.html', {'veiculos': Veiculo.objects.all()})

def novo_veiculo(request):
    form = VeiculoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/veiculos/')
    return render(request, 'veiculos\cadastro_veiculo.html', {'form': form, 'titulo': 'Novo Veículo'})


def editar_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    form = VeiculoForm(request.POST or None, request.FILES or None, instance=veiculo)
    if form.is_valid():
        form.save()
        return redirect('/veiculos/')
    return render(request, 'veiculos\cadastro_veiculo.html', {'form': form, 'titulo': 'Editar Veículo'})


def deletar_veiculo(request, id):
    Veiculo.objects.filter(id=id).delete()
    return redirect('/veiculos/')

def detalhes_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    return render(request, 'veiculos\detalhes_veiculo.html', {'veiculo': veiculo})