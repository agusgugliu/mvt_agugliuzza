from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    fecha_nacimiento = forms.DateField(label="Fecha de Nacimiento", input_formats=["%d/%m/%Y"],
    email = forms.EmailField(label="Email"),
    numero_documento = forms.IntegerField(label="Numero Documento"),
    #widget es para poder agregar un tip para que el usuario sepa como ingresar la fecha
    widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))
