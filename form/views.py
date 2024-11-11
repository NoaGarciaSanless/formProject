from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "form/home.html")


def mostrar(request):
    opcion = request.GET.get('role')
    
    preferencias = request.GET.getlist('preferencias')
    
    response_text = f"Boton de radio seleccionado: {opcion}<br>"
    response_text += "Preferencias seleccionadas: " + ", ".join(preferencias)
    
    return HttpResponse(response_text)