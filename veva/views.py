from django.shortcuts import render,redirect
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
            'password': password,
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

def login(request):
    useremail = request.POST.get('Email')
    userpass = request.POST.get('Password')

    if useremail == 'rinshad@gmail.com' and userpass == '7654321':
        request.session['email'] = useremail
        request.session['admin'] = 'admin'
        return render(request,'index.html',{'status':'Admin login Successful'})
    
    elif user_register.objects.filter(user_email=useremail,user_password=userpass).exists():
        userdetails = user_register.objects.get(user_email=request.POST['Email'],user_password=userpass)
        if userdetails.user_password == request.POST['Password']:
            request.session['uid'] = userdetails.id
            request.session['uname'] = userdetails.user_name
            request.session['uemail'] = userdetails.user_email
            request.session['utel'] = userdetails.user_mobile
            request.session['user'] = 'user'
            return render(request,'index.html',{'status':'User login Successful'})
    else :
        return render(request,'login.html',{'error':'User login Failed'})
    

def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(index)
    