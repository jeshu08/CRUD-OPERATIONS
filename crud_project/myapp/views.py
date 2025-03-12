from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

def home(request):
    return render(request, 'home.html')  


def logout(request):
    auth_logout(request)
    return redirect('login') 



def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.create_user(username=username, password=password)
        user.save()
        login(request, user)
        return redirect("home")  # Redirect to home page after signup
    return render(request, "signup.html")  # Ensure you have a signup.html template
