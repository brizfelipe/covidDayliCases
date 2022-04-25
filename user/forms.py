from django import forms
from tempus_dominus.widgets import DatePicker

class SubscriptionForms(forms.Form):
    fName = forms.CharField(label='FULL NAME:',max_length=20)
    email = forms.EmailField(label='E-MAIL')
    userName = forms.CharField(label='USER NAME:',max_length=20)
    passWord = forms.CharField(label='PASSWORD:',max_length=100,widget=forms.PasswordInput)
    repeatPassWord= forms.CharField(label='REPEAT PASSWORD:',max_length=100,widget=forms.PasswordInput)

class SingIn(forms.Form):
    user = forms.CharField(label='FULL NAME:',max_length=50)
    passWord = forms.CharField(label='PASSWORD:',max_length=100,widget=forms.PasswordInput)
    