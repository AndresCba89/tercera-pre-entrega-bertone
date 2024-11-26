from django import forms

class Usuario_Form(forms.Form):
    nombre = forms.CharField()
    dni = forms.IntegerField()
    
class Paciente_Form(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class Derivante_Form(forms.Form):
    institucion = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)

class Analsis_Form(forms.Form):
   nombre = forms.CharField(max_length=40)
   