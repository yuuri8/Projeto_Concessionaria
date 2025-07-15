from django.urls import path
from . import views 
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.listar_funcionarios, name='listar_funcionarios'),
    path('novo/', views.criar_funcionario, name='criar_funcionario'),
    path('editar/<int:funcionario_id>/', views.editar_funcionario, name='editar_funcionario'),
    path('deletar/<int:funcionario_id>/', views.deletar_funcionario, name='deletar_funcionario'),
    path('detalhes/<int:funcionario_id>/', views.detalhes_funcionarios, name='detalhes_funcionarios'),
    path('sem-permissao/', TemplateView.as_view(template_name='sem_permissao.html'), name='sem_permissao'),
    ]