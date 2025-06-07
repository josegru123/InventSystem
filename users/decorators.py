from django.shortcuts import redirect
from functools import wraps
from django.conf import settings
from rest_framework_simplejwt.authentication import JWTAuthentication

def jwt_login_required(view_func):
    """
    Decorador que verifica si el usuario está autenticado mediante JWT cookies.
    Si no lo está, redirige a la página de login configurada en settings.LOGIN_URL.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Verificar si el usuario ya está autenticado
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        
        # Intentar autenticar usando la cookie JWT
        auth_cookie = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE'])
        if auth_cookie:
            try:
                jwt_auth = JWTAuthentication()
                validated_token = jwt_auth.get_validated_token(auth_cookie)
                user = jwt_auth.get_user(validated_token)
                if user:
                    request.user = user
                    return view_func(request, *args, **kwargs)
            except Exception:
                pass  # Si hay error en el token, continuamos a la redirección
        
        # Si no está autenticado, redirigir a login
        next_url = request.path
        return redirect(f"{settings.LOGIN_URL}?next={next_url}")
    
    return wrapper