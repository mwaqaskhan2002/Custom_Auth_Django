from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import MyPasswordResetView, MyPasswordResetConfirmView, MyLoginView, HomeView, SignUpView


urlpatterns = [
    path("admin/", admin.site.urls),
    #Home 
    path('', HomeView.as_view(), name='home'),
    
    #SignUp
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    # Password Reset
    path('accounts/password_reset/', MyPasswordResetView.as_view(), name='password_reset'),
    path('accounts/reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), 
         name='password_reset_confirm'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # Authentication
    path('accounts/', include('django.contrib.auth.urls')),
    
    #
    
]
