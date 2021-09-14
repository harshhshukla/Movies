from . import views
from django.urls import path 



urlpatterns = [
  
    path('bloglist/', views.bloglist),
    path('blogdetails/<int:id>',views.blogdetails),
    path('blogcreate/', views.blogcreate),
    path('create/', views.blogview),
  
    
    
]