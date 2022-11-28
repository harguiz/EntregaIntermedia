from django import forms

class formPersonales(forms.Form):
    nombre = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    mail = forms.EmailField()


class formPronosticos(forms.Form):
    campeon = forms.CharField(max_length=50)
    subcampeon = forms.CharField(max_length=50)
    goleador = forms.CharField(max_length=50)

class formApuestas(forms.Form):
    mediopago = forms.CharField(max_length=50)
    monto = forms.IntegerField()
