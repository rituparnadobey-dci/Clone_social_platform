from django import forms
<<<<<<< HEAD
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MainPost


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    def __init__(self, *args, **kwargs):
        self.is_update = kwargs.pop('is_update', False)  # Check if it's for update
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        if self.is_update:
            del self.fields['password1']
            del self.fields['password2']
        else:
=======
from .models import MainPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MainPostForm(forms.ModelForm):
    body = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder": "Enter your Public Post!",
                                                                               "class": "form-control",}), label="")
    class Meta:
        model = MainPost
        exclude = ("user",)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Adress'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2") 

        def __init__(self, *args, **kwargs) -> None:
            super(SignUpForm, self).__init__(*args, **kwargs)

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'User Name'
            self.fields['username'].label = ''
            self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

>>>>>>> fd877cdb32189e5b3d46a56dddb8269e45b7384e
            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password1'].label = ''
            self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
            self.fields['password2'].label = ''
            self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
<<<<<<< HEAD

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if self.is_update and not password1:
            return None
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords must match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        if not self.is_update:
            user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

        

class MainPostForm(forms.ModelForm):
    body = forms.CharField(required=True, widget=forms.Textarea(attrs={"placeholder": "Enter your Public Post!", "class": "form-control"}), label="")

    class Meta:
        model = MainPost
        exclude = ("user",)


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
=======
>>>>>>> fd877cdb32189e5b3d46a56dddb8269e45b7384e
