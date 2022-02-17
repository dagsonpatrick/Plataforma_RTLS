from django import forms
from .models import Anchor

class AnchorForm(forms.ModelForm):

    class Meta:
        model = Anchor
        fields = '__all__'