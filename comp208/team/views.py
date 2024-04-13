from django.shortcuts import render

def home(request):
    return render(request, 'homepage/homepage.html')

def login_view(request):
    return render(request,'login/login.html')