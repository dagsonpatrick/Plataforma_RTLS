from django import forms
from .models import Mio

class MioForm(forms.ModelForm):

    class Meta:
        model = Mio
        fields = '__all__'