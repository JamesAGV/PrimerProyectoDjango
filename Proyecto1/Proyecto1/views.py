from django.http import HttpResponse
import datetime
#<>
def saludo(request): #primera vista
    documento = """
    <html>
        <body>
            <h1>Hola Mundo, soy James García Vidal</h1>
        </body>
    </html>
    """
    return HttpResponse(documento)

def despedida(request): #segunda vista
    documento = "Página de despedida!!!"
    return HttpResponse(documento)

def obtenerFecha(request): #tercera vista

    fecha_actual = datetime.datetime.now()

    documento = f"""
    <html>
        <body>
            <h2>Fecha y hora actual: {fecha_actual}</h2>
        </body>
    </html>
    """
    return HttpResponse(documento)

def calcularEdad(request, year, edadActual): #tercera vista

    #edadActual = 18
    periodo = year - 2023
    edadFutura = edadActual + periodo
    documento = f"""
    <html>
        <body>
            <h2>En el año {year} tendrás {edadFutura} años</h2>
        </body>
    </html>
    """

    return HttpResponse(documento)