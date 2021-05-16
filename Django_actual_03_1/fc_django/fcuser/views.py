from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm

# Create your views here.
# root 경로 설정
def index(request):
    return render(request, 'index.html', { 'email': request.session['user'] })

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    # form 유효성 검사가 끝났을 때, 다음 실행되는 부분.
    def form_valid(self, form):
        self.request.session['user'] = form.email
        return super().form_valid(form)
