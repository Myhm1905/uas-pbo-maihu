from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class FormKoordinat(ModelForm):
    class Meta:
        model = Koordinat
        fields = '__all__'

        widgets = {
            'nama_penyu' : forms.TextInput({'class':'form-control', 'placeholder':'penyu', 'required':'required'}),
            'alamat' : forms.TextInput({'class':'form-control', 'placeholder':'alamat', 'required':'required'}),
            'koordinat' : forms.TextInput({'class':'form-control', 'placeholder':'titik koordinat', 'required':'required'}),
        }

class FormKlasifikasi(ModelForm):
    class Meta:
        model = Klasifikasi
        fields = '__all__'

        widgets = {
            'nama_ilmiah' : forms.TextInput({'class':'form-control', 'placeholder':'nama ilmiah', 'required':'required'}),
            'nama_lokal' : forms.TextInput({'class':'form-control', 'placeholder':'nama lokal', 'required':'required'}),
            'spesies' : forms.TextInput({'class':'form-control', 'placeholder':'spesies', 'required':'required'}),
            'img' : forms.TextInput({'class':'form-control', 'placeholder':'images', 'required':'required'}),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']