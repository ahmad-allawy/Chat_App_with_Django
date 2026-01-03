from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm
from .models import *


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("chat-lists")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("chat-lists")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

@login_required
def HomeView(request):
    # get loggin user
    user = request.user
    # get rooms for this user
    rooms = Room.objects.filter(members=user).all()
    print(rooms)
    context = {
        "rooms": rooms
    }
    return render(request, "chat.html", context)




def RoomView(request, room_name, username):
    return render (request, "room.html")