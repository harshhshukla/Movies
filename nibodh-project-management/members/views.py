from django.shortcuts import render , redirect
from django.contrib import messages
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout

# Create your views here.

def loginview(request):
    return render(request, "members/login.html",)
 
 
def signupview(request):
     
     return render(request, "members/signup.html",)
     

 
def loginsubmit(request):
      if request.method == "POST":
          username = request.POST.get("username")
          password = request.POST.get("pass")
          user = authenticate(username = username , password = password )
          
          if user is not None:
               login(request,user)
               messages.add_message(request, messages.SUCCESS, 'Login sucess ')
               return redirect("/course/")
          else:
               messages.add_message(request, messages.ERROR, 'username and password is not valid ')
               return redirect("/members/loginview/")
          
      else:
          messages.add_message(request, messages.ERROR, 'Please login')
          return redirect("/members/loginview/")
def signupsubmit(request):
     if request.method == "POST":
          username = request.POST.get("username")
          email = request.POST.get("email")
          pass1 = request.POST.get("pass1")
          pass2 = request.POST.get("pass2")
          First_name = request.POST.get("First_name")
          Last_name = request.POST.get("Last_name")
          
          
          
          # validations
          if(not (len(pass1)>7 and not pass1.isalnum() )): 
               messages.add_message(request, messages.ERROR, 'Password must be longer then 8 should contain sybol ')
               return redirect("/members/signupview/")
          
          if(not(pass1==pass2)):
               messages.add_message(request, messages.INFO, 'both the password must be same ')
               return redirect("/members/signupview/")
          else:
               newUser = User.objects.create_user(username,email,pass1)
               newUser.first_name = First_name
               newUser.last_name = Last_name
               newUser.save()
               return  redirect( "/members/loginview/")
     else:
          messages.add_message(request, messages.ERROR, 'Please signin')
          return redirect("/members/signupview/")
 
def Logout(request):
     logout(request)
     messages.add_message(request, messages.SUCCESS, 'logout')
     
     return redirect("/course/")
 

 


 
 
