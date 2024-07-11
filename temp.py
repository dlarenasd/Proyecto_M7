import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CRUD.settings")
django.setup()

from arriendos.models import Inmueble

select_inmuebles ="""select * from arriendos_inmueble"""
select_arrendadas ="""select * from arriendos_inmueble where arrendada = True"""
select_para_arriendo ="""select * from arriendos_inmueble where arrendada = False"""
""" 
query = Inmueble.objects.raw(select_inmuebles)
for inm in query:
    file.write(inm.nombre)
    file.write(inm.descripcion)
    file.write(inm.arrendada)
    
    """

def listar_por_comuna(nombre_comuna):
    select = f""" select inm.id, inm.nombre, comuna.nombre, region.nombre 
    from arriendos_inmueble inm
    inner join arriendos_comuna comuna on
    inm.comuna_id = comuna.id
    inner join arriendos_region region on
    inm.region_id = region.id
    where comuna.nombre LIKE %s 
    """
    data = Inmueble.objects.raw(select, [f'%{nombre_comuna}%'])
    archi1=open("porcomuna.txt", "a", encoding="utf-8")
    for inm in data:
        archi1.write(f"{inm.id} - {inm.nombre} - {inm.comuna.nombre} \n")
        archi1.write(f"\t {inm.descripcion}")
        archi1.write('\n'+'\n')
    archi1.close()

def listar_por_region(nombre_region):
    select = f""" select inm.id, inm.nombre, comuna.nombre, region.nombre 
    from arriendos_inmueble inm
    inner join arriendos_comuna comuna on
    inm.comuna_id = comuna.id
    inner join arriendos_region region on
    inm.region_id = region.id
    where region.nombre LIKE %s
    """
    print(nombre_region)
    data = Inmueble.objects.raw(select, [f'%{nombre_region}%'])  
    print(data)
    archi2=open("porregion.txt", "a", encoding="utf-8")
    for inm in data:
        archi2.write(f"{inm.id} - {inm.nombre} - {inm.region.nombre} \n")
        archi2.write(f"\t {inm.descripcion}")
        archi2.write('\n'+'\n')
    archi2.close()
    
    
"""
CÓDIGO PROFE
def obtener_inmuebles_comuna(comuna_nombre):
    select = '''
            select inmu.id, inmu.nombre,
            comuna.name as comuna, region.name as region
            from miapp_inmueble inmu
            inner join miapp_comuna comuna
            on inmu.comuna_id = comuna.id
            inner join miapp_region region
            on inmu.region_id = region.id
            where comuna.name LIKE '%'''+str(comuna_nombre)+'''%'
            '''
    data_inmuebles = Inmueble.objects.raw(select)

    archivo = open("inmueble_comuna.txt", "w")

    for inmu in data_inmuebles:
        archivo.write(inmu.id +'-' +inmu.nombre +'\n')

    archivo.close()


def obtener_inmueble(nombre, descripcion):
    lista_inmuebles = Inmueble.objects.filter(nombre__contains=nombre).filter(descripcion__contains=descripcion)

    archivo = open("inmueble_nombre_des.txt", "w")

    for inmu in lista_inmuebles:
        archivo.write(inmu +'\n')

    archivo.close()
"""

if __name__=="__main__":
    listar_por_comuna("Temuco")
    listar_por_region("Araucanía")
    listar_por_comuna("San Antonio")
    listar_por_region("Metropolitana")
    listar_por_comuna("La Pintana")
    listar_por_region("Los Lagos")

