from django import forms
from django.forms.widgets import DateInput, TextInput

from .models import *

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput
from .models import *


class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)

        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label= 'User Name :')
    email = forms.EmailField(max_length=200, label= 'Email :')
    first_name = forms.CharField(max_length=100, help_text='First Name', label= 'First Name :')
    last_name = forms.CharField(max_length=100, help_text='Last Name', label= 'Last Name :')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')




class UnvettedForm(forms.ModelForm):
    token_address = models.CharField(max_length=120)
    telegram_url = models.CharField(max_length=120)
    #proof_of_payment = models.CharField(max_length=200)
    image = models.ImageField()


    class Meta():
        model = Unvetted
        fields = ("token_address", "telegram_url", "image")

class VerifyVettedForm(forms.ModelForm):
    status = models.BooleanField(default=False)
    class Meta():
        model = Unvetted
        fields = ["status"]


class BannerForm(forms.ModelForm):
    title = models.CharField(max_length=120)
    text = models.CharField(max_length=120)
    link = models.CharField(max_length=120)
    company_name = models.CharField(max_length=120)
    image = models.ImageField()

    interest = models.CharField(max_length=200)
    budget = models.CharField(max_length=100)
    proof_of_payment = models.CharField(max_length=100)
    about_project = models.TextField()


    class Meta():
        model = Banner
        fields = ("title", "text", "link", "company_name", "image", "interest", "budget", "proof_of_payment", "about_project")


class VerifyBannerForm(forms.ModelForm):
    status = models.BooleanField(default=False)
    class Meta():
        model = Banner
        fields = ["status"]



