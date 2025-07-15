from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import TestDrive
from .forms import TestDriveForm
from clientes.models import Cliente
from veiculos.models import Veiculo
from funcionarios.models import Funcionario
from django.contrib.auth.decorators import login_required
from testdrive.decorators import permissao_requerida

@login_required
def listar_testdrives(request):
    testdrive = TestDrive.objects.all()
    return render(request, 'testdrive/testdrive_lista.html', {'testdrive': testdrive})

@login_required
def criar_testdrive(request):
    if request.method == 'POST':
        form = TestDriveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_testdrives')
    else:
        form = TestDriveForm()

    context = {
        'form': form,
        'clientes': Cliente.objects.all(),
        'veiculos': Veiculo.objects.all(),
        'funcionarios': Funcionario.objects.all()
    }
    return render(request, 'testdrive/testdrive_form.html', context)

@login_required
def editar_testdrive(request, testdrive_id):
    testdrive = get_object_or_404(TestDrive, id=testdrive_id)

    if request.method == 'POST':
        form = TestDriveForm(request.POST, instance=testdrive)
        if form.is_valid():
            form.save()
            return redirect('listar_testdrives')
    else:
        form = TestDriveForm(instance=testdrive)

    context = {
        'form': form,
        'testdrive': testdrive,
        'clientes': Cliente.objects.all(),
        'veiculos': Veiculo.objects.all(),
        'funcionarios': Funcionario.objects.all()
    }
    return render(request, 'testdrive/testdrive_form.html', context)

@login_required
@permissao_requerida('admin')
def deletar_testdrive(request, testdrive_id):
    testdrive = get_object_or_404(TestDrive, id=testdrive_id)
    testdrive.delete()
    return redirect('listar_testdrives')

@login_required
def detalhes_testdrive(request, testdrive_id):
    testdrive = get_object_or_404(TestDrive, id=testdrive_id)
    return render(request, 'testdrive/testdrive_detalhe.html', {'testdrive': testdrive})