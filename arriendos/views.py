from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, HttpResponseRedirect
from .models import Inmueble, Region, Comuna, TipoInmueble, Contacto, Solicitud, Usuario, TipoUsuario
from .forms import ContactoForm, SolicitudForm, UsuarioForm, InmuebleForm
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import generic
from .services import crear_inmueble, inmueble_editar, inmueble_eliminar, usuario_editar



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

class InmuebleCreateView(generic.CreateView):
    model = Inmueble
    form_class = InmuebleForm
    template_name = "inmueble_crear.html"
    success_url = "/inmuebles/"
    
    def form_valid(self,form):
        inmueble=form.save(commit=False)
        inmueble.save()
        inmueble.usuarios.add(self.request.user.usuario.rut)
        return super().form_valid(form)
        
    
def ver_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, pk=id)
    
    return render(request, 'ver_inmueble.html', {'inm':inmueble})

@login_required
def editar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, pk=id)
    form = InmuebleForm(instance=inmueble)
    contexto = {'inm':inmueble, 'form':form}
    
    if request.method =="POST":
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            data = form.cleaned_data
        data['arrendada'] = 'arrendada' in request.POST
        inmueble_editar(data, id)
        return redirect('inmuebles')
    
    return render(request, 'inmueble_editar.html', contexto)
    


def eliminar_inmueble(request, id):
    Inmueble.objects.get(pk=id).delete()
    return redirect('inmuebles')
    


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
    else:
        return HttpResponseRedirect(request, 'indice')
        

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

def usuario(request):
    
    return render(request, 'usuario.html', {'usuario':request.user.usuario})

def actualizar_usuario(request):
    if request.method =="POST":
        usuario_editar(request.POST)
        
        return redirect('usuario')
    else:
        usuario=request.user.usuario
        contexto = {'usuario':usuario}
        return render(request, 'editar_usuario.html', contexto)

""" 
def editar_usuario(request, rut):
    usuario = get_object_or_404(Usuario, pk=rut)
    formulario = UsuarioForm()
    
    return render(request, 'editar_usuario.html', {'usuario':usuario, 'formulario': formulario}) 



formulario = UsuarioForm(instance=request.user.usuario)
usuario=request.user.usuario
print("MIREN ACÁ")
print(request.user.usuario)
try:
    print("A ver si entra")
    if request.method =="POST":
        print("VAMOS QUE SE PUEDE")
        
        pUsername = (request.POST["username"])
        pEmail = (request.POST["email"])
        pFirst_name = (request.POST["first_name"])
        pLast_name = (request.POST["last_name"])
        pTelefono = (request.POST["telefono"])
        pDireccion = (request.POST["direccion"])
        formulario.save()
        print(pUsername)
        
        usuario_editar(usuario.user.id, usuario.rut, pDireccion, pTelefono, usuario.tipo_usuario, pFirst_name, pLast_name, pEmail, pUsername)
        usuario.user.save()
        usuario.save()
            
        return redirect('usuario')
except Exception as e:
    return e        
    #formulario=UsuarioForm()
else:
    print("No sabes qué pasa")
return render(request, 'editar_usuario.html', {'usuario':usuario, 'formulario': formulario})
        


def select2(request):
    contexto = {'formulario': Select2Form()}
    return render(request, 'select2.html', contexto)
    

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
"""