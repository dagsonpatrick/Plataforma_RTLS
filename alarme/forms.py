from django import forms
from .models import Alarme

class AlarmeForm(forms.ModelForm):

    class Meta:
        model = Alarme
        fields = '__all__'