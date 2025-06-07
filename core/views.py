from django.shortcuts import render
from django.db.models import Sum, F
from users.decorators import jwt_login_required
from api.models import Cliente, Producto, Inventario  


def home(request):
    return render(request, 'home.html')

@jwt_login_required
def dashboard(request):
    clientes_count = Cliente.objects.count()
    productos_count = Producto.objects.count()
    
    # Calcular valor total del inventario
    valor_total = Inventario.objects.aggregate(
        total=Sum(F('cantidad') * F('producto__precio'))
    )['total'] or 0
    
    context = {
        'clientes_count': clientes_count,
        'productos_count': productos_count,
        'valor_total': valor_total
    }
    
    return render(request, 'dashboard.html', context)

@jwt_login_required
def clientes(request):
    return render(request, 'clients.html')  

@jwt_login_required
def productos(request):
    return render(request, 'products.html') 

@jwt_login_required
def inventario(request):
    return render(request, 'inventory.html')  