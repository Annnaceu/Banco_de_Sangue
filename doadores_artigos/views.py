from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone 
from .forms import DoadorForm
from .models import Doador

def incentivo(request):
    return render(request, 'doadores_artigos/incentivo.html')

def cadastrar_doador(request):
    if request.method == 'POST':
        form = DoadorForm(request.POST)
        if form.is_valid():
            doador = form.save(commit=False) 
            doador.data_ultima_doacao = timezone.now() 
            doador.save() 
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('lista_doadores')
    else:
        form = DoadorForm()

    return render(request, 'doadores_artigos/cadastrar_doador.html', {'form': form})

def lista_doadores(request):
    doadores = Doador.objects.all()
    return render(request, 'doadores_artigos/lista_doadores.html', {'doadores': doadores})
