from django.urls import path
from .views import MeuLoginView

urlpatterns = [
    path('login/', MeuLoginView.as_view(), name='login'),
]
