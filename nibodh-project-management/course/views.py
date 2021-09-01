from django.shortcuts import render
from django.http import HttpResponse
from . models import course
# Create your views here.


def Index(request):
    return render(request,"course\home.html")



def List(request):
    print(course.objects.all())
    params = {
        "list" : [1,2,3,4,5,6,7]
    }
    
    return render(request,"course\index.html",params)