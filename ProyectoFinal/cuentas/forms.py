from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioRegistroUsuario(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class EditarPerfilForm(forms.ModelForm):
    nombre = forms.CharField(max_length=30, initial='')
    apellido = forms.CharField(max_length=30, initial='')
    avatar = forms.ImageField(required=False)
    biografia = forms.CharField(widget=forms.Textarea, required=False)
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = Perfil
        fields = ['nombre', 'apellido', 'avatar', 'biografia', 'fecha_nacimiento']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['nombre'].initial = user.first_name
        self.fields['apellido'].initial = user.last_name

    def save(self, commit=True):
        perfil = super().save(commit=False)
        perfil.usuario.first_name = self.cleaned_data['nombre']
        perfil.usuario.last_name = self.cleaned_data['apellido']
        if commit:
            perfil.usuario.save()
            perfil.save()
        return perfil
