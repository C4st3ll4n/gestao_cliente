from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pessoa
from .forms import PessoaForm


@login_required
def listagem(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'person.html', {'pessoas': pessoas})


@login_required
def create(request):
    form = PessoaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lista_pessoa')
    return render(request, 'formulario_nova_pessoa.html', {'form': form})


@login_required
def update(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    form = PessoaForm(request.POST or None, request.FILES or None, instance=pessoa)
    if form.is_valid():
        form.save()
        return redirect('lista_pessoa')
    return render(request, 'formulario_nova_pessoa.html', {'form': form})

@login_required
def delete(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    form = PessoaForm(request.POST or None, request.FILES or None, instance=pessoa)

    if request.method == "POST":
        pessoa.delete()
        return redirect('lista_pessoa')

    return render(request, 'confirmar_delecao.html', {'pessoa': pessoa})
