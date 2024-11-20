
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Funcionario, RegistroPonto
from .forms import FuncionarioForm
from django.contrib import messages
from django.utils.timezone import now  # Usa `now` para lidar corretamente com fusos horários.
from django.contrib.auth.decorators import login_required


# Página inicial
def index(request):
    return render(request, 'index.html')

# Listar Funcionários
@login_required
def listar_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'listar_funcionarios.html', {'funcionarios': funcionarios})

# Adicionar Funcionário
def adicionar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Funcionário adicionado com sucesso!')
            return redirect('listar_funcionarios')
    else:
        form = FuncionarioForm()
    return render(request, 'adicionar_funcionario.html', {'form': form})

# Editar Funcionário

def editar_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)

    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados do funcionário atualizados com sucesso!')
            return redirect('listar_funcionarios')
    else:
        form = FuncionarioForm(instance=funcionario)

    return render(request, 'editar_funcionario.html', {'form': form})

# Deletar Funcionário
def deletar_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    funcionario.delete()
    messages.success(request, 'Funcionário removido com sucesso!')
    return redirect('listar_funcionarios')

@login_required
def listar_registros(request):
    registros = RegistroPonto.objects.select_related('funcionario').all()
    return render(request, 'listar_registros.html', {'registros': registros})


# Check-in/Check-out
def checkin_checkout(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        action = request.POST.get('action')  # Captura a ação (entrada ou saída)

        # Verifica se o CPF existe
        funcionario = Funcionario.objects.filter(cpf=cpf).first()
        if not funcionario:
            messages.error(request, 'Funcionário não encontrado!')
            return redirect('checkin_checkout')

        # Lógica para Registro de Ponto
        ultimo_registro = RegistroPonto.objects.filter(funcionario=funcionario).order_by('-id').first()

        if action == 'entrada':
            # Registra a entrada
            if not ultimo_registro or ultimo_registro.checkout:
                novo_registro = RegistroPonto(funcionario=funcionario, entrada=timezone.now())  # Usa timezone.now() para entrada
                novo_registro.save()
                messages.success(request, 'Entrada registrada com sucesso!')
            else:
                messages.error(request, 'Você já registrou a entrada. Faça o check-out primeiro.')

        elif action == 'saida':
            # Registra a saída
            if ultimo_registro and not ultimo_registro.checkout:
                ultimo_registro.checkout = timezone.now()  # Usa timezone.now() para saída
                ultimo_registro.save()
                messages.success(request, 'Saída registrada com sucesso!')
            else:
                messages.error(request, 'Não há entrada registrada para realizar a saída.')

        return redirect('checkin_checkout')  # Redireciona para a mesma página

    return render(request, 'checkin_checkout.html')