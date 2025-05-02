from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from .models import user_register
import random

# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'index.html')

def signup(request):
    if request.method == "POST":
        email = request.POST.get("Email", "").strip()
        password = request.POST.get("Password", "").strip()
        name = request.POST.get("Name", "").strip()
        mobile = request.POST.get("Mobile", "").strip()

        if user_register.objects.filter(user_email=email).exists():
            return render(request, 'signup.html', {'error': 'Email already registered'})

        otp = str(random.randint(100000, 999999))

        request.session['signup_data'] = {
            'email': email,
            'password': make_password(password),
            'name': name,
            'mobile': mobile,
            'otp': otp
        }

        return render(request, 'signup_otp.html', {'otp': otp})

    return render(request, 'signup.html')


def signup_otp(request):
    if request.method == "POST":
        user_otp = request.POST.get("signup-otp", "").strip()
        session_data = request.session.get('signup_data')

        if not session_data:
            return redirect('signup')

        if user_otp == session_data.get('otp'):
            try:
                user_register.objects.create(
                    user_email=session_data['email'],
                    user_password=session_data['password'],
                    user_name=session_data['name'],
                    user_mobile=session_data['mobile']
                )
                del request.session['signup_data']
                return render(request, 'index.html', {'signup_success': True})
            except Exception as e:
                return render(request, 'signup_otp.html', {
                    'error': f"Error saving user: {str(e)}",
                    'otp': session_data.get('otp')
                })
        else:
            return render(request, 'signup_otp.html', {
                'error': 'Invalid OTP',
                'otp': session_data.get('otp')
            })

    return redirect('signup')
