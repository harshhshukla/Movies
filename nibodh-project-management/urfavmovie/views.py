from django.shortcuts import render
from django.http import HttpResponse
from . models import favmovie , Contact 


# Create your views here.
import json

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


def checkout(request):
    str = request.POST.get("cartJson")
    cart = json.loads(str)
    currentCart = cart
   
    print(currentCart)
    totalPrice = 0 
    for id in cart:
    
    
   


    


        temp= cart[id]
        print(temp["value"])
        tempOb = favmovie.objects.get(id=id)
        price = tempOb.RentPrice
        temp["price"]=price
        temp["totalItemPrice"] = price * temp["value"]
        totalPrice = totalPrice + temp["totalItemPrice"]
        currentCart[id] = temp 
    print(totalPrice)
    params = {
        "totalPrice" : totalPrice,
        "data": currentCart
    }
    
   
   
    return render(request, "favmovie\checkout.html",params)

  

def Proced(request):
       return render(request, "favmovie\proceed.html",)
    
    





