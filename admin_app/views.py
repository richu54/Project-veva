from django.shortcuts import render,redirect
from veva.models import user_register
from user_app.models import additional_info
from django.db.models import Q
from django.utils.dateparse import parse_date
from datetime import datetime, time
from django.contrib import messages
from .models import add_product

# Create your views here.

def admin_dash(request):
    return render(request,'admin-dash.html')


def manage_user(request):
    data = user_register.objects.all()
    return render(request,'manage_user.html',{'res':data})

def user_delete(request,id):
    data = user_register.objects.get(pk=id)
    data.delete()
    return redirect(manage_user)

def user_update(request,id):
    data = user_register.objects.get(pk=id)
    return render(request,'manage-user-update.html',{'res':data})

def user_updates(request,id):
    if request.method == "POST":
        POST = user_register.objects.get(pk=id)
        POST.user_email = request.POST.get("Email")
        POST.user_password = request.POST.get("Password")
        POST.user_name = request.POST.get("Name")
        POST.user_mobile = request.POST.get("Mobile")
        POST.save()

        return redirect(manage_user)
    return render(request,'manage-user-update.html')

def search_user(request):
    query = request.GET.get('query', '')
    if query:
        users = user_register.objects.filter(
            Q(user_name__icontains=query) | Q(user_email__icontains=query)
        )
    else:
        users = user_register.objects.all()
    
    return render(request, 'manage_user.html', {'res': users})


def filter_user(request):
    users = user_register.objects.all()
    start_id = request.GET.get("start_id")
    end_id = request.GET.get("end_id")
    reg_date = request.GET.get("reg_date")

    if start_id and end_id:
        users = users.filter(id__gte=start_id, id__lte=end_id)

    if reg_date:
        try:
            date_obj = parse_date(reg_date)
            if date_obj:
                start_of_day = datetime.combine(date_obj, time.min)
                end_of_day = datetime.combine(date_obj, time.max)
                users = users.filter(registered_date__range=(start_of_day, end_of_day))
        except ValueError:
            pass

    return render(request, 'manage_user.html', {'res': users})

def manage_u_addi_info(request,id):
    try:
        data = additional_info.objects.get(pk=id)
    except additional_info.DoesNotExist:
        data = None

    return render(request, 'manage-u-additional-info.html', {'res': data})

def delete_addi_info(request,id):
    try:
        data = additional_info.objects.get(pk=id)
        data.delete()
        return redirect('manage_user') 
    except additional_info.DoesNotExist:
        messages.error(request, "Additional information not found.")
        return redirect('manage_user') 


def manage_u_info_update(request,id):
    data = additional_info.objects.get(pk=id)
    return render(request,'manage-u-info-update.html',{'res':data})

def manage_u_info_updates(request,id):
    if request.method == "POST":
        address = request.POST.get("address")
        state = request.POST.get("state")
        postal_code = request.POST.get("postal_code")
        dob = request.POST.get("dob")
        gender = request.POST.get("usergender")

        data = additional_info(id=id,user_address=address,user_state=state,user_pincode=postal_code,user_dob=dob,gender=gender)
        data.save()
        return redirect(manage_user)
    
    return render(request,'manage-u-info-update.html')

def add_products(request):
    if request.method == "POST":
        product_image = request.FILES.get("product_image")
        product_invoice = request.POST.get("product_invoice")
        product_name = request.POST.get("product_name")
        product_description = request.POST.get("product_description")
        product_brand = request.POST.get("product_brand")
        product_price = request.POST.get("product_price")
        product_offer_price = request.POST.get("product_offer_price")
        product_size = request.POST.get("product_size")
        product_offer = request.POST.get("product_offer")
        product_category = request.POST.get("product_category")

        data = add_product(product_image=product_image,product_invoice=product_invoice,product_name=product_name,product_description=product_description,product_brand=product_brand,product_price=product_price,product_offer_price=product_offer_price,product_size=product_size,product_offer=product_offer,product_category=product_category)
        data.save()
        messages.success(request, 'Product added successfully!')

    return render(request,'add-products.html')

def manage_products(request):
    data = add_product.objects.all()
    return render(request,'manage-products.html',{'res':data})

def search_product(request):
    query = request.GET.get('query', '')
    if query:
        product = add_product.objects.filter(
            Q(product_invoice__icontains = query) |
            Q(product_name__icontains = query) |
            Q(product_description__icontains = query) |
            Q(product_brand__icontains = query) |
            Q(product_category__icontains = query)
        )
    else:
        product = add_product.objects.all()

    return render(request,'manage-products.html',{'res':product})

def filter_product(request):
    product = add_product.objects.all()
    start_id = request.GET.get("start_id")
    end_id = request.GET.get("end_id")
    invoice = request.GET.get("pro-invoice")
    name = request.GET.get("pro-name")
    brand = request.GET.get("pro-brand")
    category = request.GET.get("pro-category")

    if start_id:
        product = product.filter(id__gte=start_id)

    if end_id:
        product = product.filter(id__lte=end_id)
    
    if invoice:
        product = add_product.objects.filter(product_invoice__icontains = invoice)

    if name:
        product = add_product.objects.filter(product_name__icontains = name)

    if brand:
        product = add_product.objects.filter(product_brand__icontains = brand)

    if category:
        product = add_product.objects.filter(product_category__icontains = category)

    return render(request,'manage-products.html',{'res':product})

def update_product(request,id):
    data = add_product.objects.get(pk=id)

    return render(request,'update-products.html',{'res':data})

def updates_product(request,id):
    if request.method == "POST":
        product_image = request.FILES.get("product_image")
        product_invoice = request.POST.get("product_invoice")
        product_name = request.POST.get("product_name")
        product_description = request.POST.get("product_description")
        product_brand = request.POST.get("product_brand")
        product_price = request.POST.get("product_price")
        product_offer_price = request.POST.get("product_offer_price")
        product_size = request.POST.get("product_size")
        product_offer = request.POST.get("product_offer")
        product_category = request.POST.get("product_category")

        data = add_product(id=id,product_image=product_image,product_invoice=product_invoice,product_name=product_name,product_description=product_description,product_brand=product_brand,product_price=product_price,product_offer_price=product_offer_price,product_size=product_size,product_offer=product_offer,product_category=product_category)
        data.save()
        messages.success(request, 'Product updated successfully!')
        return redirect(manage_products)


    return render(request,'update-products.html')

def delete_product(request,id):
    data = add_product.objects.get(pk=id)
    data.delete()

    return redirect(manage_products)
