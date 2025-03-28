from django.shortcuts import render, redirect, get_object_or_404
from .models import Estoque, Produto
from .forms import EstoqueForm, ProdutoForms, EditarEstoqueForm, QuantidadeForm
from django.contrib import messages

def mostrar_estoque(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    estoque = Estoque.objects.all()
    return render(request, 'estoque/index.html', {'estoque': estoque})

def adicionar_ao_estoque(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        form = EstoqueForm(request.POST)
        if form.is_valid():
            fornecedor = form.cleaned_data.get('fornecedor', '')
            descricao = form.cleaned_data.get('descricao', '')
            preco = form.cleaned_data.get('preco', 0)

            if fornecedor is None or fornecedor == '':
                fornecedor = ''
            if descricao is None or descricao == '':
                descricao = ''
            if preco is None or preco < 0:
                preco = 0
            
            produto_existente = Estoque.objects.filter(produto=form.cleaned_data['produto']).first()
            if produto_existente:
                messages.error(request, f'Produto "{form.cleaned_data['produto']}" já existe no estoque!')
                return redirect('estoque/mostrar_estoque')
            else:
                novo_produto = form.save(commit=False)
                novo_produto.fornecedor = fornecedor
                novo_produto.descricao = descricao
                novo_produto.preco = preco
                novo_produto.save()
                messages.success(request, f'Produto "{form.cleaned_data['produto']}" adicionado ao estoque com sucesso!')
            return redirect('estoque/mostrar_estoque')
        else:
            messages.error(request, 'Erro ao adicionar produto!')
            return redirect('estoque/mostrar_estoque')
        
    else:
        form = EstoqueForm()
    produtos = Produto.objects.all()
    return render(request, 'estoque/adicionar_ao_estoque.html', {'form': form, 'produtos': produtos})

def editar_produto(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    produto = get_object_or_404(Estoque, id=id)
    if request.method == 'POST':
        form = EditarEstoqueForm(request.POST, instance=produto)
        if form.is_valid():
            fornecedor = form.cleaned_data['fornecedor']
            descricao = form.cleaned_data['descricao']
            preco = form.cleaned_data['preco']

            if fornecedor is None or fornecedor == '':
                fornecedor = ''
            if descricao is None or descricao == '':
                descricao = ''
            if preco is None or preco < 0:
                preco = 0

            produto.fornecedor = fornecedor
            produto.descricao = descricao
            produto.preco = preco
            produto.save()
            messages.success(request, f'Produto "{produto.produto}" editado com sucesso!')
            return redirect('estoque/mostrar_estoque')
        else:
            messages.error(request, 'Erro ao editar produto!')
    else:
        form = EditarEstoqueForm(instance=produto)
    return render(request, 'estoque/editar_produto.html', {'form': form, 'produto': produto})

def excluir_produto(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    produto = get_object_or_404(Estoque, id=id)
    produto.delete()
    messages.success(request, f'Produto "{produto.produto}" excluído com sucesso!')
    return redirect('estoque/mostrar_estoque')

def adicionar_novo_produto(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        form = ProdutoForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Produto "{form.cleaned_data['nome']}" adicionado com sucesso!')
            return redirect('estoque/mostrar_estoque')
        else:
            messages.error(request, 'Erro ao adicionar produto!')
    else:
        form = ProdutoForms()
    return render(request, 'estoque/adicionar_novo_produto.html', {'form':form})

def aumentar_quantidade(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    produto = get_object_or_404(Estoque, id=id)
    if request.method == 'POST':
        form = QuantidadeForm(request.POST)
        if form.is_valid():
            produto.quantidade += form.cleaned_data['quantidade']
            produto.save()
            messages.success(request, f'Quantidade de "{produto.produto}" aumentada com sucesso!')
            return redirect('estoque/mostrar_estoque')
        else:
            messages.error(request, 'Erro ao aumentar quantidade!')
            return redirect('estoque/mostrar_estoque')
    else:
        form = QuantidadeForm(initial={'quantidade': produto.quantidade})
    return render(request, 'estoque/aumentar_quantidade.html', {'form': form, 'produto': produto})

def diminuir_quantidade(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    produto = get_object_or_404(Estoque, id=id)
    if request.method == 'POST':
        form = QuantidadeForm(request.POST)
        if form.is_valid():
            produto.quantidade -= form.cleaned_data['quantidade']
            produto.save()
            messages.success(request, f'Quantidade de "{produto.produto}" diminuida com sucesso!')
            return redirect('estoque/mostrar_estoque')
        else:
            messages.error(request, 'Erro ao diminuir quantidade!')
            return redirect('estoque/mostrar_estoque')
    else:
        form = QuantidadeForm(initial={'quantidade': produto.quantidade})
    return render(request, 'estoque/diminuir_quantidade.html', {'form': form, 'produto': produto})

def buscar_produto(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    query = request.GET.get('buscar', '')
    if query:
        produtos = Estoque.objects.filter(produto__nome__icontains=query)
    else:
        produtos = Estoque.objects.all()
    return render(request, 'estoque/buscar_produto.html', {'estoque': produtos})