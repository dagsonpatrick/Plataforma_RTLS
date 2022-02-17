from django import forms
from .models import Regra

class RegraForm(forms.ModelForm):

    class Meta:
        model = Regra
        fields = '__all__'