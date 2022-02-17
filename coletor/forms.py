from django import forms
from .models import Coletor

class ColetorForm(forms.ModelForm):

    class Meta:
        model = Coletor
        fields = '__all__'