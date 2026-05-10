# accounts/urls.py

# IMPORT path
# This lets Django create website URL routes
from django.urls import path

# IMPORT views.py from current app
# The dot means:
# "look inside this same accounts folder"
from . import views


# URL PATTERNS
# This list connects browser URLs to Python functions in views.py

urlpatterns = [

    # HOMEPAGE ROUTE
    # When someone visits:
    # http://127.0.0.1:8000/
    # Django runs the homepage() function inside views.py
    path('', views.homepage, name='home'),


    # REGISTER PAGE
    # URL:
    # /register/
    # Opens user registration page
    path('register/', views.register, name='register'),


    # LOGIN PAGE
    # URL:
    # /login/
    # Opens member login page
    path('login/', views.my_login, name='login'),


    # DASHBOARD PAGE
    # URL:
    # /dashboard/
    # This will become the protected member area
    path('dashboard/', views.dashboard, name='dashboard'),


    # LOGOUT ROUTE
    # URL:
    # /logout/
    # Logs user out and redirects to homepage
    path('logout/', views.user_logout, name='user-logout'),

]