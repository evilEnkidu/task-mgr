from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm
)

class CustomUserAdmin(UserAdmin):
    list_display = [
        "username", "email", "role", "team", "is_staff"
    ]
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "role", "team", "password1", "password2"),
        }),
    )

    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": ("role", "team")
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
