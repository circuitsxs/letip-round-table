# accounts/views.py
from .models import Announcement

# IMPORT render
# Used to load and display HTML templates

# IMPORT redirect
# Used to send users to another page after actions
from django.shortcuts import render, redirect


# IMPORT DJANGO'S BUILT-IN USER REGISTRATION FORM
# UserCreationForm already handles:
# - username creation
# - password validation
# - password confirmation
from django.contrib.auth.forms import UserCreationForm


# IMPORT DJANGO AUTHENTICATION SYSTEM
# Handles:
# - login
# - logout
# - sessions
from django.contrib import auth


# created a custom form 5/10/26
from .forms import LoginForm, CreateUserForm



# HOMEPAGE VIEW
# This function loads the homepage template
# URL:
# http://127.0.0.1:8000/
def homepage(request):

    return render(request, 'accounts/index.html')



# REGISTER VIEW
# Handles creating new users/accounts
# URL:
# /register/
def register(request):


    # CREATE EMPTY REGISTRATION FORM
    registerForm = CreateUserForm()


    # CHECK IF USER SUBMITTED THE FORM
    if request.method == 'POST':


        # FILL FORM WITH USER DATA
        registerForm = CreateUserForm(request.POST)


        # VALIDATE FORM
        # Checks:
        # - username availability
        # - password strength
        # - password match
        if registerForm.is_valid():


            # SAVE USER INTO DATABASE
            registerForm.save()


            # REDIRECT USER TO HOMEPAGE
            return redirect('home')


    # SEND FORM TO HTML TEMPLATE
    context = {
        'registerForm': registerForm
    }


    # LOAD register.html
    return render(request, 'accounts/register.html', context)



# LOGIN VIEW
# Handles user login/authentication
# URL:
# /login/
def my_login(request):


    # CREATE EMPTY LOGIN FORM
    form = LoginForm()


    # CHECK IF LOGIN FORM WAS SUBMITTED
    if request.method == 'POST':


        # LOAD USER INPUT INTO FORM
        form = LoginForm(request, data=request.POST)


        # VALIDATE USERNAME/PASSWORD
        if form.is_valid():


            # LOG USER INTO SESSION
            # form.get_user() returns authenticated user
            auth.login(request, form.get_user())


            # REDIRECT TO DASHBOARD
            return redirect('dashboard')


    # SEND LOGIN FORM TO TEMPLATE
    context = {
        'loginForm': form
    }


    # LOAD my-login.html
    return render(request, 'accounts/my-login.html', context)



# DASHBOARD VIEW
# Protected member area
# URL:
# /dashboard/

# MEMBER DASHBOARD VIEW
# LOADS ANNOUNCEMENTS FROM DATABASE
# AND SENDS THEM TO dashboard.html


def dashboard(request):

    # GET ALL ANNOUNCEMENTS
    # ORDER NEWEST POSTS FIRST
    announcements = Announcement.objects.order_by('-date_posted')[:3]

    # STORE DATABASE DATA INSIDE CONTEXT DICTIONARY
    # SO IT CAN BE ACCESSED IN HTML TEMPLATE
    context = {
        'announcements': announcements
    }

    # RENDER DASHBOARD PAGE
    # AND PASS ANNOUNCEMENT DATA INTO IT
    return render(request, 'accounts/dashboard.html', context)


# LOGOUT VIEW
# Logs user out and destroys session
# URL:
# /logout/
def user_logout(request):


    # REMOVE USER SESSION
    auth.logout(request)


    # SEND USER BACK TO HOMEPAGE
    return redirect('home')