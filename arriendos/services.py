from django.contrib.auth.models import User
from .models import Comuna, Direccion, Inmueble, TipoInmueble, Usuario, TipoUsuario
#CREAR (CREATE)

def crear_direccion(pCalle, pNumero, comuna_id, pIndicaciones, pDepto = None):
    obj_comuna = Comuna.objects.get(pk = comuna_id)
    direccion = Direccion(calle = pCalle, 
                        numero = pNumero, 
                        comuna = obj_comuna,
                        indicaciones = pIndicaciones,
                        depto = pDepto)
    direccion.save()

def crear_tipo_inmueble(pNombre, pDescripcion):
    tipo_inmueble = TipoInmueble(nombre = pNombre, 
                                descripcion = pDescripcion)
    tipo_inmueble.save()
    
def crear_inmueble(pNombre, pDescripcion, pConstruidos, pTerreno, pEstacionamientos, pHabitaciones, pBanios, direccion_id, tipo_id, pPrecio, arrendador_id):
    obj_direccion = Direccion.objects.get(pk=direccion_id)
    obj_tipo_inmueble = TipoInmueble.objects.get(pk = tipo_id)
    
    obj_arrendador = Usuario.objects.get(pk=arrendador_id)
    inmueble = Inmueble(nombre = pNombre, 
                        descripcion = pDescripcion,
                        m2_construidos = pConstruidos,
                        m2_terreno = pTerreno,
                        estacionamientos = pEstacionamientos,
                        habitaciones = pHabitaciones,
                        banios = pBanios,
                        direccion = obj_direccion,
                        tipo_inmueble = obj_tipo_inmueble,
                        precio_mensual = pPrecio)
    inmueble.save()
    inmueble.usuarios.add(obj_arrendador)
    inmueble.save()

def crear_tipo_usuario(pNombre, pDescripcion):
    tipo_usuario = TipoUsuario(nombre = pNombre, 
                                descripcion = pDescripcion)
    tipo_usuario.save()
    
def crear_usuario(user_id, pRut, pDireccion, pTelefono, tipo_id):
    obj_user = User.objects.get(pk=user_id)
    obj_tipo_usuario = TipoUsuario.objects.get(pk=tipo_id)
    
    usuario = Usuario(user = obj_user,
                    rut = pRut,
                    direccion = pDireccion, 
                    telefono = pTelefono,
                    tipo_usuario = obj_tipo_usuario)
    usuario.save()

#LISTAR (READ)

def listar_direcciones():
    lista_direcciones = Direccion.objects.all()
    for direccion in lista_direcciones :
        print(direccion)

def listar_inmuebles():
    lista_inmuebles = Inmueble.objects.all()
    for inmueble in lista_inmuebles :
        print(inmueble)

def listar_usuario():
    lista_usuarios = Usuario.objects.all()
    for usuario in lista_usuarios :
        print(usuario)

def listar_tipo_inmuebles():
    lista_tipos_inmuebles = TipoInmueble.objects.all()
    for tipo in lista_tipos_inmuebles :
        print(tipo)

def listar_tipo_usuarios():
    lista_tipos_usuarios = TipoUsuario.objects.all()
    for tipo in lista_tipos_usuarios :
        print(tipo)

#EDITAR(UPDATE)

def editar_direccion(direccion_id, pCalle, pNumero, comuna_id, pIndicaciones, pDepto = None):
    direccion = Direccion.objects.get(pk=direccion_id)
    crear_direccion(pCalle, pNumero, comuna_id, pIndicaciones, pDepto)
    direccion.save()

def editar_inmueble(inmueble_id, pNombre, pDescripcion, pConstruidos, pTerreno, pEstacionamientos, pHabitaciones, pBanios, direccion_id, tipo_id, pPrecio, arrendador_id):
    inmueble = Inmueble.objects.get(pk=inmueble_id)
    crear_inmueble(pNombre, pDescripcion, pConstruidos, pTerreno, pEstacionamientos, pHabitaciones, pBanios, direccion_id, tipo_id, pPrecio, arrendador_id)
    inmueble.save()

def asignar_arrendatario_a_inmueble(arrendatario_id, inmueble_id):
    inmueble = Inmueble.objects.get(pk=inmueble_id)
    arrendatario = Usuario.objects.get(pk=arrendatario_id)
    
    inmueble.usuarios.add(arrendatario)
    inmueble.save()
#FALTA UN MÉTODO PARA DESASIGNAR USUARIOS A UN INMUEBLE
def editar_usuario(usuario_id, user_id, pRut, pDireccion, pTelefono, tipo_id):
    usuario = Usuario.objects.get(pk = usuario_id)
    crear_usuario(user_id, pRut, pDireccion, pTelefono, tipo_id)
    usuario.save()

def editar_tipo_inmueble(tipo_id, pNombre, pDescripcion):
    tipo_inmueble = TipoInmueble.objects.get(pk = tipo_id)
    crear_tipo_inmueble(pNombre, pDescripcion)
    tipo_inmueble.save()

def editar_tipo_usuario(tipo_id, pNombre, pDescripcion):
    tipo_usuario = TipoUsuario.objects.get(pk = tipo_id)
    crear_tipo_usuario(pNombre, pDescripcion)
    tipo_usuario.save()

#ELIMINAR (DELETE)

def eliminar_direccion(direccion_id):
    Direccion.objects.get(pk=direccion_id).delete()

def eliminar_inmueble(inmueble_id):
    Inmueble.objects.get(pk=inmueble_id).delete()

def eliminar_usuario(usuario_id):
    Usuario.objects.get(pk=usuario_id).delete()

def eliminar_tipo_inmueble(tipo_id):
    TipoInmueble.objects.get(pk=tipo_id).delete()

def eliminar_tipo_usuario(tipo_id):
    TipoUsuario.objects.get(pk=tipo_id).delete()