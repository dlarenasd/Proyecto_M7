from django.shortcuts import render
from .models import Inmueble, Region, Comuna, TipoInmueble
import json
from django.http import JsonResponse

# Create your views here.
def indexView(request):
    tipos_inmuebles = TipoInmueble.objects.all()
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    
    contexto = {'tipos_inmuebles':tipos_inmuebles,
                'regiones':regiones,
                'comunas':comunas}
    return render(request, 'index.html', contexto)

from django.views import generic

class InmueblesListView(generic.ListView):
    model = Inmueble
    context_object_name = 'lista_inmuebles'   # su propio nombre para la lista como variable de plantilla
    template_name = 'arrendador.html'  # Especifique su propio nombre/ubicación de plantilla
    paginate_by = 10
    
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
        inmuebles = Inmueble.objects.all()
        
        tipo_inmueble = request.POST['tipos_inmuebles']
        if tipo_inmueble != None:
            tipo = TipoInmueble.objects.get(pk = tipo_inmueble)
            inmuebles = inmuebles.filter(tipo_inmueble=tipo)
            print(inmuebles)
        region = request.POST['regiones']
        if region != None:
            obj_region = Region.objects.get(pk = region)
            inmuebles = inmuebles.filter(region=obj_region)
        comuna = request.POST['comunas']
        if comuna != None: 
            obj_comuna = Comuna.objects.get(pk = comuna)
            inmuebles = inmuebles.filter(comuna=obj_comuna)
        
        print(inmuebles)
        return render(request, 'buscador.html', {'inmuebles':inmuebles})
        

        