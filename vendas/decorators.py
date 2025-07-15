from django.shortcuts import redirect

def permissao_requerida(permissao):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)  # permite superusuário

            funcionario = getattr(request.user, 'funcionario', None)
            if funcionario and funcionario.permissao == permissao:
                return view_func(request, *args, **kwargs)
            return redirect('sem_permissao')
        return _wrapped_view
    return decorator
