# accounts/forms.py


# IMPORT DJANGO'S BUILT-IN LOGIN FORM SYSTEM
# AuthenticationForm already knows how to:
# - validate usernames/passwords
# - check users against the database
# - handle authentication safely
from django.contrib.auth.forms import AuthenticationForm


# IMPORT DJANGO FORMS SYSTEM
# Gives access to form fields like CharField
from django import forms


# IMPORT INPUT WIDGETS
# These control how the form fields appear in HTML
from django.forms.widgets import PasswordInput, TextInput



# CUSTOM LOGIN FORM
# This class inherits from Django's built-in AuthenticationForm
# We are customizing the appearance of the username/password inputs
class LoginForm(AuthenticationForm):


    # USERNAME FIELD
    # TextInput creates a standard text box
    username = forms.CharField(
        widget=TextInput()
    )


    # PASSWORD FIELD
    # PasswordInput hides typed characters for security
    password = forms.CharField(
        widget=PasswordInput()
    )

# CUSTOM REGISTRATION FORM


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):


    # CUSTOM USERNAME FIELD
    # Limits username to 40 characters
    # Allows letters and numbers only
    username = forms.CharField(
        max_length=40,
        help_text='40 characters or fewer. Letters and numbers only.'
    )


    # FORM SETTINGS
    class Meta:

        # USE DJANGO USER MODEL
        model = User


        # FIELDS TO DISPLAY
        fields = [
            'username',
            'password1',
            'password2'
        ]