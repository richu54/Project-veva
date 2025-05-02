
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('admin_app.urls')),
    path('',include('user_app.urls')),
    path('',views.index),
    path('signup',views.signup,name='signup'),
    path('signup_otp',views.signup_otp,name='signup_otp'),
    path('home',views.home),
    path('login',views.login),
    path('logout',views.logout)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
