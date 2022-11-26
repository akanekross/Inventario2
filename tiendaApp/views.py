from django.shortcuts import render

# Create your views here.
from tiendaApp.models import Productos
from . import forms
from tiendaApp.forms import FormProducto
from django.shortcuts import redirect


# Create your views here.
def producto(request):
    #producto = Productos(nombre="Pepsi")
    #producto.save()
   
    producto1 = Productos.objects.all()
    
    data = {'producto1':producto1}

    return render(request, 'tiendaApp/productos.html',data)

def RegistrationProducto(request):
     
     form = FormProducto()
     if request.method == 'POST' :
        form = FormProducto(request.POST)
        if form.is_valid() :
            form.save()
        return producto(request)
     data = {'form':form}
     return render(request,'tiendaApp/RegistrarProducto.html',data)
 
    
def eliminar(request,id):
    Productos2 = Productos.objects.get(id = id)
    Productos2.delete()
    return redirect('/producto')
    #return redirect('/producto')

def actualizar(request,id):
    Producto = Productos.objects.get(id=id)
    form = FormProducto(instance=Producto)
    if request.method == 'POST':
        form = FormProducto(request.POST, instance=Producto)
        if form.is_valid():
            form.save()
        return producto(request)

    data ={'form':form}
    return render(request, 'tiendaApp/RegistrarProducto.html',data)


def index(request):
    return render(request,'tiendaApp/index.html')



