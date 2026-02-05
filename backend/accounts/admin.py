from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'user_name', 'role', 'is_active']
    
    list_filter = ['role', 'is_active', 'is_staff']
    
    search_fields = ['email', 'user_name']
    
    readonly_fields = ['date_joined']
    
    ordering = ['-date_joined']
    
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('user_name', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Form layout for creating new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'password1', 'password2', 'role'),
        }),
    )

# Register with our custom admin class
admin.site.register(User, UserAdmin)