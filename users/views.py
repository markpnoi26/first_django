from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm => moved to forms.py but with an extra field
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    data = {'form': form}
    return render(request, 'users/register.html', data)

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def update(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile has been updated')
            return redirect('users-profile')
    else:
        print(request.user)
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        data = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'users/update.html', data)
