from allauth.account.forms import SignupForm
from django.contrib.auth.models import User, Group
from django import forms
from django.utils.translation import gettext as _

from .models import newsfeed

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
    password2 = forms.CharField(label=_("Password again"),
        widget=forms.PasswordInput,)

    def __init__(self, *args, **kwargs):
       super(SignupForm, self).__init__(*args, **kwargs)
       self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': 'Enter first name'})
       self.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': 'Enter last name'})
       self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
       self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Password again'})
       self.fields['email2'].widget = forms.TextInput(attrs={'placeholder': 'Email again'})

    def save(self, request):
        
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        # add new user to member group
        user_group = "members"
        g = Group.objects.get(name=user_group)
        user.groups.add(g)
        user.save()
        
        return user
    
class ContactForm(forms.Form):
    '''Class used to create contact form '''

    name = forms.CharField(
        required = False,
        widget = forms.widgets.TextInput(
            attrs={
                "placeholder": "Your name",
                "class": "form-control form-control-sm",
                "required": True,
                }
            ),
            label="Your name",
        )
    email = forms.EmailField(
        required = False,
        widget = forms.widgets.EmailInput(
            attrs={
                "placeholder": "Your e-mail",
                "class": "form-control form-control-sm",
                "required": True,
                }
            ),
            label="Your e-mail",
        )

    subject = forms.CharField(
        required=False,
        widget = forms.widgets.TextInput(
            attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Subject",
                "required": True,
                }
            ),
        label="Subject",
    )

    mess = forms.CharField(
        required=False,
        widget = forms.widgets.Textarea(
            attrs={
                 "placeholder": "Enter message here",
                "class": "form-control form-control-sm validate",
                "required": True,
                }
            ),
        label="What do you want to say to us?",
    )
    
class NewsForm(forms.ModelForm):
    '''Class used to create news form '''

    class Meta:
        model = newsfeed
        fields = '__all__'

    title = forms.CharField(
        required = False,
        widget = forms.widgets.TextInput(
            attrs={
                "placeholder": "Title",
                "class": "form-control form-control-sm",
                "required": True,
                }
            ),
            label="Title",
        )
    
    description = forms.CharField(
        required = False,
        widget = forms.widgets.TextInput(
            attrs={
                "placeholder": "Description",
                "class": "form-control form-control-sm",
                "required": True,
                }
            ),
            label="Description",
        )    

    