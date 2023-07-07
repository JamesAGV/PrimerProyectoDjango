from django.http import HttpResponse

def saludo(request): #primera vista
    return HttpResponse("Hola Mundo, soy James García")

def despedida(request): #segunda vista
    return HttpResponse("Página de despedida!!!")