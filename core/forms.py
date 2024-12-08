from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente

class RegistroClienteForm(UserCreationForm):
    nombre_empresa = forms.CharField(max_length=255, required=True, label='Nombre de la Empresa')
    rut_empresa = forms.CharField(max_length=255, required=True, label='Rut de la Empresa')
    direccion = forms.CharField(max_length=255, required=True, label='Dirección')
    telefono_contacto = forms.CharField(max_length=20, required=True, label='Teléfono de Contacto')

    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']

    def save(self, commit=True):
        # Guardamos el usuario primero
        user = super().save(commit=commit)
        # Creamos el cliente asociado
        Cliente.objects.create(
            usuario=user,
            nombre_empresa=self.cleaned_data['nombre_empresa'],
            rut_empresa=self.cleaned_data['rut_empresa'],
            direccion=self.cleaned_data['direccion'],
            telefono_contacto=self.cleaned_data['telefono_contacto'],
        )
        
        return user