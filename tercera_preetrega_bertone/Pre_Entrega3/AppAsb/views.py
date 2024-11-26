from django.shortcuts import render
from AppAsb.models import Usuario, Derivante, Paciente, Analisis
from AppAsb.forms import Usuario_Form, Paciente_Form, Derivante_Form, Analsis_Form
from django.http import HttpResponse

# Create your views here.

def inicio(req):
    return render(req, 'appasb/index.html')

def usuario(req):
     return render(req, 'appasb/usuario.html')

def paciente(req):
    return render(req, 'appasb/paciente.html')

def derivante(req):
    return render(req, 'appasb/derivante.html')

def analisis(req):
    return render(req, 'appasb/analisis.html')

def busquedausuario(request):
      return render(request, "appasb/busquedaUsuario.html")

def ususario_form(request):
    if request.method == "POST":
        miFormulario = Usuario_Form(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                usuario = Usuario(nombre=informacion["nombre"], dni=informacion["dni"])
                usuario.save()
                return render(request, "appasb/usuario.html")
    else:
        miFormulario =Usuario_Form()

    return render(request, "appasb/us_form.html", {"miFormulario": miFormulario})

def paciente_form(request):
    if request.method == "POST":
        miFormulario = Paciente_Form(request.POST)  
        print(miFormulario)

        if miFormulario.is_valid():  
            informacion = miFormulario.cleaned_data 
            paciente = Paciente(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"]) 
            paciente.save()  
            return render(request, "appasb/paciente.html") 
    else:
        miFormulario =Paciente_Form() 

    return render(request, "appasb/pte_form.html", {"miFormulario": miFormulario})


def derivante_form(request):
    if request.method == "POST":
        miFormulario = Derivante_Form(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                derivante = Derivante(institucion=informacion["institucion"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"])
                derivante.save()
                return render(request, "appasb/derivante.html")
    else:
        miFormulario =Derivante_Form()

    return render(request, "appasb/dev_form.html", {"miFormulario": miFormulario})


def analisis_form(request):
    if request.method == "POST":
        miFormulario = Analsis_Form(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                analisis = Analisis(nombre=informacion["nombre"])
                analisis.save()
                return render(request, "appasb/analisis.html")
    else:
        miFormulario =Analsis_Form()

    return render(request, "appasb/an_form.html", {"miFormulario": miFormulario})


def buscar(request):

    if request.GET["dni"]:

        respuesta = f"Estoy buscando el dni nro: {request.GET['dni']}"
        dni = request.GET['dni']

        nombre = Usuario.objects.filter(dni__icontains=dni)

        return render(request, "appasb/resultadobusqus.html", {"nombre": nombre, "dni": dni})

    else:

        respuesta = "No enviaste datos"

   
    return HttpResponse(respuesta)





