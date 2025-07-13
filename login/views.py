from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy

class MeuLoginView(LoginView):
    template_name = 'login.html'  # Caminho para seu template
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True  # Se o usuário já estiver logado, redireciona

    def get_success_url(self):
        return reverse_lazy('dashboard')  # Substitua 'dashboard' pela sua URL pós-login
