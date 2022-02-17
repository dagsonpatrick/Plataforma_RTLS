from django import forms
from django.forms.widgets import ClearableFileInput
from .models import Plano


class PlanoModelForm(forms.ModelForm):

    foto = forms.ImageField(widget=ClearableFileInput)

    class Meta:
        model = Plano
        fields = '__all__'
        widgets ={
            'nome': forms.TextInput(attrs ={
                'class': 'form-control',
                'maxlength': 35,
                'placeholder': 'Digite o nome do plano'
            }),
            'descricao': forms.TextInput(attrs ={
                'class': 'form-control',
                'maxlength': 50,
                'placeholder': 'Digite a descrição do plano'
            })
        }

        error_messages ={
            'nome':{
                'required': 'O campo nome é obrigatório'
            },
            'descricao':{
                'required': 'O campo descrição é obrigatório'
            }
        }
