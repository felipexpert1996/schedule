from django.urls import path
from .views import SignupView

urlpatterns = [
    path('cadastro/', SignupView.as_view(), name='signup'),
]
