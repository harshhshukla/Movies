from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return HttpResponse("yoo")

def home(request):
   return render(request,"index.html")


def form(request):
   return render(request,"form.html")

def showname(request):
    
    params = {
        "name" : request.GET.get("name"),
        "surname" : request.GET.get("surname"),
        "phone_number" : request.GET.get("phone_number"),
        "Email_address" : request.GET.get("Email_address"),
        "Password" : request.GET.get("Password"),
         "Date_Of_Birth" : request.GET.get("Date_Of_Birth"),
        "youtube" : request.GET.get("youtube")
        }
    print(params)
    return render(request,"showData.html",params)

