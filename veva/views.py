from django.shortcuts import render,redirect
from .models import user_register
import random
from django.contrib import messages
from .models import send_message
import requests
from admin_app.models import add_product
from django.utils.timezone import now
from django.db.models import Sum
from user_app.models import Order_details

# Create your views here.

def index(request):
    all_products = list(add_product.objects.filter(product_offer__gte=15))
    random.shuffle(all_products)
    selected_products = all_products[:12]

    offer_recommendations = []
    for p in selected_products:
        if p.product_price and p.product_offer_price and p.product_price > p.product_offer_price:
            discount = round(((p.product_price - p.product_offer_price) / p.product_price) * 100)
        else:
            discount = 0
        offer_recommendations.append({
            "id": p.id,
            "name": p.product_name,
            "price": p.product_offer_price,
            "original_price": p.product_price,
            "image_url": p.product_image.url,
            "size": p.product_size,
            "offer_percent": discount,
        })
    return render(request,'index.html', {"offer_recommendations": offer_recommendations})

def home(request):
    all_products = list(add_product.objects.filter(product_offer__gte=15))
    random.shuffle(all_products)
    selected_products = all_products[:12]

    offer_recommendations = []
    for p in selected_products:
        if p.product_price and p.product_offer_price and p.product_price > p.product_offer_price:
            discount = round(((p.product_price - p.product_offer_price) / p.product_price) * 100)
        else:
            discount = 0
        offer_recommendations.append({
            "id": p.id,
            "name": p.product_name,
            "price": p.product_offer_price,
            "original_price": p.product_price,
            "image_url": p.product_image.url,
            "size": p.product_size,
            "offer_percent": discount,
        })
    return render(request,'index.html', {"offer_recommendations": offer_recommendations})

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
                user = user_register.objects.create(
                    user_email=session_data['email'],
                    user_password=session_data['password'],
                    user_name=session_data['name'],
                    user_mobile=session_data['mobile']
                )
                request.session['uid'] = user.id
                request.session['uname'] = user.user_name
                request.session['uemail'] = user.user_email
                request.session['utel'] = user.user_mobile
                request.session['user'] = 'user'

                del request.session['signup_data']

                return redirect('user_account')

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
    if request.method == "POST":
        useremail = request.POST.get('Email')
        userpass = request.POST.get('Password')

        total_users = user_register.objects.count() 
        total_products = add_product.objects.count()
        pending_requests = send_message.objects.count()
        today = now().date()
        first_day = today.replace(day=1)

        monthly_sales = Order_details.objects.filter(
        created_at__date__gte=first_day,
        status="Delivered"
        ).aggregate(total=Sum('total_amount'))['total'] or 0

        if useremail == 'rinshad@gmail.com' and userpass == '7654321':
            request.session['email'] = useremail
            request.session['admin'] = 'admin'
            return render(request, 'admin-dash.html',{'total_users': total_users, 'total_products':total_products, 'pending_requests':pending_requests, 'monthly_sales':monthly_sales})

        elif user_register.objects.filter(user_email=useremail, user_password=userpass).exists():
            userdetails = user_register.objects.get(user_email=useremail, user_password=userpass)
            if userdetails.user_password == userpass:
                request.session['uid'] = userdetails.id
                request.session['uname'] = userdetails.user_name
                request.session['uemail'] = userdetails.user_email
                request.session['utel'] = userdetails.user_mobile
                request.session['user'] = 'user'
                messages.success(request, "Login successful")
                return redirect(index)
            else:
                return render(request, 'login.html', {'error': 'Incorrect password'})

        else:
            return render(request, 'login.html', {'error': 'Email not exist'})

    return render(request, 'login.html')

def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(index)
    

def reset_pass_step1(request):
    if request.method == "POST":
        email = request.POST.get("check_email", "").strip()
        if not user_register.objects.filter(user_email=email).exists():
            return render(request, 'reset-pass-step1.html', {'error': 'Email not found'})

        otp = str(random.randint(100000, 999999))
        request.session['reset_data'] = {'email': email, 'otp': otp}
        return render(request, 'reset-pass-step2.html', {'otp': otp})

    return render(request, 'reset-pass-step1.html')


def reset_pass_step2(request):
    if request.method == "POST":
        user_otp = request.POST.get("reset_otp", "").strip()
        session_data = request.session.get('reset_data')

        if not session_data:
            return redirect('reset_pass_step1')

        if user_otp == session_data.get('otp'):
            return render(request, 'reset-pass-step3.html')

        return render(request, 'reset-pass-step2.html', {
            'error': 'Invalid OTP',
            'otp': session_data.get('otp')  # demo otp
        })

    return redirect('reset_pass_step1')


from django.shortcuts import redirect

def reset_pass_step3(request):
    if request.method == "POST":
        new_password = request.POST.get("reset_pass", "").strip()
        session_data = request.session.get('reset_data')

        if not session_data:
            return redirect('reset_pass_step1')

        try:
            user = user_register.objects.get(user_email=session_data['email'])
            user.user_password = new_password 
            user.save()
            del request.session['reset_data']
            messages.success(request, "Password reset successful.")
            return redirect('login')

        except user_register.DoesNotExist:
            return redirect('reset_pass_step1')

    return redirect('reset_pass_step1')

def contact(request):

    if 'uid' not in request.session:
        messages.error(request, "Please login to access the contact form.")
        return redirect('login')
    
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        data = send_message(name=name,email=email,subject=subject,message=message)
        data.save()

    return render(request,'contact.html')

def terms_and_condition(request):

    return render(request,'terms-and-condition.html')

def privacy_and_policy(request):

    return render(request,'privacy-and-policy.html')

def faq(request):
    return render(request,'faq.html')


