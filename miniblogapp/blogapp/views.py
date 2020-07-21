 
from django.shortcuts import render , HttpResponseRedirect
 
from .forms import  LoginForm,SignupForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .models import post
 
# Create your views here.


def home(request): 
    post1 = post.objects.all()      
    return render(request, 'blog/home.html',{'post1':post1})   

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')

def dashboard(request):
    post1 = post.objects.all()
    return render(request,'blog/dashboard.html',{'poast1':post1})

def logout(request):
    return render(request,'/')

def signin(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulation!!")
            form.save()
    else:
        form = SignupForm()  
    return render(request,'blog/signin.html',{'form': form} )

def login_1(request):
    

    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request,data=request.POST) 
            if form.is_valid():
               uname= form.cleaned_data['username']
               upass= form.cleaned_data['password'] 
               user= authenticate(username=uname,password=upass)
               if user is not None:              
                  login(request,user)
                  messages.success(request,'Loged Succesfully')
                  return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request,'blog/login.html',{'form': form})
    else:
        return HttpResponseRedirect ('/dashboard/')



   
 
