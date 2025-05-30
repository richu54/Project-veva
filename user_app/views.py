from django.shortcuts import render, redirect
from veva.models import user_register
from .models import additional_info
from django.contrib import messages

# Create your views here.

def user_account(request):
    if 'uid' not in request.session:
        messages.warning(request, "Please login to access your account")
        return redirect('login') 
    
    try:
        user_id = request.session['uid']
        data = user_register.objects.get(pk=user_id)
        data_2 = additional_info.objects.filter(id=user_id).first()
        
        return render(request, 'user-account.html', {'res': data,'reg': data_2})
        
    except user_register.DoesNotExist:
        messages.error(request, "User account not found")
        return redirect('home') 
    except Exception as e:
        messages.error(request, "An error occurred while loading your account")
        return redirect('home')  


def user_profile_update(request,id):
    data = user_register.objects.get(pk=id)
    return render(request,'user-profile-update.html',{'res':data})

def user_profile_updates(request,id):
    if request.method == "POST":
        POST = user_register.objects.get(pk=id)
        POST.user_email = request.POST.get("Email")
        POST.user_password = request.POST.get("Password")
        POST.user_name = request.POST.get("Name")
        POST.user_mobile = request.POST.get("Mobile")
        POST.save()
        return redirect(user_account)
    
    return render(request,'user-profile-update.html')

def addi_info(request):
    user_id = request.session['uid']
    if request.method == "POST":
        address = request.POST.get("address")
        state = request.POST.get("state")
        postal_code = request.POST.get("postal_code")
        dob = request.POST.get("dob")
        gender = request.POST.get("usergender")

        data = additional_info(id=user_id,user_address=address,user_state=state,user_pincode=postal_code,user_dob=dob,gender=gender)
        data.save()
        return redirect(user_account)
    
    return render(request,'user-additional-info.html')


def product_browsing(request):
    return render(request,'product_browsing.html')

def product_detailes(request):
    return render(request,'product-detailes.html')