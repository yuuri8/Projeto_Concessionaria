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
