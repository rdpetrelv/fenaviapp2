from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("nombre", "apellido", "bodega")

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class AuthenticationDropdown(AuthenticationForm):
    CHOISES = []
    for us in CustomUser.objects.all():
        if us.is_staff == False:
            a =(us.username, f"{us.nombre} {us.apellido}")
            CHOISES.append(a)
    
    username = forms.ChoiceField(label='Nombre de usuario', choices = CHOISES)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)