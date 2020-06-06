from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Department, City


class UserAdmin(BaseUserAdmin):
    """ Define User admin panel """
    list_display = ('first_name', 'last_name', 'type_id', 'n_document', 'email', 'date_joined', 'last_login', 'is_active')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('email',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, UserAdmin)
