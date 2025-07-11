from django.urls import path
from . import views 

urlpatterns = [
    path('', views.lista_clientes, name='listar_clientes'),
    path('novo/', views.criar_cliente, name='criar_cliente'),
    path('editar/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('deletar/<int:cliente_id>/', views.deletar_cliente, name='deletar_cliente'),
    path('detalhe/<int:cliente_id>/', views.detalhes_cliente, name='detalhar_cliente'),
    ]