from django import forms
from django.contrib.auth.forms import UserCreationForm  

# from captcha.fields import CaptchaField

class CustomRegisterForm(UserCreationForm):
    # captcha = CaptchaField()
    pass


class SignupCapthaForm(forms.Form):
    pass