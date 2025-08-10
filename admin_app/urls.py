
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin_dash',views.admin_dash,name='admin_dash'),
    path('manage_user',views.manage_user,name='manage_user'),
    path('user_delete/<int:id>',views.user_delete,name='user_delete'),
    path('user_update/<int:id>',views.user_update,name='user_update'),
    path('user_update/user_updates/<int:id>',views.user_updates,name='user_updates'),
    path('search_user',views.search_user,name='search_user'),
    path('filter_user',views.filter_user,name='filter_user'),
    path('manage_u_info_update/<int:id>',views.manage_u_info_update,name='manage_u_info_update'),
    path('manage_u_info_update/manage_u_info_updates/<int:id>',views.manage_u_info_updates,name='manage_u_info_updates'),
    path('add_product',views.add_products),
    path('manage_products',views.manage_products,name='manage_products'),
    path('search_product',views.search_product,name='search_product'),
    path('filter_product',views.filter_product,name='filter_product'),
    path('update_product/<int:id>',views.update_product,name='update_product'),
    path('update_product/updates_product/<int:id>',views.updates_product,name='updates_product'),
    path('delete_product/<int:id>',views.delete_product,name='delete_product'),
    path('admin_order_tracking/', views.admin_order_tracking, name='admin_order_tracking'),
    path('admin_order_complete/<int:id>/', views.mark_order_complete, name='mark_order_complete'),
    path('admin_order_delete/<int:id>/', views.delete_order, name='delete_order'),
    path('admin_order_history/', views.admin_order_history, name='admin_order_history'),
    path('delete_order_history/<int:id>/', views.delete_order_history, name='delete_order_history'),
    path('manage_user_request',views.manage_user_request,name='manage_user_request'),
    path('delete_user_request/<int:id>',views.delete_user_request,name='delete_user_request'),
    # path('search_order_history',views.search_order_history,name='search_order_history'),
    # path('filter_order_history',views.filter_order_history,name='filter_order_history'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
