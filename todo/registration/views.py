from django.shortcuts import render, redirect, reverse
from registration.forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import login, authenticate


def registration_view(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)

        if form.is_valid():
            success_url = reverse('registration:login')
            form.save()
            return redirect(success_url)

    context = {
        'form': form
    }
    return render(request, 'registration.html', context)


def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            success_url = reverse('main:main')
            username = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user and user.is_active:
                login(request, user)
                return redirect(success_url)

    context = {
        'form': form
    }
    return render(request, 'login.html', context)
