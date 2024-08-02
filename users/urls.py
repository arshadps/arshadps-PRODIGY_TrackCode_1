# users/urls.py

from django.urls import path
from .views import signup_view, login_view, home_view
from django.contrib.auth.views import LogoutView
from .views import logout_view, login_view

urlpatterns = [
    path('admin/', login_view, name='admin'),
    path('signup/', signup_view, name='signup'),
    path('login/', views.login, name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('home/', home_view, name='home'),
    path('accounts/logout/', logout_view, name='logout'),  # Map to the custom logout view
    path('accounts/login/', login_view, name='login'), 
    path('accounts/logout/', LogoutView.as_view(), name='logout'),  # Use the built-in view
    path('accounts/login/', login_view, name='login'), 
]
