from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("chat-lists/", views.HomeView, name="chat-lists"),
    path("<str:room_name>/<str:username>/", views.RoomView, name="room")
]