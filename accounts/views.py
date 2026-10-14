from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile


def login_view(request):
    # Already logged in? Skip the form.
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Reads the users table and checks the hashed password
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # creates the session, updates last_login
            if not request.POST.get("remember"):
                request.session.set_expiry(0)  # expire when browser closes
            return redirect("home")

        messages.error(request, "Invalid username or password")

    return render(request, "accounts/login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        password = request.POST.get("password")
        confirm = request.POST.get("confirm_password")

        if not username or not password:
            messages.error(request, "Username and password are required")
        elif password != confirm:
            messages.error(request, "Passwords do not match")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "That username is already taken")
        else:
            # SAVE to the database (create_user hashes the password)
            user = User.objects.create_user(
                username=username, email=email, password=password
            )
            Profile.objects.create(user=user, phone=phone)
            messages.success(request, "Account created. You can log in now.")
            return redirect("login")

    return render(request, "accounts/register.html")


@login_required(login_url="login")
def home_view(request):
    # READ all saved records from the database
    profiles = Profile.objects.select_related("user").order_by("-created_at")
    return render(request, "accounts/home.html", {"profiles": profiles})


def logout_view(request):
    logout(request)
    return redirect("login")