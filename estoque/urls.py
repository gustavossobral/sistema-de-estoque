from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_estoque, name='mostrar_estoque'),
    path('adicionar_ao_estoque/', views.adicionar_ao_estoque, name='adicionar_ao_estoque'),
    path('editar_produto/<int:id>/', views.editar_produto, name='editar_produto'),
    path('adicionar_novo_produto/', views.adicionar_novo_produto, name='adicionar_novo_produto'),
    path('excluir_produto/<int:id>/', views.excluir_produto, name='excluir_produto'),
    path('aumentar_quantidade/<int:id>/', views.aumentar_quantidade, name='aumentar_quantidade'),
    path('diminuir_quantidade/<int:id>/', views.diminuir_quantidade, name='diminuir_quantidade'),
    path('buscar_produto/', views.buscar_produto, name='buscar_produto'),
]