from django import forms
from .models import AssociacaoCollaborator, AssociacaoAnchor,AssociacaoAtivo

class ColaboradorForm(forms.ModelForm):

    class Meta:
        model = AssociacaoCollaborator
        fields = '__all__'

class AnchorForm(forms.ModelForm):

    class Meta:
        model = AssociacaoAnchor
        fields = '__all__'

class AtivoForm(forms.ModelForm):

    class Meta:
        model = AssociacaoAtivo
        fields = '__all__'