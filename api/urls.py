from django.urls import path
from . import views

urlpatterns = [
    
    # API de Clientes
    path('clientes/', views.ClienteListCreateView.as_view(), name='cliente_list'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),
    
    # API de Productos
    path('productos/', views.ProductoListCreateView.as_view(), name='producto_list'),
    path('productos/<int:pk>/', views.ProductoDetailView.as_view(), name='producto_detail'),
    
    # API de Inventario
    path('inventario/', views.InventarioListCreateView.as_view(), name='inventario_list'),
    path('inventario/<int:pk>/', views.InventarioDetailView.as_view(), name='inventario_detail'),
]