from django.shortcuts import render
from django.http import HttpResponse
from appformularios.models import *
from appformularios.forms import *

# Create your views here.
def inicio(request):
    return render(request, "appformularios/index.html")

#Aqui van las funciones para los clientes
def creacion_cliente(request):

    if request.method == "POST":
        formulario = ClienteFormulario(request.POST)    

        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            cliente = Cliente(nombre=data["nombre"], cedula=data["cedula"], email=data["email"], sector=data["sector"])

            cliente.save()

    formulario = ClienteFormulario()

    contexto = {"formulario": formulario}

    return render(request, "appformularios/clientes_formulario.html", contexto)

def buscar_cliente(request):
    
    return render(request, "appformularios/busqueda_clientes.html")


def resultado_busqueda_clientes(request):
    cedula = request.GET["cedula"]

    clientes = Cliente.objects.filter(cedula=cedula)
    return render(request, "appformularios/resultados_busqueda_clientes.html",{"clientes":clientes})


#Aqui van las funciones para los productos
def creacion_producto(request):

    if request.method == "POST":
        formulario = ProductoFormulario(request.POST)

        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            producto = Producto(id_producto=data["id_producto"], nombre_producto=data["nombre_producto"], descripcion=data["descripcion"])

            producto.save()

    formulario = ProductoFormulario()

    contexto = {"formulario": formulario}

    return render(request, "appformularios/productos_formulario.html", contexto)

def buscar_producto(request):
    
    return render(request, "appformularios/busqueda_productos.html")


def resultado_busqueda_productos(request):
    id_producto = request.GET["id_producto"]

    productos = Producto.objects.filter(id_producto=id_producto)
    return render(request, "appformularios/resultados_busqueda_productos.html",{"productos":productos})



#Aqui van las funciones para las sucursales
def creacion_sucursal(request):

    if request.method == "POST":
        formulario = SucursalFormulario(request.POST)

        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            sucursal = Sucursal(nombre_direccion=data["nombre_direccion"], direccion=data["direccion"], departamento=data["departamento"], pais=data["pais"], codigo_postal=data["codigo_postal"])

            sucursal.save()

    formulario = SucursalFormulario()

    contexto = {"formulario": formulario}

    return render(request, "appformularios/sucursales_formulario.html", contexto)


def buscar_sucursal(request):
    
    return render(request, "appformularios/busqueda_sucursales.html")


def resultado_busqueda_sucursales(request):
    nombre_direccion = request.GET["nombre_direccion"]

    sucursales = Sucursal.objects.filter(nombre_direccion=nombre_direccion)
    return render(request, "appformularios/resultados_busqueda_sucursales.html",{"sucursales":sucursales})


