"""

Forms for Newsletter App.
"""
from django import forms
from .models import subscription


class AddSubscriberForm(forms.ModelForm):
    """Form for adding email to newsletter subscribers"""

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "id": "newsletter_email",
            }
        ),
    )

    class Meta:
        """Meta class"""

        model = subscription
        fields = [
            "email",
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({"class": "form-control input-style"})
        self.fields["email"].widget.attrs.update(size="40")