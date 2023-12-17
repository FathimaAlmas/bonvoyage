"""
URL configuration for voyage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .import views

urlpatterns = [
    path('hotel',views.hotel,name='hotel'),
    
    path('destinations',views.destinations,name='destinations'),

    path('packages',views.packages,name='packages'),
    
    path('booking/', views.booking, name='booking'),
   
    path('search',views.searchDestinations,name='search'),

    path('dynamic/<int:destinations_id>/',views.dynamic,name='dynamic'),

    path('pack2/<int:package2_id>/',views.package2, name='pack2'),

    path('viewhotels/<int:hotels_id>/',views.view_hotels,name='viewhotels'),

    path('payment/',views.payment.as_view(),name='payment'),
    path('charge/',views.charge,name='charge'),
    path('error/',views.error,name='error'),
    path('receipt/', views.receipt, name='receipt'),

    path('cancel_book/<int:booking_id>/', views.cancel_booking, name='cancel_book'),
    path('booking_list/',views.booking_list,name='booking_list')
     
]
