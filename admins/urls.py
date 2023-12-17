from django.urls import path
from .import views
urlpatterns = [
    path('adminhome',views.admin_home,name='adminhome'),
     
    path('add_dest/',views.add_destinations,name='admin_destination'),
    path('dest_admin',views.dest_admin,name='dest_admin'),
    path('update_dest/<int:dest_id>/', views.update_dest, name='update_dest'),
    path('delete_dest/<int:dest_id>/', views.delete_dest, name='delete_dest'),

    path('addpack/',views.add_packages,name='admin_package'),
    path('pack_admin',views.pack_admin,name='pack_admin'),
    path('update_pack/<int:pack_id>/', views.update_pack, name='update_pack'),
    path('delete_pack/<int:pack_id>/', views.delete_pack, name='delete_pack'),    
]
