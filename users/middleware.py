from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.authentication import JWTAuthentication

class JWTCookieMiddleware(MiddlewareMixin):
    """
    Middleware que convierte las cookies JWT en encabezados de autorización
    y establece el usuario autenticado en request.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.jwt_auth = JWTAuthentication()

    def __call__(self, request):
        # Obtener token de la cookie
        auth_cookie = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE'])
        
        # Si existe, añadirlo al encabezado de autorización
        if auth_cookie:
            request.META['HTTP_AUTHORIZATION'] = f"Bearer {auth_cookie}"
            
            # Autenticar al usuario usando el token
            try:
                validated_token = self.jwt_auth.get_validated_token(auth_cookie)
                user = self.jwt_auth.get_user(validated_token)
                request.user = user  
            except Exception:
                # Si hay un error con el token, dejamos que continúe sin autenticación
                pass
        
        response = self.get_response(request)
        return response