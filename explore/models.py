from django.db import models
from django.contrib.auth.models import User

class Destinations(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='destinations')
    desc=models.TextField()
    
class Hotel(models.Model):
    owner = models.TextField(default='Unknown')
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='hotel')
    desc=models.TextField()
    price=models.IntegerField()
    rating=models.PositiveIntegerField()
    license_verified = models.BooleanField(default=False)
    license_number=models.PositiveIntegerField()
    submitted = models.BooleanField(default=False)
   
    def __str__(self):
        return self.name

class Packages(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='packages')
    img1=models.ImageField(upload_to='packages')
    desc=models.TextField()
    desc1=models.TextField()
    price=models.IntegerField()
    price1=models.IntegerField()
   
class Booking(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=10)
    email=models.CharField(max_length=200)
    checkin=models.DateField()
    checkout=models.DateField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    package = models.ForeignKey(Packages, on_delete=models.CASCADE)

    GUESTS_CHOICES = (
        (1, '1 guest'),
        (2, '2 guests'),
        (3, '3 guests'),
        (4, '4 guests'),
        (5, '5 guests'),
    )

    guests = models.PositiveIntegerField(choices=GUESTS_CHOICES)
    
    AC = 'AC'
    NON_AC = 'Non-AC'
    SINGLE_BED = 'Single Bed'
    DOUBLE_BED = 'Double Bed'

    ROOM_TYPE_CHOICES = (
        (AC, 'AC'),
        (NON_AC, 'Non-AC'),
        (SINGLE_BED, 'Single Bed'),
        (DOUBLE_BED, 'Double Bed'),
    )

    room_type = models.CharField(max_length=100, choices=ROOM_TYPE_CHOICES)
    canceled = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Dynamic(models.Model):
    desc1=models.TextField()
    desc2=models.TextField()
    img=models.ImageField(upload_to='dynamic')
    img1=models.ImageField(upload_to='dynamic')
    img2=models.ImageField(upload_to='dynamic')
    img3=models.ImageField(upload_to='dynamic')
    img4=models.ImageField(upload_to='dynamic')
    img5=models.ImageField(upload_to='dynamic')

    def __str__(self):
        return self.desc1

class Package2(models.Model):
    desc1=models.TextField()
    desc2=models.TextField()
    desc3=models.TextField()
    img=models.ImageField(upload_to='package2')
    img1=models.ImageField(upload_to='package2')
    img2=models.ImageField(upload_to='package2')
    name=models.CharField(max_length=100)
    hotelimg=models.ImageField(upload_to='package2')
    hotelname=models.CharField(max_length=50)
    hoteldesc=models.TextField()

class ViewHotels(models.Model):
    img=models.ImageField(upload_to='viewhotels')
    img1=models.ImageField(upload_to='viewhotels')
    img2=models.ImageField(upload_to='viewhotels')
    name=models.CharField(max_length=100)
    name1=models.CharField(max_length=100)
    name2=models.CharField(max_length=100)
    hotelname=models.CharField(max_length=100)
    desc=models.TextField()
    desc1=models.TextField()
    desc2=models.TextField()
    review=models.TextField()
    review1=models.TextField()
    review2=models.TextField()
    rating=models.PositiveIntegerField()
    rating1=models.PositiveIntegerField()
    rating2=models.PositiveIntegerField()
    price=models.IntegerField()
    price1=models.IntegerField()
    price2=models.IntegerField()

# Create your models here.
