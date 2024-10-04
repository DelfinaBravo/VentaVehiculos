from django.shortcuts import render,get_object_or_404,redirect
#---->Importamos el Sector de Formularios
from .forms import *
from .models import *
from django.contrib import messages  # Importa el sistema de mensajes
#--->Importamos la Libreria de Logout
from django.contrib.auth import logout
#--->Importamos la Libreria de Permisos
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def Home(request):
    buscar=Vehiculos.objects.all().order_by('-Codigo')[:6]
    data={
        'forms':buscar
    }
    return render (request,'index.html',data)


@login_required

@permission_required('App.add_autos')
def Agregar(request):
    data={
        'forms':NuevoVehiculos()
    }
    if request.method=='POST':
        query=NuevoVehiculos(data=request.POST,files=request.FILES)
        if  query.is_valid():
            query.save()
            data['mensaje']="Datos Registrados"
        else:
            data['forms']=NuevoVehiculos
    return render (request,'Pages/agregar.html',data)

def ver_Vehiculos(request):
    #--->TREAMOS TODOS LOS ELEMENTOS DEL TABLA
    buscar=Vehiculos.objects.all()
    data={
        'forms':buscar
    }
    return render(request,'Pages/visualizar.html',data)

# boton modificar. 
@permission_required('App.change_Vehiculos')

def Modificar_Vehiculos(request,Codigo):
    sql=get_object_or_404(Vehiculos,Codigo=Codigo)
    data={
        'forms':NuevoVehiculos(instance=sql)
    }
    if request.method=='POST':
        query=NuevoVehiculos(data=request.POST,instance=sql,files=request.FILES)
        if  query.is_valid():
            query.save()
            data['mensaje']="Datos Modificados Correctamente "
        else:
            data['forms']=NuevoVehiculos
    return render (request,'Pages/modificar.html',data)

# boton eliminar
@permission_required('App.delete_Vehiculos')

def Eliminar_Vehiculos(request,Codigo):
    buscar=get_object_or_404(Vehiculos,Codigo=Codigo)
    buscar.delete()
    return redirect(to="visualizar")

def salir(request):
    logout(request)
    return redirect(to='inicio')

def detalle_vehiculo(request, Codigo):
    vehiculo = get_object_or_404(Vehiculos, Codigo=Codigo)
    message = None  # Inicializar mensaje como None

    if request.method == 'POST':
        if vehiculo.Cantidad > 0:
            vehiculo.Cantidad -= 1
            vehiculo.save()
            message = "Compra exitosa!"  # Mensaje de éxito

    return render(request, 'pages/detalle_vehiculo.html', {'vehiculo': vehiculo, 'message': message})
