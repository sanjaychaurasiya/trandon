from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import Group
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('first_name', 'middle_name', 'last_name', 'email', 'is_staff', 'is_active')
    list_filter = ('first_name', 'middle_name', 'last_name', 'email', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('first_name', 'middle_name', 'last_name', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'middle_name', 'last_name', 'email', 'password1', 'password2',
                       'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
# """admin.site.unregister() is used to unregister any model from the admin panel."""
# admin.site.unregister(Group)
