from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "form/home.html")


def mostrar(request):
    name = request.GET.get('name')
    city = request.GET.get('city')
    server = request.GET.get('server')
    role = request.GET.get('role')
    
    mail = request.GET.get('Mail')
    payroll = request.GET.get('Payroll')
    selfService = request.GET.get('selfService')
    
    data= {
        "Name" : name,
        "City" : city,
        "Server" : server,
        "Role" : role,
        "Mail" : mail,
        "Payroll" : payroll,
        "SelfService" : selfService,   
    }
    
    return render(request, "form/result.html", {"data" :data})