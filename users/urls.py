from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.register, name="users-register"),
    path('login/', views.sign_in, name="users-login")

]
