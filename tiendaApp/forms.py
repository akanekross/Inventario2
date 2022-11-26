from django import forms
from django.core import validators
from tiendaApp.models import Productos

class RegistroProducto(forms.Form):
    ESTADOS =[('activo','ACTIVO'),('inactivo','INACTIVO')]
    Nserie = forms.CharField()
    NomProducto= forms.CharField(validators=[ #aqui tengo un validator
        validators.MinLengthValidator(2),
        validators.MaxLengthValidator(30)
    ])
    Descripcion = forms.CharField()
    Cantidad = forms.CharField()
    Categoria = forms.CharField()
    estados = forms.CharField(widget=forms.Select(choices=ESTADOS))

    Nserie.widget.attrs['class']= 'form-control'
    NomProducto.widget.attrs['class']= 'form-control'
    Descripcion.widget.attrs['class']= 'form-control'
    Cantidad.widget.attrs['class']= 'form-control'
    Categoria.widget.attrs['class']= 'form-control'

class FormProducto(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'

    