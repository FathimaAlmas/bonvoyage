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
    path('',views.index,name='index'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),

    path('blog',views.blog,name='blog'),
    path('addblog',views.add_blog,name='add_blog'),
    path('viewblog',views.viewblog,name='viewblog'),
    path('update_blog/<int:blog_id>/', views.update_blog, name='updateblog'),
    path('delete_blog/<int:blog_id>/', views.delete_blog, name='deleteblog'),
    
    
    path('comments_list/', views.comments_list, name='comments_list'),
    path('create_comment/', views.create_comment, name='create_comment'),
    
    path('update_comment/<int:comment_id>/', views.update_comment, name='update_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
    

