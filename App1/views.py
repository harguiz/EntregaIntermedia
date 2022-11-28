from django.shortcuts import render
from django.http import HttpResponse
from App1.forms import *
from App1.models import *
# Create your views here.

def inicio(request):

    return render(request, "AppTemplate/iniciopadre.html")

def form1(request):

    if request.method == "POST":
        form = formPersonales(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre1 = info["nombre"]
            edad1 = info["edad"]
            mail1 = info["mail"] 
            persona1 = Personales (nombre = nombre1, edad=edad1, mail = mail1)
            persona1.save()
            return render (request, "AppTemplate/iniciopadre.html")
    else:
        formPerson = formPersonales()

    return render(request, "AppTemplate/form1.html", {"form": formPerson})

def form2(request):

    if request.method == "POST":
        form = formPronosticos(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            campeon1 = info["campeon"]
            subcampeon1 = info["subcampeon"]
            goleador1 = info["goleador"] 
            pronostico1 = Pronosticos (campeon = campeon1, subcampeon=subcampeon1, goleador = goleador1)
            pronostico1.save()
            return render (request, "AppTemplate/iniciopadre.html")
    else:
        formPronos = formPronosticos()

    return render(request, "AppTemplate/form2.html", {"form": formPronos})

def form3(request):

    if request.method == "POST":
        form = formApuestas(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            mdp1 = info["mediopago"]
            monto1 = info["monto"]
            apuesta1 = Apuestas (mediopago = mdp1, monto=monto1)
            apuesta1.save()
            return render (request, "AppTemplate/iniciopadre.html")
    else:
        formApues = formApuestas()

    return render(request, "AppTemplate/form3.html", {"form": formApues})

def busquedaPronostico(request):

    return render (request, "AppTemplate/busqueda.html")

def respuestaPronostico(request):

    if request.GET["busquedapronostico"]:
        varpronos = request.GET["busquedapronostico"]
        objpronos = Pronosticos.objects.filter(campeon = varpronos) #coincidencia total
        return render (request, "AppTemplate/respuesta.html", {"Pronostico": objpronos})
    else:
        return render (request, "AppTemplate/busqueda.html", {"Mensaje" : "Ingresar Carga"})