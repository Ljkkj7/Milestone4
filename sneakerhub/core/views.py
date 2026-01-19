from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomerUserCreationForm(UserCreationForm):
    """Custom signup form for customers"""
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'This email is already registered.'
            )
        return email
    
    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match.")
        elif len(password2) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        elif not any(char.isdigit() for char in password2):
            raise forms.ValidationError("Password must contain at least one digit.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
# class CreatorUserCreationForm(UserCreationForm):
    


class homePage(TemplateView):
    template_name = "home.html"


def customerSignupView(request):
    """Customer signup view"""
    if request.method == 'POST':
        form = CustomerUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('marketplace')
    else:
        form = CustomerUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def customerLoginView(request):
    """Customer login view"""
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('marketplace')
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')


def customerLogoutView(request):
    """Customer logout view"""
    logout(request)
    return redirect('home')