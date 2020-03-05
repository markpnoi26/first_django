from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm => moved to forms.py but with an extra field
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.
def register(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()

    data = {'form': form}
    return render(request, 'users/register.html', data)


def sign_in(request):
    return render(request, 'users/sign_in.html')
