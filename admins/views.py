from django.shortcuts import render, redirect, get_object_or_404
from explore.models import Destinations
from django.contrib.auth.decorators import login_required
from explore.models import Packages


def admin_home(request):
    return render(request,'base/adminhome.html')


#DESTINATIONS
def add_destinations(request):
    if request.method == 'POST':
        name=request.POST.get('dest_name')
        img=request.FILES.get('dest_img')
        desc=request.POST.get('dest_desc')
        Destinations.objects.create(name=name,img=img,desc=desc)
        if 'add_another' in request.POST:
            return redirect('admin_destination')
        else:
            return redirect('dest_admin')
    return render(request,'base/admin_destination.html')
    
def dest_admin(request):
    destinations=Destinations.objects.all()
    return render(request,'base/dest_admin.html',{'destinations':destinations})


@login_required
def update_dest(request,dest_id):
    destinations=get_object_or_404(Destinations,id=dest_id)
    if request.method == 'POST':
        destinations.name=request.POST.get('dest_name')
        destinations.img=request.FILES.get('dest_img')
        destinations.desc=request.POST.get('dest_desc')
        destinations.save()
        return redirect('dest_admin')
    
    return render(request,'base/update_dest.html',{'destinations':destinations})


@login_required
def delete_dest(request, dest_id):
    destinations= get_object_or_404(Destinations, id=dest_id)
    if request.method == 'POST':

        destinations.delete()
        return redirect('dest_admin')
    return render(request, 'base/dest_admin.html', {'destinations': destinations})


#PACKAGES
def add_packages(request):
    if request.method == 'POST':
        name=request.POST.get('pack_name')
        img=request.FILES.get('pack_img')
        img1=request.FILES.get('pack_img1')
        desc=request.POST.get('pack_desc')
        desc1=request.POST.get('pack_desc1')
        price=request.POST.get('pack_price')
        price1=request.POST.get('pack_price1')
        Packages.objects.create(name=name,img=img,img1=img1,desc=desc,desc1=desc1,price=price,price1=price1)
        if 'add_another' in request.POST:
            return redirect('admin_package')
        else:
            return redirect('pack_admin')
    
    return render(request,'base/admin_package.html')
   
def pack_admin(request):
    packages=Packages.objects.all()
    return render(request,'base/pack_admin.html',{'packages':packages})
    

@login_required
def update_pack(request,pack_id):
    packages=get_object_or_404(Packages,id=pack_id)
    if request.method == 'POST':
        packages.name=request.POST.get('pack_name')
        packages.img=request.FILES.get('pack_img')
        packages.img1=request.FILES.get('pack_img1')
        packages.desc=request.POST.get('pack_desc')
        packages.desc1=request.POST.get('pack_desc1')
        packages.price=request.POST.get('pack_price')
        packages.price1=request.POST.get('pack_price1')
        packages.save()
        return redirect('pack_admin')
    
    return render(request,'base/update_pack.html',{'packages':packages})


@login_required
def delete_pack(request, pack_id):
    packages= get_object_or_404(Packages, id=pack_id)
    if request.method == 'POST':

        packages.delete()
        return redirect('pack_admin')
    return render(request, 'base/pack_admin.html', {'packages': packages})

    

