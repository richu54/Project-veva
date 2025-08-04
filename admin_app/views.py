from django.shortcuts import render,redirect
from veva.models import user_register, send_message
from user_app.models import additional_info
from django.db.models import Q
from django.utils.dateparse import parse_date
from datetime import datetime, time
from django.contrib import messages
from .models import add_product
from user_app.models import Order_details
import json
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
from datetime import datetime, timedelta
from django.utils.timezone import now

# Create your views here.

def admin_dash(request):
    total_users = user_register.objects.count()  
    total_products = add_product.objects.count()
    pending_requests = send_message.objects.count()
    today = now().date()
    first_day = today.replace(day=1)

    monthly_sales = Order_details.objects.filter(
    created_at__date__gte=first_day,
    status="Delivered" 
    ).aggregate(total=Sum('total_amount'))['total'] or 0
    return render(request, 'admin-dash.html', {'total_users': total_users, 'total_products':total_products, 'pending_requests':pending_requests, 'monthly_sales':monthly_sales})

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

def admin_order_tracking(request):
    
    pending_orders = Order_details.objects.filter(status="Pending").order_by('-created_at')

    for order in pending_orders:
        try:
            order.product_data = json.loads(order.product)
        except Exception:
            order.product_data = []

    return render(request, 'manage-order-tracking.html', {'orders': pending_orders})

def mark_order_complete(request, id):
    try:
        order = Order_details.objects.get(pk=id)
        order.status = "Delivered"
        order.save()
        messages.success(request, f"Order #{id} marked as Delivered.")
    except Order_details.DoesNotExist:
        messages.error(request, f"Order #{id} not found.")
    return redirect(admin_order_tracking)

def delete_order(request, id):
    try:
        order = Order_details.objects.get(pk=id)
        order.delete()
        messages.success(request, f"Order #{id} deleted.")
    except Order_details.DoesNotExist:
        messages.error(request, f"Order #{id} not found.")
    return redirect(admin_order_tracking)

def admin_order_history(request):

    delivered_or_cancelled_orders = Order_details.objects.filter(
        status__in=['Delivered', 'Cancelled']
    ).order_by('-created_at')

    for order in delivered_or_cancelled_orders:
        try:
            order.product_data = json.loads(order.product)
        except Exception:
            order.product_data = []

    return render(request, 'manage-order-history.html', {'orders': delivered_or_cancelled_orders})

@csrf_exempt
def delete_order_history(request, id):
    if request.method == "POST":
        try:
            order = Order_details.objects.get(id=id, status="Delivered")
            order.delete()
            messages.success(request, "Order history deleted successfully.")
        except Order_details.DoesNotExist:
            messages.error(request, "Order not found or not completed.")
        return redirect(admin_order_history)
    else:
        messages.error(request, "Invalid method.")
        return redirect(admin_order_history)
    
def manage_user_request(request):

    requests = send_message.objects.all()
    return render(request,'manage-user-request.html',{'res':requests})

def delete_user_request(request,id):
    data = send_message.objects.get(pk=id)
    data.delete()
    return redirect(manage_user_request)