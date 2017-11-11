from django import forms

from .models import Film
from .validators import validate_genre

class FilmadCreateForm(forms.Form):
    name            = forms.CharField()
    description     = forms.CharField(max_length=2000)
    poster          = forms.ImageField()
    genre           = forms.CharField(max_length=2000)
    premiere        = forms.DateField()
    sessiontime     = forms.DateTimeField()
    durability      = forms.IntegerField()
    price           = forms.IntegerField()
    
    

class FilmCreateForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = [
            'name',
            'description',
            'poster',
            'genre',
            'premiere',
            'sessiontime',
            'durability',
            'price',
            'slug',
        ]





