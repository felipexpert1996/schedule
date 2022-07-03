from allauth.account.views import SignupView, LoginView, LogoutView
from .forms import CustomSingupForm, CustomLoginForm


class CustomSignupView(SignupView):
    template_name = 'auth/signup.html'
    form_class = CustomSingupForm


class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    form_class = CustomLoginForm


class CustomLogoutView(LogoutView):
    pass
