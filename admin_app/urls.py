
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin_dash',views.admin_dash),
    path('manage_user',views.manage_user,name='manage_user'),
    path('user_delete/<int:id>',views.user_delete,name='user_delete'),
    path('user_update/<int:id>',views.user_update,name='user_update'),
    path('user_update/user_updates/<int:id>',views.user_updates,name='user_updates'),
    path('search_user',views.search_user,name='search_user'),
    path('filter_user',views.filter_user,name='filter_user')
]
