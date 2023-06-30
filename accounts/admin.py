from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'id',
        'username',
        'nombre',
        'apellido',
        'bodega',
        'email',
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("nombre", "apellido", "bodega",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("nombre", "apellido", "bodega",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
