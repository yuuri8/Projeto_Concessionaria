from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.lista_veiculos, name='lista_veiculos'),
    path('novo/', views.novo_veiculo, name='novo_veiculo'),
    path('editar/<int:id>/', views.editar_veiculo, name='editar_veiculo'),
    path('deletar/<int:id>/', views.deletar_veiculo, name='deletar_veiculo'),
    path('detalhes/<int:id>/', views.detalhes_veiculo, name='detalhes_veiculo'),
    path('sem-permissao/', TemplateView.as_view(template_name='sem_permissao.html'), name='sem_permissao'),
]
