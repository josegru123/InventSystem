from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views


# Agrega estas importaciones:
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Inventario",
      default_version='v1',
      description="Documentación de la API del sistema de inventario",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), 
    path('', include('users.urls')),  


   # URLs para las templates
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('clientes/', views.clientes, name='clientes'),
    path('productos/', views.productos, name='productos'),
    path('inventario/', views.inventario, name='inventario'),

   # URLs para la documentación de las API
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]