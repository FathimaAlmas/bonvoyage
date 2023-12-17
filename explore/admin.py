from django.contrib import admin
from .models import Destinations,Packages,Booking,Dynamic,Package2,ViewHotels
admin.site.register(Destinations)
admin.site.register(Packages)

class BookingAdmin(admin.ModelAdmin):
    list_display=('id','firstname','lastname','phonenumber','email','checkin','checkout','guests','room_type')


admin.site.register(Booking,BookingAdmin)
admin.site.register(Dynamic)
admin.site.register(Package2)
admin.site.register(ViewHotels)

# Register your models here.
