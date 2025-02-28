from django.shortcuts import render, redirect
from .models import Estoque, produto_choices
from .forms import EstoqueForm

def mostrar_estoque(request):
    estoque = Estoque.objects.all()
    return render(request, 'estoque.html', {'estoque': estoque})

def adicionar_produto(request):
    if request.method == 'POST':
        form = EstoqueForm(request.POST)
        if form.is_valid():
            produto_form = form.cleaned_data['produto']
            quantidade_form = form.cleaned_data['quantidade']
            preco_form = form.cleaned_data['preco']
            fornecedor_form = form.cleaned_data['fornecedor']
            descricao_form = form.cleaned_data['descricao']

            try:
                # Se o produto já existir no estoque, adicionar a quantidade informada
                estoque_produto = Estoque.objects.get(produto=produto_form)
                if estoque_produto.quantidade is not None:
                    estoque_produto.quantidade += quantidade_form

                # Validar se o preço é diferente do preço atual, caso seja, atualizar no banco
                if preco_form is not None and preco_form != estoque_produto.preco:
                    estoque_produto.preco = preco_form

                estoque_produto.fornecedor = fornecedor_form
                estoque_produto.descricao = descricao_form
                estoque_produto.save()
                
            except Estoque.DoesNotExist:
                form.save()
            return redirect('mostrar_estoque')
    else:
        form = EstoqueForm()
    return render(request, 'adicionar_produto.html', {'form': form, 'produto_choices': produto_choices})