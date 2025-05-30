
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('user_account',views.user_account,name='user_account'),
    path('user_profile_update/<int:id>',views.user_profile_update,name='user_profile_update'),
    path('user_profile_update/user_profile_updates/<int:id>',views.user_profile_updates,name='user_profile_updates'),
    path('additional_info',views.addi_info),
    path('product_browsing',views.product_browsing,name='product_browsing'),
    path('product_detailes',views.product_detailes,name='product_detailes'),
]
