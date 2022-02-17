from django import forms
from django.contrib.auth.models import User
from .models import FotoUser
from django.contrib.auth.forms import UserChangeForm
from django.forms.widgets import ClearableFileInput


#UserChangeForm
class EditProfileForm(forms.ModelForm):

    username = forms.CharField(required=True, label='username')
    first_name = forms.CharField(required=True, label='first_name', max_length=13)
    last_name = forms.CharField(required=True, label='last_name', max_length=13)
    email = forms.EmailField(required=True, label='Email')


    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name",)


class EditFotoProfileForm(forms.ModelForm):

    foto = forms.ImageField(widget=ClearableFileInput)

    class Meta:
        model = FotoUser
        exclude = ('usuario',)
        fields = '__all__'






