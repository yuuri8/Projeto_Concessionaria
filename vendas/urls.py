from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_vendas, name='lista_vendas'),
    path('nova/', views.nova_venda, name='nova_venda'),

]


