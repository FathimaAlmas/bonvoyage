from django.contrib import admin
from .models import UserProfile,AdminProfile,HotelProfile

admin.site.register(UserProfile)
admin.site.register(AdminProfile)
admin.site.register(HotelProfile)

# Register your models here.
