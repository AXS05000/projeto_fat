from django.contrib import messages
from django.http import Http404, HttpResponse
from django.shortcuts import render

from .forms import BaseCNPJModelForm, NotasModelForm
from .models import Notas

# from core.main import make_recipe - Importação para testar as coisas.

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def search(request):

    search_term = request.GET.get('q', '')

    if not search_term:
        raise Http404
        
    return render(request, 'search.html')

def gestao(request):
    notas = Notas.objects.all().order_by('-id')
    return render(request, 'gestao.html', context={
        'nota_gestao': notas,
    })

def notafiscalindividual(request, id):
    notas = Notas.objects.filter(id=id).order_by('-id')
    return render(request, 'pages/recipe-view.html', context={
        'nota_gestao': notas,
        'pag_de_detalhe': True,
    })

def cliente(request, cliente_id):
    notas = Notas.objects.filter(cnpj_da_nota__id=cliente_id).order_by('-id')

    if not notas:
        return HttpResponse(content='Not found', status=404)
    return render(request, 'cliente.html', context={
        'nota_gestao': notas,
        'title_cliente': f'{notas.first().cnpj_da_nota.nome_cliente} | Ametista'
    })
































def qtddecargos(request):
    return render(request, 'qtddecargos.html')

def notafiscal(request):
    if str(request.method) == 'POST':
        form = NotasModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Formulario salvo com sucesso')
            form = NotasModelForm()
        else:
            messages.error(request, 'Erro ao salvar o formulario')
            
    else:
        form = NotasModelForm()
    context = {
        'form': form
    }
    return render(request, 'notafiscal.html', context)

# Inicio aqui das quantidades de cargos a mais.



# 2 Cargos

def notafiscal2(request):
    if str(request.method) == 'POST':
        form = NotasModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Formulario salvo com sucesso')
            form = NotasModelForm()
        else:
            messages.error(request, 'Erro ao salvar o formulario')
            
    else:
        form = NotasModelForm()
    context = {
        'form': form
    }
    return render(request, 'notafiscal2.html', context)

# 3 Cargos

def notafiscal3(request):
    if str(request.method) == 'POST':
        form = NotasModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Formulario salvo com sucesso')
            form = NotasModelForm()
        else:
            messages.error(request, 'Erro ao salvar o formulario')
            
    else:
        form = NotasModelForm()
    context = {
        'form': form
    }
    return render(request, 'notafiscal3.html', context)


# 4 Cargos

def notafiscal4(request):
    if str(request.method) == 'POST':
        form = NotasModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Formulario salvo com sucesso')
            form = NotasModelForm()
        else:
            messages.error(request, 'Erro ao salvar o formulario')
            
    else:
        form = NotasModelForm()
    context = {
        'form': form
    }
    return render(request, 'notafiscal4.html', context)

# 5 Cargos

def notafiscal5(request):
    if str(request.method) == 'POST':
        form = NotasModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Formulario salvo com sucesso')
            form = NotasModelForm()
        else:
            messages.error(request, 'Erro ao salvar o formulario')
            
    else:
        form = NotasModelForm()
    context = {
        'form': form
    }
    return render(request, 'notafiscal5.html', context)

# 6 Cargos

def notafiscal6(request):
    if str(request.method) == 'POST':
        form = NotasModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Formulario salvo com sucesso')
            form = NotasModelForm()
        else:
            messages.error(request, 'Erro ao salvar o formulario')
            
    else:
        form = NotasModelForm()
    context = {
        'form': form
    }
    return render(request, 'notafiscal6.html', context)


# 7 Cargos

def notafiscal7(request):
    if str(request.method) == 'POST':
        form = NotasModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Formulario salvo com sucesso')
            form = NotasModelForm()
        else:
            messages.error(request, 'Erro ao salvar o formulario')
            
    else:
        form = NotasModelForm()
    context = {
        'form': form
    }
    return render(request, 'notafiscal7.html', context)

# 8 Cargos

def notafiscal8(request):
    if str(request.method) == 'POST':
        form = NotasModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Formulario salvo com sucesso')
            form = NotasModelForm()
        else:
            messages.error(request, 'Erro ao salvar o formulario')
            
    else:
        form = NotasModelForm()
    context = {
        'form': form
    }
    return render(request, 'notafiscal8.html', context)


def cnpj(request):
    if str(request.method) == 'POST':
        form = BaseCNPJModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Formulario salvo com sucesso')
            form = BaseCNPJModelForm()
        else:
            messages.error(request, 'Erro ao salvar o formulario')
            
    else:
        form = BaseCNPJModelForm()
    context = {
        'form': form
    }
    return render(request, 'cnpj.html', context)
