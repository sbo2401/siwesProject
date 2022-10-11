from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(User_details)

from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class ContactForm(forms.ModelForm):
    class Meta:
        widgets = {
            "tel": PhoneNumberPrefixWidget(initial="NG"),
        }


@admin.register(User_detail)
class ContactAdmin(admin.ModelAdmin):
    form = ContactForm
