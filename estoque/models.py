from django.db import models

produto_choices = [
    ('tecido', 'Tecido'),
    ('couro', 'Couro'),
    ('espuma', 'Espuma'),
    ('madeira', 'Madeira'),
    ('mola', 'Mola'),
    ('algodao', 'Algodão'),
    ('poliester', 'Poliéster'),
    ('veludo', 'Veludo'),
    ('linho', 'Linho'),
    ('seda', 'Seda'),
]

class Estoque(models.Model):
    produto = models.CharField(max_length=255, default='', editable=True, choices=produto_choices)
    data = models.DateField(auto_now_add=True, editable=True)
    quantidade = models.IntegerField(default=0, editable=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=True)
    fornecedor = models.CharField(max_length=255, default='', editable=True, blank=True, null=True)
    descricao = models.TextField(default='', editable=True, blank=True, null=True)

    def __str__(self):
        return self.produto
