from django import forms
from django.contrib.auth.models import User

class Register(forms.Form):
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'Enter Your First Name'}))

    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'Enter Your Last Name'}))

    username = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'placeholder':'Enter Your Matric Number or Staff Id'}))

    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={'placeholder':'Enter Your E-mail Address'}))

    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'placeholder':'Enter Your Password'}))

    password2 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'placeholder':'Confirm Your Password'}))

    def clean(self):
        super(Register, self).clean()
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        
        if password.islower():
            self.errors[''] = self.error_class(["Password must contain an uppercase"])
        
        elif password.isnumeric():
            self.errors[''] = self.error_class(["Password must contain an alphabet"])

        elif password.isalpha():
            self.errors[''] = self.error_class(["Password must contain a number"])

        elif len(password) < 8:
            self.errors[''] = self.error_class(["Password is too short"])

        elif password != password2:
            self.errors[''] = self.error_class(["The two password fields must match"])

        elif len(username) !=7  and len(username) != 9:
            self.errors[''] = self.error_class(["You have entered an invalid username"])

        else:
            pass
        
        try:
            if len(username) == 9:
                username = int(username)
        except ValueError:
            self.errors[''] = self.error_class(["You have entered an invalid username"])

        if not (len(username) == 7 and username.isalnum()):
            self.errors[''] = self.error_class(["Youuuu have entered an invalid username"])
        else:
            username = str(username)

        for instance in User.objects.all():
            if instance.username == username:
                self.errors[''] = self.error_class(["User already exist"])
            elif instance.email == email:
                self.errors[''] = self.error_class(["E-mail already in use"])
            else:
                pass

        return self.cleaned_data

class Signin(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'Enter Your Userame'}))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'placeholder':'Enter Your Password'}))