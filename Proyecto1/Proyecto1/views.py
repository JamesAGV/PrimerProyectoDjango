from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render
#<>

def renderizar(file_path, dictionary):
    file = open(file_path)
    plt = Template(file.read())
    file.close()
    ctx = Context(dictionary)
    document = plt.render(ctx)
    return document
class Persona(object):
    def __init__(self, nombres, apellidos, edad):
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad

def saludo(request): #primera vista
    nombre = 'James Andrés'
    apellido = 'García Vidal'
    apellido = 'García Vidal'
    edad = 32
    temas = ['PLantillas', 'Modelos', 'Formularios', 'Vistas', 'Despliegue']
    #personas = ['James', 'Yolima', 'Maria José', 'Josefa', 'Esteban']
    personas = None
    fecha_actual = datetime.datetime.now()
    esposa = Persona('Yolima Andrea', 'Castaño Zuluaga', 43)
    dictionary = {'nombre':nombre, 'apellido':apellido, 'edad':edad, 'estampa':fecha_actual, 'esposa':esposa, 'temas':temas, 'personas':personas}
    path = "/home/oem/PycharmProjects/PrimerProyectoDjango/Proyecto1/Proyecto1/templates/my_template.html"
    return HttpResponse(renderizar(file_path=path, dictionary=dictionary))

def saludo_2(request): #segunda vista
    nombre = 'James Andrés'
    apellido = 'García Vidal'
    apellido = 'García Vidal'
    edad = 32
    temas = ['PLantillas', 'Modelos', 'Formularios', 'Vistas', 'Despliegue']
    #personas = ['James', 'Yolima', 'Maria José', 'Josefa', 'Esteban']
    personas = None
    fecha_actual = datetime.datetime.now()
    esposa = Persona('Yolima Andrea', 'Castaño Zuluaga', 43)
    dictionary = {'nombre':nombre, 'apellido':apellido, 'edad':edad, 'estampa':fecha_actual, 'esposa':esposa, 'temas':temas, 'personas':personas}
    doc_externo = loader.get_template('my_template.html')
    documento = doc_externo.render(dictionary)
    return HttpResponse(documento)

def saludo_3(request): #segunda vista
    nombre = 'James Andrés'
    apellido = 'García Vidal'
    apellido = 'García Vidal'
    edad = 32
    temas = ['PLantillas', 'Modelos', 'Formularios', 'Vistas', 'Despliegue']
    #personas = ['James', 'Yolima', 'Maria José', 'Josefa', 'Esteban']
    personas = None
    fecha_actual = datetime.datetime.now()
    esposa = Persona('Yolima Andrea', 'Castaño Zuluaga', 43)
    dictionary = {'nombre':nombre, 'apellido':apellido, 'edad':edad, 'estampa':fecha_actual, 'esposa':esposa, 'temas':temas, 'personas':personas}

    return render(request, 'my_template.html', dictionary)


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

def dashboards(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "dashboards.html", {'fecha_actual':fecha_actual})