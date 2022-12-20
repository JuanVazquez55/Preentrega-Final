from django.urls import path 
from appformularios.views import *

urlpatterns = [
    path('inicio/',inicio, name="entrega-inicio"),
    path('clientes/crear/', creacion_cliente, name="entrega-clientes-crear"),
    path('clientes/buscar/', buscar_cliente , name="entrega-clientes-buscar"),
    path('clientes/buscar/resultados/', resultado_busqueda_clientes , name="entrega-clientes-buscar-resultados"),
    path('productos/crear/', creacion_producto, name="entrega-productos-crear"),
    path('productos/buscar/', buscar_producto , name="entrega-productos-buscar"),
    path('productos/buscar/resultados/', resultado_busqueda_productos , name="entrega-productos-buscar-resultados"),
    path('sucursales/crear/', creacion_sucursal, name="entrega-sucursales-crear"),
    path('sucursales/buscar/', buscar_sucursal , name="entrega-sucursales-buscar"),
    path('sucursales/buscar/resultados/', resultado_busqueda_sucursales , name="entrega-sucursales-buscar-resultados"),
    
    
]