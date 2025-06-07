# filepath: c:\Users\jose\Desktop\SistemaInventario\users\views.py
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from .models import User
from .serializers import UserRegisterSerializer, CustomTokenObtainPairSerializer
from .utils import set_token_cookies

class RegisterView(generics.CreateAPIView):
    """Vista de registro que usa cookies JWT seguras"""
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Generar token JWT
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        
        # Crear respuesta
        response = Response({
            'user': serializer.data,
            'message': 'Usuario registrado exitosamente'
        }, status=status.HTTP_201_CREATED)
        
        # Añadir cookies usando la función de utilidad
        return set_token_cookies(response, access_token, refresh_token)

class CookieTokenObtainPairView(TokenObtainPairView):
    """Vista para obtener JWT y establecerlos como cookies"""
    serializer_class = CustomTokenObtainPairSerializer
    
    def finalize_response(self, request, response, *args, **kwargs):
        if response.status_code == 200:
            access = response.data.get('access')
            refresh = response.data.get('refresh')
            
            # Establecer cookies usando la función de utilidad
            response = set_token_cookies(response, access, refresh)
        
        return super().finalize_response(request, response, *args, **kwargs)

class CookieTokenRefreshView(TokenRefreshView):
    """Vista para actualizar tokens utilizando la cookie de refresh"""
    
    def post(self, request, *args, **kwargs):
        # Extraer el token de refresh de las cookies
        refresh_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'])
        
        # Si hay token en las cookies, usarlo directamente
        if refresh_token:
            request.data['refresh'] = refresh_token
        
        # Continuar con el comportamiento normal
        return super().post(request, *args, **kwargs)
    
    def finalize_response(self, request, response, *args, **kwargs):
        if response.status_code == 200:
            access = response.data.get('access')
            refresh = response.data.get('refresh')
            
            # Establecer cookies usando la función de utilidad
            response = set_token_cookies(response, access, refresh)
        
        return super().finalize_response(request, response, *args, **kwargs)

class LogoutView(APIView):
    """Vista para eliminar las cookies JWT y cerrar sesión"""
    
    def post(self, request):
        response = Response({"detail": "Sesión cerrada exitosamente"})
        
        # Eliminar cookies
        response.delete_cookie(settings.SIMPLE_JWT['AUTH_COOKIE'])
        response.delete_cookie(settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'])
        
        return response

# Vistas web de usuarios
def register_page(request):
    """Página de registro"""
    return render(request, 'register.html')

def login_page(request):
    """Página de inicio de sesión"""
    return render(request, 'login.html')