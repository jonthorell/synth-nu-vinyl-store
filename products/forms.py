from django import forms
from .widgets import CustomClearableFileInput
from .models import product, genre


class ProductForm(forms.ModelForm):

    class Meta:
        model = product
        fields = '__all__'
        
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = genre.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in genres]

        self.fields['genre'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control input-style'