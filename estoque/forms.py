from django import forms
from .models import Estoque, Produto

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['produto', 'quantidade', 'preco', 'fornecedor', 'descricao']

class ProdutoForms(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome']

    # Deixar a primeira letra sempre maiúscula
    def save(self, commit=True):
        produto = super().save(commit=False)
        produto.nome = produto.nome.capitalize()
        if commit:
            produto.save()
        return produto
    
class EditarEstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['preco', 'fornecedor', 'descricao']

class QuantidadeForm(forms.Form):
    quantidade = forms.IntegerField(min_value=0, label='Quantidade')