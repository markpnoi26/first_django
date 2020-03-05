from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.register, name="users-register"),
    path('sign_in/', views.sign_in, name="users-sign_in")

]
