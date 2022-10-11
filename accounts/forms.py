from django import forms
from django.contrib.auth.models import User
from .models import *


class Register(forms.Form):
    first_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "Enter Your First Name"}),
    )

    last_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "Enter Your Last Name"}),
    )

    username = forms.CharField(
        max_length=9,
        widget=forms.TextInput(attrs={"placeholder": "Enter Your Matric Number"}),
    )

    email = forms.EmailField(
        max_length=255,
        widget=forms.EmailInput(attrs={"placeholder": "Enter Your E-mail Address"}),
    )

    password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter Your Password", "id": "password"}
        ),
    )

    password2 = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirm Your Password", "id": "password2"}
        ),
    )

    def clean(self):
        super(Register, self).clean()
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")

        if password != password2:
            self.errors[""] = self.error_class(["The two password fields must match"])

        elif password.islower():
            self.errors[""] = self.error_class(["Password must contain an uppercase"])

        elif password.isnumeric():
            self.errors[""] = self.error_class(["Password must contain an alphabet"])

        elif password.isalpha():
            self.errors[""] = self.error_class(["Password must contain a number"])

        elif len(password) < 8:
            self.errors[""] = self.error_class(["Password is too short"])

        elif len(username) != 9:
            self.errors[""] = self.error_class(["You have entered an invalid username"])

        else:
            pass

        try:
            if len(username) == 9:
                username = int(username)
        except ValueError:
            self.errors[""] = self.error_class(["You have entered an invalid username"])

        for instance in User.objects.all():
            if instance.username == str(username):
                self.errors[""] = self.error_class(["User already exist"])
            elif instance.email == email:
                self.errors[""] = self.error_class(["E-mail already in use"])
            else:
                pass

        return self.cleaned_data


class Signin(forms.Form):
    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "Enter Your Userame"}),
    )
    password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter Your Password", "id": "password"}
        ),
    )


class Userdetail(forms.ModelForm):
    class Meta:
        model = User_detail
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(
                attrs={"placeholder": "Enter Your First Name"}
            ),
            "last_name": forms.TextInput(attrs={"placeholder": "Enter Your Last Name"}),
            "other_name": forms.TextInput(attrs={"placeholder": "Enter Other Names"}),
            "email": forms.EmailInput(
                attrs={"placeholder": "Enter Your E-mail Address"}
            ),
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "gender": forms.RadioSelect(attrs={"type": "radio", "class": "gender"}),
            "tel": forms.TextInput(attrs={"placeholder": "Enter Your Phone Number"}),
            'username':forms.TextInput(attrs={'placeholder': 'Enter Your Username'}),
        }

    def clean(self):
        super(Userdetail, self).clean()
        tel = self.cleaned_data.get("tel")
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")

        for instance in User_detail.objects.all():
            if instance.username == username:
                self.errors[""] = self.error_class(["User already exist"])
            elif instance.email == email:
                self.errors[""] = self.error_class(["E-mail already in use"])
            elif instance.tel == tel:
                self.errors[""] = self.error_class(["Phone Number already exists"])

