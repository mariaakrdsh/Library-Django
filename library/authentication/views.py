from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from authentication.models import CustomUser


class LoginForm(forms.Form):
    email = forms.EmailField(initial="")
    password = forms.CharField(initial="", widget=forms.PasswordInput)


class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password']


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/all')
            else:
                return render(request, 'login.html', {'error': 'No such user.', 'form': form})
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password.', 'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('login/')
    else:
        form = CustomUserForm()
    return render(request, 'register.html', {'form': form})
