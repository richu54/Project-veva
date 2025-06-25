
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('user_account',views.user_account,name='user_account'),
    path('user_profile_update/<int:id>',views.user_profile_update,name='user_profile_update'),
    path('user_profile_update/user_profile_updates/<int:id>',views.user_profile_updates,name='user_profile_updates'),
    path('additional_info',views.addi_info),
    path('product_browsing',views.product_browsing,name='product_browsing'),
    path('product_detailes/<int:id>',views.product_detailes,name='product_detailes'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('delete-wishlist', views.delete_wishlist, name='delete_wishlist'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('add_shipping_address',views.add_shipping_address,name='add_shipping_address'),
    path('delete_shipping_address/<int:id>',views.delete_shipping_address,name='delete_shipping_address'),
    path('update_shipping_address/<int:id>',views.update_shipping_address,name='update_shipping_address'),
    path('update_shipping_address/updates_shipping_address/<int:id>',views.updates_shipping_address,name='updates_shipping_address'),
    path('show_cart', views.show_cart, name='show_cart'),
    path('update-cart/<int:cart_id>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('remove_cart_item/<int:id>/',views.remove_cart_item,name='remove_cart_item'),
]
