from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, AuthenticationDropdown
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect

# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"

def home(request):
    if request.method == 'GET':
        return render(request, 'home.html', {'form': AuthenticationDropdown})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'home.html', {'form': AuthenticationDropdown, 'error': 'Error en nombre de usuario y contraseña, intente nuevamente'})
        else:
            login(request, user)
            return redirect('home')