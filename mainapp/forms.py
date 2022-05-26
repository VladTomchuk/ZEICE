from django import forms
from captcha.fields import CaptchaField
from django.utils.translation import ugettext_lazy as _


class MyForm(forms.Form):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Your name')}), required=True)
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Your email')}), required=True)
    phone = forms.CharField(label='', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': _('Your number')}), required=True)
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Message')}), required=True)
    captcha = CaptchaField(label='', )