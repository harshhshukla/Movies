from . import views
from django.urls import path , include



urlpatterns = [
   
    path('', views.Index),
    path('favlist/', views.Favlist),
    path('contactus/', views.contactUs),
    path('contactUsSubmit/', views.contactUsSubmit),
    path('checkout/',views.checkout),
    path('Proced/',views.Proced),
  
   
]