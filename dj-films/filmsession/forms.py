from django import forms

from films.models import Film

from .models import Session

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = [
            'film',
            'public'
        ]
    def __init__(self, user=None, *args, **kwargs):
        super(SessionForm, self).__init__(*args,**kwargs)
        self.fields['film'].queryset = Film.objects.filter(owner=user)