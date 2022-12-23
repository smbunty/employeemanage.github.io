from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def ndex(request):
    return render (request,'ndex.html')
def signup (request):
    return render(request,'signup.html') 
def signin (request):
    return render(request,'signin.html') 
def e (request):
    return render(request,'e.html')      
    
def signupage (request):
    if request.method=="POST":
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        usr=request.POST['username']
        email=request.POST['email']
        pwd=request.POST["password"]
        try:
            user=User.objects.get(username=usr)
            return render(request,'signup.html')
        except:
            user=User.objects.create_user(first_name=fname,last_name=lname,username=usr,email=email,password=pwd)
            user.save()
            return render(request,'signup.html')             

    else:
        return render(request,'signup.html')
def signinpage(request):
    if request.method=="POST":
        usr=request.POST['username']
        pwd=request.POST['password']
        user=auth.authenticate(username=usr,password=pwd)
        if user is not None:
            auth.login (request,user)
            return render (request,'userhome.html')
        else:
            return render (request,'signup.html')
    else:
        return render (request,'signin.html') 
def user(request):
    return render(request,'userhome.html')
def logout(request):
    auth.logout(request)
    return render(request,'signup.html')    