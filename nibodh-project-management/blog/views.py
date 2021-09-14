from django.shortcuts import render , redirect
from . models import blog 
# Create your views here.
def bloglist(request):
    blog_list = blog.objects.all()
    
    params ={
        
        "data" : blog_list
    }
    return render(request, "blog/bloglist.html",params)

def blogcreate(request):
    title = request.POST.get("title")
    body = request.POST.get("body")
    author = request.user
    if(request.FILES):
        image = request.FILES["image"]
        newBlog = blog(title= title ,image = image , body=body , author = author)
    else:
        newBlog = log(title= title , body=body , author = author)    
    
    newBlog.save()
    return redirect("/blog/")


    
     


def blogview(request):
    
    
    
    
    return render(request, "blog/blogcreate.html")   

def blogdetails(request):
    Blog = blog.objects.get(id=id)
    params ={
        "blog" : blog
    }
    
    
    
    return render(request, "blog/blogdetails.html",params)

