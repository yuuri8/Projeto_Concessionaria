from django.shortcuts import render
from veiculos.models import Veiculo
from clientes.models import Cliente
from funcionarios.models import Funcionario
from vendas.models import Venda
from testdrive.models import TestDrive

from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth
from datetime import datetime

def dashboard(request):
    total_veiculos = Veiculo.objects.count()
    veiculos_disponiveis = Veiculo.objects.filter(disponivel=True).count()
    veiculos_vendidos = Venda.objects.count()
    total_clientes = Cliente.objects.count()
    testdrives_pendentes = TestDrive.objects.filter(status='pendente').count()
    testdrives_realizados = TestDrive.objects.filter(status='realizado').count()
    total_vendas = Venda.objects.aggregate(total=Sum('valor'))['total'] or 0

    # Vendas por mês (últimos 6 meses)
    vendas_por_mes = (
        Venda.objects
        .annotate(mes=TruncMonth('data'))
        .values('mes')
        .annotate(total=Count('id'))
        .order_by('mes')
    )
    labels = [v['mes'].strftime('%b/%Y') for v in vendas_por_mes]
    valores = [v['total'] for v in vendas_por_mes]

    contexto = {
        'total_veiculos': total_veiculos,
        'veiculos_disponiveis': veiculos_disponiveis,
        'veiculos_vendidos': veiculos_vendidos,
        'total_clientes': total_clientes,
        'testdrives_pendentes': testdrives_pendentes,
        'testdrives_realizados': testdrives_realizados,
        'total_vendas': total_vendas,
        'grafico_labels': labels,
        'grafico_dados': valores,
    }

    return render(request, 'dashboard.html', contexto)