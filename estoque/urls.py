from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.mostrar_estoque, name='mostrar_estoque'),
    path('adicionar_produto/', views.adicionar_produto, name='adicionar_produto'),
]