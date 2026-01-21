from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.conf import settings


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
            sendSignUpConfirmationEmail(user)
        return user

def sendSignUpConfirmationEmail(user):

    subject = "Welcome to SneakerHub!"

    # Plain text fallback message
    plain_message = f"Hello {user.username},\n\nThank you for signing up at SneakerHub! We're excited to have you on board."

    html_message = f"""
    <div style='font-family: Arial, sans-serif; background: #fff; color: #1a1a1a; max-width: 600px; margin: 0 auto; border: 1px solid #eee; border-radius: 8px; box-shadow: 0 2px 8px #f0f0f0;'>
        <div style='background: #fff; border-bottom: 2px solid #000; padding: 24px 32px 12px 32px; text-align: center;'>
            <h1 style='margin: 0; font-size: 28px; font-weight: 900; letter-spacing: -1px; color: #000; text-transform: uppercase;'>SneakerHub</h1>
        </div>
        <div style='padding: 32px;'>
            <h2 style='font-size: 22px; color: #000; margin-top: 0;'>Welcome to SneakerHub!</h2>
            <p style='font-size: 16px; color: #1a1a1a;'>Hi <b>{user.username}</b>,</p>
            <p style='font-size: 16px;'>Thank you for signing up at SneakerHub! We're excited to have you on board.</p>
            <p style='font-size: 16px;'>Start exploring our marketplace and find your perfect pair of sneakers today.</p>
            <p style='font-size: 16px;'>If you have any questions or need assistance, feel free to reach out to our support team.</p>
            <p style='font-size: 15px; color: #888; margin-top: 32px; text-align: center;'>Best Regards,<br>SneakerHub Team</p>
        </div>
    </div>
    """

    send_mail(
        subject,
        plain_message,
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
        html_message=html_message,
    )

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