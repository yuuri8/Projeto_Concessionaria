from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from dashboard.views import dashboard

urlpatterns = [
    path('login/', include('login.urls')),
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('funcionarios/', include('funcionarios.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('veiculos/', include('veiculos.urls')),
    path('clientes/', include('clientes.urls')),
    path('vendas/', include('vendas.urls')),
    path('test-drives/', include('testdrive.urls')),
    path('dashboard/', include('dashboard.urls')),
]
