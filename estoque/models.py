from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nome

class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fornecedor = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade}"