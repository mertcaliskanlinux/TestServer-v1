from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


from .forms import LoginForm

def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
        
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"{username} için oturum açıldı")
                return redirect("users:dashboard")
            else:
                messages.error(request, "Geçersiz kullanıcı adı veya parola")
                return redirect("users:login")
    else:
        form = LoginForm()
    
    return render(request, "registration/login.html", {"form": form})




@login_required
def dashboard(request):
    return render(request, "users/dashboard.html")



def logout_user(request):
    logout(request)
    return redirect("users:login")



def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            
            user = authenticate(request, username=username, password=password)
            login(request, user)
            
            messages.success(request, f"{username} için hesap oluşturuldu")
            return redirect("users:login")
        else:
            messages.error(request, "Geçersiz form")
            return redirect("users:register_user")
    else:
        form = UserCreationForm()
        return render(request, "registration/register.html", {"form": form})
