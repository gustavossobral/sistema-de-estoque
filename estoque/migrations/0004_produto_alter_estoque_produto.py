# Generated by Django 5.1.6 on 2025-03-06 13:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_remove_estoque_data_alter_estoque_descricao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='estoque',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.produto'),
        ),
    ]
