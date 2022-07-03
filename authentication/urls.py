from django.urls import path
from .views import CustomSignupView, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('cadastro/', CustomSignupView.as_view(), name='account_signup'),
    path('login/', CustomLoginView.as_view(), name='account_login'),
    path('logout/', CustomLogoutView.as_view(), name='account_logout'),
]
