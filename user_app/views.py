from django.shortcuts import render, redirect
from veva.models import user_register
from .models import additional_info
from django.contrib import messages
from admin_app.models import add_product
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Wishlist

# Create your views here.

def user_account(request):
    if 'uid' not in request.session:
        messages.warning(request, "Please login to access your account")
        return redirect('login') 
    
    try:
        user_id = request.session['uid']
        data = user_register.objects.get(pk=user_id)
        data_2 = additional_info.objects.filter(id=user_id).first()

        wished_ids = Wishlist.objects.filter(user_id=user_id) \
                                 .values_list('product_id', flat=True)
        wishlist_products = add_product.objects.filter(id__in=wished_ids)
        
        return render(request, 'user-account.html', {'res': data,'reg': data_2, 'wishlist_products': wishlist_products, 'wished_ids': wished_ids,})
        
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

    query = request.GET.get("query", "").strip()

    all_products = add_product.objects.all()

    if query:
        all_products = all_products.filter(
            Q(product_invoice__icontains=query) |
            Q(product_name__icontains=query) |
            Q(product_description__icontains=query) |
            Q(product_brand__icontains=query) |
            Q(product_category__icontains=query.replace(" ", "_"))  
        )

    wished_ids = []
    wishlist_products = []
    if request.session.get('uid'):
        wished_ids = Wishlist.objects.filter(user_id=request.session['uid']) \
                                     .values_list('product_id', flat=True)
        wishlist_products = add_product.objects.filter(id__in=wished_ids)

    fresh_products = add_product.objects.filter(product_category = 'Fresh_Products')
    dairy_eggs = add_product.objects.filter(product_category = 'Dairy_Eggs')
    meat_seafood = add_product.objects.filter(product_category = 'Meat_Seafood')
    pantry = add_product.objects.filter(product_category = 'Pantry')
    frozen_products = add_product.objects.filter(product_category = 'Frozen_Products')
    snacks_bakery = add_product.objects.filter(product_category = 'Snacks_Bakery')
    drinks = add_product.objects.filter(product_category = 'Drinks')
    homeware = add_product.objects.filter(product_category = 'Homeware')

    data = {
        'all_products' : all_products,
        'Fresh_Products' : fresh_products,
        'Dairy_Eggs' : dairy_eggs,
        'Meat_Seafood' : meat_seafood,
        'Pantry' : pantry,
        'Frozen_Products' : frozen_products,
        'Snacks_Bakery' : snacks_bakery,
        'Drinks' : drinks,
        'Homeware' : homeware,

        'wished_ids': wished_ids,
        'wishlist_products': wishlist_products,
    }

    return render(request,'product_browsing.html', data)

def product_detailes(request,id):
    data = add_product.objects.get(pk=id)

    wished_ids = []
    wishlist_products = []
    if request.session.get('uid'):
        wished_ids = Wishlist.objects.filter(user_id=request.session['uid']) \
                                     .values_list('product_id', flat=True)
        wishlist_products = add_product.objects.filter(id__in=wished_ids)

    return render(request,'product-detailes.html',{'res':data, 'wished_ids': wished_ids,'wishlist_products': wishlist_products})

def wishlist(request):
    if request.method == "GET":
        if 'uid' not in request.session:
            return JsonResponse({'status': 'unauthorized'}, status=401)

        user_id = request.session['uid']
        product_id = request.GET.get('product_id')

        product = get_object_or_404(add_product, id=product_id)

        wish, created = Wishlist.objects.get_or_create(user_id=user_id, product=product)
        if created:
            return JsonResponse({'status': 'added'})
        else:
            wish.delete()
            return JsonResponse({'status': 'removed'})
        
def delete_wishlist(request):

    if request.method == "POST":
        if 'uid' not in request.session:
            return JsonResponse({'status': 'unauthorized'}, status=401)

        user_id = request.session['uid']
        product_id = request.POST.get('product_id')

        Wishlist.objects.filter(user_id=user_id, product_id=product_id).delete()
        return JsonResponse({'status': 'deleted'})