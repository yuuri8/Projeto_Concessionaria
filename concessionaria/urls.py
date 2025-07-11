from django.contrib import admin
from django.urls import path, include
from funcionarios.views import home
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('funcionarios/', include('funcionarios.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('veiculos/', include('veiculos.urls')),
    path('clientes/', include('clientes.urls')),
]
