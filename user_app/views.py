from django.shortcuts import render, redirect
from veva.models import user_register
from .models import additional_info
from django.contrib import messages
from admin_app.models import add_product
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Wishlist
from .models import Shipping_address
from user_app.models import Cart
from django.urls import reverse
from django.http import HttpResponseRedirect

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
            # redirect to login if not logged in
            return redirect('login')

        user_id = request.session['uid']
        product_id = request.POST.get('product_id')

        Wishlist.objects.filter(user_id=user_id, product_id=product_id).delete()
        return redirect('user_account')
    
def add_to_cart(request):
    if 'uid' not in request.session:
        return redirect('login')

    user_id = request.session['uid']
    user = user_register.objects.get(id=user_id) 
    data = Shipping_address.objects.filter(user_id=user_id)

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        anchor = request.POST.get('redirect_anchor', '')

        product = add_product.objects.get(id=product_id)

        cart_item, created = Cart.objects.get_or_create(user=user, product=product)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()

        return HttpResponseRedirect(reverse('product_browsing') + anchor)

    cart_items = Cart.objects.filter(user=user)

    total_mrp = 0
    total_discount = 0
    delivery_fee = 0

    for item in cart_items:
        price = item.product.product_price
        offer = item.product.product_offer
        quantity = item.quantity

        discount = (price * offer) / 100

        total_mrp += price * quantity
        total_discount += discount * quantity

    total_amount = (total_mrp - total_discount) + delivery_fee

    return render(request, 'add-to-cart.html', {'res':data, 'cart_items': cart_items, 'total_mrp': total_mrp, 'total_discount': total_discount, 'delivery_fee': delivery_fee, 'total_amount': total_amount})

def add_shipping_address(request):
    if 'uid' not in request.session:
        return redirect('login')

    uid = request.session['uid']
    user = user_register.objects.get(pk=uid)

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        mobile = request.POST.get("mobile")
        pincode = request.POST.get("pincode")
        locality = request.POST.get("locality")
        address_line = request.POST.get("address_line")
        city = request.POST.get("city")
        state = request.POST.get("state")
        landmark = request.POST.get("landmark")
        alt_phone = request.POST.get("alt_phone")

        data = Shipping_address(user=user,full_name=full_name,mobile=mobile,pincode=pincode,locality=locality,address_line=address_line,city=city,state=state,landmark=landmark,alt_phone=alt_phone)
        data.save()
        return redirect(add_to_cart)

    return render(request,'add-shipping-address.html')

def delete_shipping_address(request,id):
    data = Shipping_address.objects.get(pk=id)
    data.delete()
    return redirect(add_to_cart)

def update_shipping_address(request,id):
    data = Shipping_address.objects.get(pk=id)
    return render(request,'update-shipping-address.html',{'res':data})

def updates_shipping_address(request,id):
    if 'uid' not in request.session:
        return redirect('login')

    uid = request.session['uid']
    user = user_register.objects.get(pk=uid)

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        mobile = request.POST.get("mobile")
        pincode = request.POST.get("pincode")
        locality = request.POST.get("locality")
        address_line = request.POST.get("address_line")
        city = request.POST.get("city")
        state = request.POST.get("state")
        landmark = request.POST.get("landmark")
        alt_phone = request.POST.get("alt_phone")

        data = Shipping_address(id=id,user=user,full_name=full_name,mobile=mobile,pincode=pincode,locality=locality,address_line=address_line,city=city,state=state,landmark=landmark,alt_phone=alt_phone)
        data.save()
        return redirect(add_to_cart)

    return render(request,'update-shipping-address.html')


def show_cart(request):
    if 'uid' not in request.session:
        return redirect('login')
    
    user_id = request.session['uid']
    user = user_register.objects.get(id=user_id)
    cart_items = Cart.objects.filter(user=user)

    return render(request, 'add-to-cart.html', {'cart_items': cart_items})

def update_cart_quantity(request, cart_id):
    if 'uid' not in request.session:
        return redirect('login')

    user_id = request.session['uid']
    try:
        cart_item = Cart.objects.get(id=cart_id, user_id=user_id)
    except Cart.DoesNotExist:
        return redirect('add_to_cart')

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'increase':
            cart_item.quantity += 1
        elif action == 'decrease' and cart_item.quantity > 1:
            cart_item.quantity -= 1
        cart_item.save()

    return redirect('add_to_cart')


def remove_cart_item(request,id):
    if 'uid' not in request.session:
        return redirect('login')

    user_id = request.session['uid']
    try:
        cart_item = Cart.objects.get(pk=id, user_id=user_id)
        cart_item.delete()
    except Cart.DoesNotExist:
        pass

    return redirect(add_to_cart)
