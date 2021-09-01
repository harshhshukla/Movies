from django.shortcuts import render
from django.http import HttpResponse
from . models import favmovie , Contact 

# Create your views here.


def Index(request):
     return render(request, "favmovie\basic.html")


def Favlist(request):
    Favmoviess = favmovie.objects.all()
    params = {
        "data" : Favmoviess
    }
    return render(request, "favmovie\index.html",params)

def contactUs(request):
    return render(request, "favmovie\contactUs.html",)


def contactUsSubmit(request):
    
    name =request.POST.get("NameCont")
    Email =request.POST.get("EmailCon")
    PhoneNo =request.POST.get("phoneCon")
    Description =request.POST.get("desCon")
    
    newContact = Contact( name=name ,Email=Email ,PhoneNo=PhoneNo ,Descriptionn=Description, )
    newContact.save()
   
    return HttpResponse("hello")

def Login(request):
    return render(request, "favmovie\login.html",)


def Signup(request):
    return render(request, "favmovie\signup.html",)

def blogs(request):
    return render(request, "favmovie\blog.html",)

def blogcreate(request):
    return render(request, "favmovie\blogcreate.html",)

def blogdetails(request):
    return render(request, "favmovie\blogdetails.html",)

