from django import forms
from .models import MainPost


class MainPostForm(forms.ModelForm):
    body = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder": "Enter your Public Post!",
                                                                               "class": "form-control",}), label="")
    class Meta:
        model = MainPost
        exclude = ("user",)
