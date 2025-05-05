from django.shortcuts import render,redirect
from veva.models import user_register
from django.db.models import Q
from django.utils.dateparse import parse_date
from datetime import datetime, time

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
            pass  # Invalid date format, ignore filter

    return render(request, 'manage_user.html', {'res': users})