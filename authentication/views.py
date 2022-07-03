from allauth.account.views import SignupView
from .forms import CustonSingupForm


class SignupView(SignupView):
    template_name = 'auth/signup.html'
    form_class = CustonSingupForm