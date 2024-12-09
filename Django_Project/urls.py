from django.contrib import admin
from django.urls import path 
from My_Application import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Blogs.html/', views.blogs, name='blogs'),
    path('Contacts.html/', views.contacts, name='contacts'),
    path('ourcar/', views.ourcar, name='our_car'),  
    path('About.html/', views.about, name='about'), 
    path('service.html/', views.service, name='service'),
    path('ourtestimonial/', views.our_testimonial, name='our_testimonial'),
    path('carfeatures/', views.carfeatures, name='car_features'), 
    path('ourteam/', views.our_team, name='our_team'),
    path('bookcar.html/', views.book_car, name='bookcar'),
   


    
]
