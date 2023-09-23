from django.http import HttpResponse
#<>
def saludo(request): #primera vista
    documento = "<html><body><h1>Hola Mundo, soy James García</h1></body></html>"
    return HttpResponse(documento)

def despedida(request): #segunda vista
    documento = "Página de despedida!!!"
    return HttpResponse(documento)

