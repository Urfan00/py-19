from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm


def login_view(request):

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, 'Login oldunuz.')
                return redirect('contact')
            else:
                messages.add_message(request, messages.ERROR, 'KullaniciAdi veya şifre yanlış')

    context = {
        'form': form
    }

    return render(request, 'login.html', context)
