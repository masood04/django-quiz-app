from django.contrib import admin
from .models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'is_active', 'is_staff', 'first_name', 'last_name')

    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2',
                       'is_staff', 'is_active', 'first_name', 'last_name')}
         ),
    )

    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Token)
