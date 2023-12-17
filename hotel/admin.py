from django.contrib import admin
from explore.models import Hotel

def approve_hotels(modeladmin, request, queryset):
    queryset.update(license_verified=True)

approve_hotels.short_description = 'Approve selected hotels'

class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'license_verified']
    actions = [approve_hotels]

admin.site.register(Hotel, HotelAdmin)

