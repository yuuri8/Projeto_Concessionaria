from django.shortcuts import render, redirect, get_object_or_404
from .models import Venda
from .forms import VendaForm



def lista_vendas(request):
    return render(request, 'vendas/lista_vendas.html', {'vendas': Venda.objects.all()})


def nova_venda(request):
    form = VendaForm(request.POST or None)
    if form.is_valid():
        venda = form.save()
        veiculo = venda.veiculo
        veiculo.disponivel = False
        veiculo.save()
        return redirect('/vendas/')
    return render(request, 'vendas/cadastro_venda.html', {'form': form})

def editar_venda(request, id):
    venda = get_object_or_404(Venda, id=id)
    form = VendaForm(request.POST or None, request.FILES or None, instance=venda)
    if form.is_valid():
        form.save()
        return redirect('/vendas/')
    return render(request, 'vendas/cadastro_venda.html', {'form': form, 'venda': venda})

def detalhes_venda(request, id):
    venda = get_object_or_404(Venda, id=id)
    return render(request, 'vendas/detalhes_venda.html', {'venda': venda})

def deletar_venda(request, id):
    Venda.objects.filter(id=id).delete()
    return redirect('/vendas/')