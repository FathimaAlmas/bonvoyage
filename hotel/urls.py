from django.urls import path
from . import views

urlpatterns = [
    path('submit_hotel/', views.submit_hotel, name='submit_hotel'),
    path('view_submitted_hotels/', views.view_submitted_hotels, name='view_submitted_hotels'),
    path('approve_hotel/<int:pk>/', views.approve_hotel, name='approve_hotel'),
    path('reject_hotel/<int:pk>/', views.reject_hotel, name='reject_hotel'),

    path('hotelhome',views.hotel_home,name='hotelhome'),

    path('addhotel/',views.add_hotel,name='admin_hotel'),
    path('hotel_admin',views.hotel_admin,name='hotel_admin'),
    path('update_hotel/<int:hotel_id>/', views.update_hotel, name='update_hotel'),
    path('delete_hotel/<int:hotel_id>/', views.delete_hotel, name='delete_hotel'),
]