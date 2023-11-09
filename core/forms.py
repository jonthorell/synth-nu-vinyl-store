from allauth.account.forms import SignupForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext as _

class CustomSignupForm(SignupForm):
    '''Class used to alter some of the allauth fields '''
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'email2', 'password1', 'password2')
        
    field_order = ['username', 'first_name', 'last_name', 'email', 'email2', 'password1', 'password2']
        
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,)

    def __init__(self, *args, **kwargs):
       super(SignupForm, self).__init__(*args, **kwargs)
       self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': 'Enter first name'})
       self.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': 'Enter last name'})
       self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
       self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Password again'})

    def save(self, request):
        
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        return user