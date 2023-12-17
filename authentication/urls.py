from django.urls import path
from . import views

urlpatterns = [
    path('admin_register',views.admin_registration,name='admin_register'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('admin_profile/<int:user_id>/', views.admin_profile, name='admin_profile'),
    
    path('user_register',views.user_registration,name='user_register'),
    path('user_login',views.user_login,name='user_login'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('user_profile/<int:user_id>/', views.user_profile, name='user_profile'),

    path('hotel_register',views.hotel_registration,name='hotel_register'),
    path('hotel_login',views.hotel_login,name='hotel_login'),
    path('hotel_logout',views.hotel_logout,name='hotel_logout'),
    path('hotel_profile/<int:user_id>/', views.hotel_profile, name='hotel_profile'),

]