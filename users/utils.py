from django.conf import settings

def set_token_cookies(response, access_token, refresh_token=None):
    """
    Establece las cookies JWT en una respuesta HTTP
    
    Args:
        response: Objeto Response de Django REST Framework
        access_token: Token de acceso JWT
        refresh_token: Token de actualización JWT (opcional)
    
    Returns:
        La misma respuesta con las cookies establecidas
    """
    # Establecer cookie de acceso
    response.set_cookie(
        key=settings.SIMPLE_JWT['AUTH_COOKIE'],
        value=access_token,
        expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
        secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
        httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
        samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
    )
    
    # Establecer cookie de refresh si se proporciona
    if refresh_token:
        response.set_cookie(
            key=settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'],
            value=refresh_token,
            expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
            secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )
    
    return response