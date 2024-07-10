from django.contrib.auth.models import User
from .models import Comuna, Inmueble, TipoInmueble, Usuario, TipoUsuario, Region
from .baseModel import BaseModel as bm

class InmuebleModel(bm):

    def sql_obtener_todos_inmuebles():
        sql = "select nombre, arrendada from arriendos_inmueble"
        parametros = None
        inmuebles= list(bm.execute(sql,parametros))

        for inmu in inmuebles:
            print(inmu)

        return inmuebles

    def obtener_todos_inmuebles():
        return Inmueble.objects.all()
    
    def raw_obtener_todos_inmuebles():
        sql = "select nombre, arrendada from arriendos_inmueble"
        query = Inmueble.objects.raw(sql)
        for p in query:
            print(p.nombre)
            print(p.arrendada)
            
#class ClienteModel
        

#CREAR (CREATE)

def crear_tipo_inmueble(pNombre, pDescripcion):
    tipo_inmueble = TipoInmueble(nombre = pNombre, 
                                descripcion = pDescripcion)
    tipo_inmueble.save()
    
def crear_inmueble(pNombre, pDescripcion, pConstruidos, pTerreno, pEstacionamientos, pHabitaciones, pBanios, pDireccion, comuna_id, region_id, tipo_id, pPrecio, arrendador_id):
    obj_comuna = Comuna.objects.get(pk=comuna_id)
    obj_region = Region.objects.get(pk=region_id)
    obj_tipo_inmueble = TipoInmueble.objects.get(pk = tipo_id)
    
    obj_arrendador = Usuario.objects.get(pk=arrendador_id)
    inmueble = Inmueble(nombre = pNombre, 
                        descripcion = pDescripcion,
                        m2_construidos = pConstruidos,
                        m2_terreno = pTerreno,
                        estacionamientos = pEstacionamientos,
                        habitaciones = pHabitaciones,
                        banios = pBanios,
                        direccion = pDireccion,
                        comuna = obj_comuna,
                        region = obj_region,
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

def editar_inmueble(inmueble_id, pNombre, pDescripcion, pConstruidos, pTerreno, pEstacionamientos, pHabitaciones, pBanios, pDireccion, comuna_id, region_id, tipo_id, pPrecio, arrendador_id):
    inmueble = Inmueble.objects.get(pk=inmueble_id)
    crear_inmueble(pNombre, pDescripcion, pConstruidos, pTerreno, pEstacionamientos, pHabitaciones, pBanios, pDireccion, comuna_id, region_id, tipo_id, pPrecio, arrendador_id)
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

def eliminar_inmueble(inmueble_id):
    Inmueble.objects.get(pk=inmueble_id).delete()

def eliminar_usuario(usuario_id):
    Usuario.objects.get(pk=usuario_id).delete()

def eliminar_tipo_inmueble(tipo_id):
    TipoInmueble.objects.get(pk=tipo_id).delete()

def eliminar_tipo_usuario(tipo_id):
    TipoUsuario.objects.get(pk=tipo_id).delete()