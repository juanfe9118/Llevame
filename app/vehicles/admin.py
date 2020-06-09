from django.contrib import admin
from .models import Vehicle


class VehicleAdmin(admin.ModelAdmin):
    """ Define Vehicle admin panel """
    list_display = ('plate', 'model', 'color', 'brand', 'user')
    ordering = ('user',)
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Vehicle, VehicleAdmin)
