# Generated by Django 5.1.6 on 2025-03-02 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_rename_material_estoque_produto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estoque',
            name='data',
        ),
        migrations.AlterField(
            model_name='estoque',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='estoque',
            name='fornecedor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='estoque',
            name='produto',
            field=models.CharField(choices=[('tecido', 'Tecido'), ('couro', 'Couro'), ('espuma', 'Espuma'), ('madeira', 'Madeira'), ('mola', 'Mola'), ('algodao', 'Algodão'), ('poliester', 'Poliéster'), ('veludo', 'Veludo'), ('linho', 'Linho'), ('seda', 'Seda')], max_length=255),
        ),
    ]
