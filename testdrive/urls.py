from django.urls import path
from . import views 

urlpatterns = [
    path('', views.listar_testdrives, name='listar_testdrives'),
    path('novo/', views.criar_testdrive, name='criar_testdrive'),
    path('editar/<int:testdrive_id>/', views.editar_testdrive, name='editar_testdrive'),
    path('deletar/<int:testdrive_id>/', views.deletar_testdrive, name='deletar_testdrive'),
    path('detalhes/<int:testdrive_id>/', views.detalhes_testdrive, name='detalhes_testdrive'),
    ]