from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, TextInput, Select
from django.utils import timezone


# Create your models here.

class Unvetted(models.Model):
    token_address = models.CharField(max_length=120)
    telegram_url = models.CharField(max_length=120)
    image = models.ImageField(upload_to='media')
    #proof_of_payment = models.CharField(max_length=200, blank=True, default=None)
    pub_date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.token_address


class Banner(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    link = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    company_name = models.CharField(max_length=100)
    interest = models.CharField(max_length=200)
    budget = models.CharField(max_length=100)
    proof_of_payment = models.CharField(max_length=100)
    about_project = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
