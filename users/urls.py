from . import views #from users app views
from django.urls import path
from django.contrib.auth import views as auth_views # from contrib.auth app views

urlpatterns = [
    path('register/', views.register, name="users-register"),
    path('profile/', views.profile, name="users-profile"),
    path('update/', views.update, name='users-update'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')

]
