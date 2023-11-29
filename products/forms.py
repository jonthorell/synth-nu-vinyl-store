from django import forms
from .widgets import CustomClearableFileInput
from .models import product, genre


class ProductForm(forms.ModelForm):

    class Meta:
        model = product
        fields = '__all__'
        exclude = ('price_currency','slug',)
        
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    
    field_order = ['image','name', 'artist', 'description', 'genre', 'new_old', 'media_format', 'media_color','sku','price','stock','rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = genre.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in genres]

        self.fields['genre'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control input-style'
            
class GenreForm(forms.ModelForm):
    '''Class used to create new-genre form '''

    class Meta:
        model = genre
        fields = '__all__'

    name = forms.CharField(
        required = False,
        widget = forms.widgets.TextInput(
            attrs={
                "placeholder": "Short Name",
                "class": "form-control form-control-sm",
                "required": True,
                }
            ),
            label="Short Name",
        )
    
    friendly_name = forms.CharField(
        required = False,
        widget = forms.widgets.TextInput(
            attrs={
                "placeholder": "Friendly (long) Name",
                "class": "form-control form-control-sm",
                "required": True,
                }
            ),
            label="Friendly Name",
        )    

    description = forms.CharField(
        required = False,
        widget = forms.widgets.TextInput(
            attrs={
                "placeholder": "Description of the genre",
                "class": "form-control form-control-sm",
                "required": True,
                }
            ),
            label="Genre",
        )    