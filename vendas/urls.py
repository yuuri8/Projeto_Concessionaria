from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_vendas, name='lista_vendas'),
    path('nova/', views.nova_venda, name='nova_venda'),
    path('editar/<int:id>/', views.editar_venda, name='editar_venda'),
    path('deletar/<int:id>/', views.deletar_venda, name='deletar_venda'),
    path('detalhes/<int:id>/', views.detalhes_venda, name='detalhes_venda'),
]


