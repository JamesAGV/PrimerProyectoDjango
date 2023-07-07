from django.http import HttpResponse
#<>
def saludo(request): #primera vista
    return HttpResponse("<html><body><h1>Hola Mundo, soy James García</h1></body></html>")

def despedida(request): #segunda vista
    return HttpResponse("Página de despedida!!!")

