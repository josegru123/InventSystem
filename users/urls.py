from django.urls import path
from . import views

urlpatterns = [
    # API users
    path('api/register/', views.RegisterView.as_view(), name='api_register'),
    path('api/token/', views.CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', views.CookieTokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', views.LogoutView.as_view(), name='api_logout'),

    # Vistas web
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
]