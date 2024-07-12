from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Inmueble, Region, Comuna, TipoInmueble, Contacto, Solicitud, Usuario, TipoUsuario
from .forms import ContactoForm, SolicitudForm
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import generic
from .services import crear_inmueble, editar_inmueble, eliminar_inmueble



# Create your views here.
def indexView(request):
    tipos_inmuebles = TipoInmueble.objects.all()
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    
    contexto = {'tipos_inmuebles':tipos_inmuebles,
                'regiones':regiones,
                'comunas':comunas}
    return render(request, 'index.html', contexto)

class InmueblesListView(generic.ListView):
    model = Inmueble
    context_object_name = 'lista_inmuebles'   # su propio nombre para la lista como variable de plantilla
    template_name = 'arrendador.html'  # Especifique su propio nombre/ubicación de plantilla
    paginate_by = 10

def ver_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, pk=id)
    
    return render(request, 'ver_inmueble.html', {'inmueble':inmueble})

def editar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, pk=id)
    tipos_inmuebles = TipoInmueble.objects.all()
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    tipo_arrendador = TipoUsuario.objects.get(pk=1)
    arrendadores = Usuario.objects.filter(tipo_usuario = tipo_arrendador)
    contexto = {'tipos_inmuebles':tipos_inmuebles,
                'regiones':regiones,
                'comunas':comunas,
                'arrendadores':arrendadores,
                'inmueble':inmueble}
    if request.method =="POST":
        nombre = (request.POST["nombre"])
        descripcion = (request.POST["descripcion"])
        m2_construidos = (request.POST["m2_construidos"])
        m2_terreno = (request.POST["m2_terreno"])
        estacionamientos = (request.POST["estacionamientos"])
        habitaciones = (request.POST["habitaciones"])
        banios = (request.POST["banios"])
        direccion = (request.POST["direccion"])
        comuna = (request.POST["comunas"])
        region = (request.POST["regiones"])
        tipo = (request.POST["tipo_inmueble"])
        precio = (request.POST["precio_mensual"])
        usuarios = (request.POST["usuarios"])
        
        editar_inmueble(inmueble.id, nombre,descripcion,m2_construidos,m2_terreno,estacionamientos,habitaciones, banios, direccion, comuna, region, tipo, precio, usuarios )

    
    return render(request, 'editar_inmueble.html', contexto)

def eliminar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, pk=id)
    
    eliminar_inmueble(inmueble.id)
    


@login_required
def crear_inmueble(request):
    tipos_inmuebles = TipoInmueble.objects.all()
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    tipo_usuario = TipoUsuario.objects.get(pk=1)
    arrendadores = Usuario.objects.filter(tipo_usuario = tipo_usuario)
    contexto = {'tipos_inmuebles':tipos_inmuebles,
                'regiones':regiones,
                'comunas':comunas,
                'arrendadores':arrendadores}
    if request.method =="POST":
        nombre = (request.POST["nombre"])
        descripcion = (request.POST["descripcion"])
        m2_construidos = (request.POST["m2_construidos"])
        m2_terreno = (request.POST["m2_terreno"])
        estacionamientos = (request.POST["estacionamientos"])
        habitaciones = (request.POST["habitaciones"])
        banios = (request.POST["banios"])
        direccion = (request.POST["direccion"])
        comuna = (request.POST["comunas"])
        region = (request.POST["regiones"])
        tipo = (request.POST["tipo_inmueble"])
        precio = (request.POST["precio_mensual"])
        usuarios = (request.POST["usuarios"])

        crear_inmueble(nombre,descripcion,m2_construidos,m2_terreno,estacionamientos,habitaciones, banios, direccion, comuna, region, tipo, precio, usuarios )
        
    return render(request, 'crear_inmueble.html', contexto)

def filtrar_comunas(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            regionId = data.get('regionId')
            #print('**** region id ****',regionId)
            dataBD = list(Comuna.objects.filter(
                region=regionId).values()
                )
            #print('**** dataBD ****',dataBD)
            return JsonResponse({'status': 200, 'data': dataBD})
        else:
            return JsonResponse({'error': 'Método no permitido'}, status=405)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
def buscar_inmuebles(request):
    if request.method == "POST":
        inmuebles = Inmueble.objects.filter(arrendada = False)
        
        tipo_inmueble = request.POST['tipos_inmuebles']
        if tipo_inmueble != '0':
            tipo = TipoInmueble.objects.get(pk = tipo_inmueble)
            inmuebles = inmuebles.filter(tipo_inmueble=tipo)
            print(inmuebles)
        region = request.POST['regiones']
        if region != '0':
            obj_region = Region.objects.get(pk = region)
            inmuebles = inmuebles.filter(region=obj_region)
            
        comuna = request.POST['comunas']
        if comuna != "0": 
            obj_comuna = Comuna.objects.get(pk = comuna)
            inmuebles = inmuebles.filter(comuna=obj_comuna)
        
        print(inmuebles)
        return render(request, 'buscador.html', {'inmuebles':inmuebles})
        

def registro(request):
    if request.method == "POST":
        username = (request.POST["username"])
        email = (request.POST["email"])
        password = (request.POST["password"])
    
        user = User.objects.create_user(username, email, password)
    
        user.first_name = (request.POST["first_name"])
        user.last_name = (request.POST["last_name"])
        
        user.save()#inserta o actualiza
        
        rut =(request.POST["rut"])
        direccion = (request.POST["direccion"])
        telefono = (request.POST["telefono"])
        
        usuario=Usuario.objects.create(user=user, rut=rut, direccion = direccion, telefono=telefono)
        usuario.save()
        
        return redirect('login')
    return render(request, 'registro.html')   

def contacto(request):
    if request.method == "POST":
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            contact_form = ContactoForm.objects.create(**formulario.cleaned_data)
            
            return redirect ('exito/')
    else:
        formulario = ContactoForm()
    return render(request, 'contacto.html', {'formulario': formulario})

