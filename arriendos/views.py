from django.shortcuts import render
from .models import Inmueble

# Create your views here.
def indexView(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'index.html', {'inmuebles':inmuebles})

