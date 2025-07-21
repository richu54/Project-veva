
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('admin_app.urls')),
    path('',include('user_app.urls')),
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('signup_otp',views.signup_otp,name='signup_otp'),
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('logout',views.logout),
    path('reset_pass_step1',views.reset_pass_step1,name='reset_pass_step1'),
    path('reset_pass_step2',views.reset_pass_step2,name='reset_pass_step2'),
    path('reset_pass_step3',views.reset_pass_step3,name='reset_pass_step3'),
    path('contact',views.contact,name='contact'),
    path('terms_and_condition',views.terms_and_condition,name='terms_and_condition'),
    path('privacy_and_policy',views.privacy_and_policy,name='privacy_and_policy'),
    path('faq',views.faq,name='faq'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
