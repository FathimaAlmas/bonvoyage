from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BookingForm, CancelBookingForm
from django.contrib import messages


from .models import Hotel
from .models import ViewHotels
from .models import Destinations
from .models import Dynamic
from .models import Packages,Package2
from .forms import BookingForm
from .models import Booking

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from xhtml2pdf import pisa
from decimal import Decimal  

from django.conf import settings
from django.views.generic import TemplateView
import stripe


#destinations
def destinations(request):
    destinations=Destinations.objects.all()
    return render(request,'base/destinations.html',{'destinations':destinations})

def dynamic(request,destinations_id):
    dynamics=get_object_or_404(Dynamic,pk=destinations_id)
    return render(request,'base/dynamic.html',{'dynamics':dynamics})


def searchDestinations(request):
    if request.method=='GET':
            query=request.GET.get('query')
            if query:
                destinations=Destinations.objects.filter(name__icontains=query)
                return render(request,'base/search.html',{'destinations':destinations})
            else:
                print("No Destinations")
                return render(request,'base/search.html',{})


#packages
def packages(request):
    packages=Packages.objects.all()
    return render(request,'base/packages.html',{'packages':packages})

def package2(request,package2_id):
    package2=get_object_or_404(Package2,pk=package2_id)
    return render(request,'base/pack2.html',{'package2':package2})


#hotels
def hotel(request):
    hotel = Hotel.objects.filter(license_verified = True)
    return render(request,'base/hotel.html',{'hotel':hotel})

def view_hotels(request,hotels_id):
    hotels=get_object_or_404(ViewHotels,pk=hotels_id)
    return render(request,'base/viewhotels.html',{'hotels':hotels})


#booking
def booking(request):
    hotels = Hotel.objects.all()
    packages = Packages.objects.all()
   

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)  
            selected_hotel = form.cleaned_data['hotel']
            selected_package = form.cleaned_data['package']
            total_cost = selected_hotel.price + selected_package.price
            booking.total_cost = total_cost
            booking.save()      
            return redirect('payment')
    else:
        form = BookingForm()

    context = {
        'form': form,
        'hotels': hotels,
        'packages': packages,
       
    }

    return render(request, 'base/booking.html', context)         

class payment(TemplateView):
    template_name='base/payment.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY 
        return context

stripe.api_key = settings.STRIPE_SECRET_KEY     
def charge(request):
    publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    return render(request, 'base/charge.html', {'key': publishable_key})

    if request.method == 'POST':
        try:
            token = request.POST['stripeToken']
            charge = stripe.Charge.create(
                amount=500,  # Make sure to replace this with the actual amount
                currency='inr',
                description='Payment Gateway',
                source=token,
            )
            return render(request, 'base/charge.html')
        except stripe.error.CardError as e:
            return render(request, 'base/error.html', {'error': e})
        except Exception as e:
            return render(request, 'base/error.html', {'error': e})
    return redirect('payment')
    

def error(request):
    return render(request,'base/error.html')


#payment receipt
def receipt(request):
    receipt = Booking.objects.last()

    # Calculate package and hotel prices
    package_price = receipt.package.price if receipt.package else Decimal('0.00')
    hotel_price = receipt.hotel.price if receipt.hotel else Decimal('0.00')
    tax = (package_price + hotel_price) * Decimal('0.07')  # Assuming tax is 7% of the total

    template_path = 'base/receipt.html'
    context = {
        'firstname': receipt.firstname,
        'lastname': receipt.lastname,
        'phonenumber': receipt.phonenumber,
        'email': receipt.email,
        'id': receipt.id,
        'checkin': receipt.checkin,
        'checkout': receipt.checkout,
        'guests': receipt.guests,
        'package': receipt.package,
        'hotel': receipt.hotel,
        'room_type': receipt.room_type,
        'package_price': package_price,
        'hotel_price': hotel_price,
        'tax': tax,
        'total_with_tax': package_price + hotel_price + tax,
    }
    

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="{receipt.package}_trip_bill.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)
    return response


#cancellation
def cancel_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)    
    if request.method == 'POST':
        form = CancelBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = CancelBookingForm(instance=booking)
    return render(request, 'base/cancel_book.html', {'form': form, 'booking': booking})


def booking_list(request):
    # if not request.user.is_authenticated:
    #     messages.warning(request, 'Please log in to view your bookings.')
    #     return redirect('user_login')
    bookings = Booking.objects.filter(canceled=False)
    return render(request, 'base/booking_list.html', {'bookings': bookings})
