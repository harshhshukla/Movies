from . import views
from django.urls import path , include



urlpatterns = [
   
    path('', views.Index),
    path('favlist/', views.Favlist),
    path('contactus/', views.contactUs),
    path('contactUsSubmit/', views.contactUsSubmit),
    path('login/', views.Login),
    path('signup/', views.Signup),
    path('blogs/', views.blogs),
    path('blogcreate/', views.blogcreate),
    path('blogdetails/', views.blogdetails),
] 