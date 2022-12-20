from django import forms

#Aqui creo los formularios a utilizar

class ClienteFormulario(forms.Form):
    nombre = forms.CharField()
    cedula = forms.CharField()
    email = forms.EmailField()
    sector = forms.CharField()

class ProductoFormulario(forms.Form):
    id_producto = forms.CharField()
    nombre_producto = forms.CharField()
    descripcion = forms.CharField()
    

class SucursalFormulario(forms.Form):
    nombre_direccion = forms.CharField()
    direccion = forms.CharField()
    departamento = forms.CharField()
    pais = forms.CharField()
    codigo_postal = forms.IntegerField()