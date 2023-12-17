from django.shortcuts import get_object_or_404, render, redirect
from .forms import HotelSubmissionForm
from django.contrib import messages
from explore.models import Hotel
from django.contrib.auth.decorators import login_required

def submit_hotel(request):
    if request.method == 'POST':
        form = HotelSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            # Set the owner before saving the form
            form.instance.owner = request.user
            # Mark the hotel as submitted for approval
            # form.instance.submitted = True
            form.save()
            messages.success(request, 'Hotel submitted successfully. Waiting for approval.')
            return redirect('index') # Redirect to the home page or a thank-you page
    else:
        form = HotelSubmissionForm()
    return render(request, 'base/submit_hotel.html', {'form': form})

def view_submitted_hotels(request):
    if request.user.is_superuser:
        hotels = Hotel.objects.filter(license_verified = False)
        return render(request, 'base/view_submitted_hotels.html', {'hotels': hotels})
    else:
        return redirect('hotelhome') # Redirect to the home page

def approve_hotel(request, pk):
    if request.user.is_superuser:
        hotel = Hotel.objects.get(id=pk)
        hotel.license_verified = True
        hotel.save()
        # messages.success(request, 'Hotel approved successfully.')
        return redirect('view_submitted_hotels')
    else:
        return redirect('index') # Redirect to the home page

def reject_hotel(request, pk):
    if request.user.is_superuser:
        hotel = Hotel.objects.get(id=pk)
        hotel.delete()
        messages.success(request, 'Hotel rejected successfully.')
        return redirect('view_submitted_hotels')
    else:
        return redirect('index') # Redirect to the home page
    

def hotel_home(request):
    return render(request,'base/hotel_home.html')


#HOTELS
def hotel_admin(request):
    hotel=Hotel.objects.all()
    return render(request,'base/hotel_admin.html',{'hotel':hotel})

def add_hotel(request):
    if request.method == 'POST':
        name = request.POST.get('hotel_name')
        img = request.FILES.get('hotel_img')
        desc = request.POST.get('hotel_desc')
        price = request.POST.get('hotel_price')
        rating = request.POST.get('hotel_rating')
        license_number=request.POST.get('hotel_license')
        Hotel.objects.create(name=name,img=img, desc=desc,price=price,rating=rating,license_number=license_number)
        if 'add_another' in request.POST:
            
            return redirect('admin_hotel') 
        else:
            
            return redirect('hotel_admin') 

    return render(request, 'base/admin_hotel.html')
    
@login_required
def update_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    if request.method == 'POST':
        hotel.name = request.POST.get('hotel_name')
        hotel.img=request.FILES.get('hotel_img')
        hotel.desc=request.POST.get('hotel_desc')
        hotel.price = request.POST.get('hotel_price')
        hotel.rating = request.POST.get('hotel_rating')
        hotel.license = request.POST.get('hotel_license')
        hotel.save()
        return redirect('hotel_admin')
    return render(request, 'base/update_hotel.html', {'hotel': hotel})

@login_required
def delete_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    if request.method == 'POST':

        hotel.delete()
        return redirect('hotel_admin')
    return render(request, 'base/hotel_admin.html', {'hotel': hotel})
