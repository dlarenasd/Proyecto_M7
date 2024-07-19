from string import Template
import json

def comuna_template():
    comuna_template = Template(str({"model":"arriendos.comunas","fields": {"nombre" : "$comuna","region" : ""}}))
    return comuna_template

comunas_tarapaca = [
        {"name": "Alto Hospicio"},
        {"name": "Camiña"},
        {"name": "Colchane"},
        {"name": "Huara"},
        {"name": "Iquique"},
        {"name": "Pica"},
        {"name": "Pozo Almonte"}
    ]

comunas_antofagasta = [
            {"name": "Antofagasta"},
            {"name": "Calama"},
            {"name": "María Elena"},
            {"name": "Mejillones"},
            {"name": "Ollagüe"},
            {"name": "San Pedro de Atacama"},
            {"name": "Sierra Gorda"},
            {"name": "Taltal"},
            {"name": "Tocopilla"}
        ]

comunas_atacama =  [
            {"name": "Alto del Carmen"},
            {"name": "Caldera"},
            {"name": "Chañaral"},
            {"name": "Copiapó"},
            {"name": "Diego de Almagro"},
            {"name": "Freirina"},
            {"name": "Huasco"},
            {"name": "Tierra Amarilla"},
            {"name": "Vallenar"}
        ]

comunas_coquimbo = [
            {"name": "Andacollo"},
            {"name": "Canela"},
            {"name": "Combarbalá"},
            {"name": "Coquimbo"},
            {"name": "Illapel"},
            {"name": "La Higuera"},
            {"name": "La Serena"},
            {"name": "Los Vilos"},
            {"name": "Monte Patria"},
            {"name": "Ovalle"},
            {"name": "Paiguano"},
            {"name": "Punitaqui"},
            {"name": "Río Hurtado"},
            {"name": "Salamanca"},
            {"name": "Vicuña"}
        ]

comunas_valparaiso = [
            {"name": "Algarrobo"},
            {"name": "Cabildo"},
            {"name": "Calera"},
            {"name": "Calle Larga"},
            {"name": "Cartagena"},
            {"name": "Casablanca"},
            {"name": "Catemu"},
            {"name": "Concón"},
            {"name": "El Quisco"},
            {"name": "El Tabo"},
            {"name": "Hijuelas"},
            {"name": "Isla de Pascua"},
            {"name": "Juan Fernández"},
            {"name": "La Cruz"},
            {"name": "La Ligua"},
            {"name": "Limache"},
            {"name": "Llaillay"},
            {"name": "Los Andes"},
            {"name": "Nogales"},
            {"name": "Olmué"},
            {"name": "Panquehue"},
            {"name": "Papudo"},
            {"name": "Petorca"},
            {"name": "Puchuncaví"},
            {"name": "Putaendo"},
            {"name": "Quillota"},
            {"name": "Quilpué"},
            {"name": "Quintero"},
            {"name": "Rinconada"},
            {"name": "San Antonio"},
            {"name": "San Esteban"},
            {"name": "San Felipe"},
            {"name": "Santa María"},
            {"name": "Santo Domingo"},
            {"name": "Valparaíso"},
            {"name": "Villa Alemana"},
            {"name": "Viña del Mar"},
            {"name": "Zapallar"}
        ]

comunas_ohiggins = [
            {"name": "Chimbarongo"},
            {"name": "Chépica"},
            {"name": "Codegua"},
            {"name": "Coinco"},
            {"name": "Coltauco"},
            {"name": "Doñihue"},
            {"name": "Graneros"},
            {"name": "La Estrella"},
            {"name": "Las Cabras"},
            {"name": "Litueche"},
            {"name": "Lolol"},
            {"name": "Machalí"},
            {"name": "Malloa"},
            {"name": "Marchihue"},
            {"name": "Nancagua"},
            {"name": "Navidad"},
            {"name": "Olivar"},
            {"name": "Palmilla"},
            {"name": "Paredones"},
            {"name": "Peralillo"},
            {"name": "Peumo"},
            {"name": "Pichidegua"},
            {"name": "Pichilemu"},
            {"name": "Placilla"},
            {"name": "Pumanque"},
            {"name": "Quinta de Tilcoco"},
            {"name": "Rancagua"},
            {"name": "Rengo"},
            {"name": "Requínoa"},
            {"name": "San Fernando"},
            {"name": "San Francisco de Mostazal"},
            {"name": "San Vicente de Tagua Tagua"},
            {"name": "Santa Cruz"}
        ]

comunas_maule = [
            {"name": "Cauquenes"},
            {"name": "Chanco"},
            {"name": "Colbún"},
            {"name": "Constitución"},
            {"name": "Curepto"},
            {"name": "Curicó"},
            {"name": "Empedrado"},
            {"name": "Hualañé"},
            {"name": "Licantén"},
            {"name": "Linares"},
            {"name": "Longaví"},
            {"name": "Maule"},
            {"name": "Molina"},
            {"name": "Parral"},
            {"name": "Pelarco"},
            {"name": "Pelluhue"},
            {"name": "Pencahue"},
            {"name": "Rauco"},
            {"name": "Retiro"},
            {"name": "Romeral"},
            {"name": "Río Claro"},
            {"name": "Sagrada Familia"},
            {"name": "San Clemente"},
            {"name": "San Javier de Loncomilla"},
            {"name": "San Rafael"},
            {"name": "Talca"},
            {"name": "Teno"},
            {"name": "Vichuquén"},
            {"name": "Villa Alegre"},
            {"name": "Yerbas Buenas"}
        ]

comunas_biobio = [
            {"name": "Alto Biobío"},
            {"name": "Antuco"},
            {"name": "Arauco"},
            {"name": "Cabrero"},
            {"name": "Cañete"},
            {"name": "Chiguayante"},
            {"name": "Concepción"},
            {"name": "Contulmo"},
            {"name": "Coronel"},
            {"name": "Curanilahue"},
            {"name": "Florida"},
            {"name": "Hualpén"},
            {"name": "Hualqui"},
            {"name": "Laja"},
            {"name": "Lebu"},
            {"name": "Los Álamos"},
            {"name": "Los Ángeles"},
            {"name": "Lota"},
            {"name": "Mulchén"},
            {"name": "Nacimiento"},
            {"name": "Negrete"},
            {"name": "Penco"},
            {"name": "Quilaco"},
            {"name": "Quilleco"},
            {"name": "San Pedro de la Paz"},
            {"name": "San Rosendo"},
            {"name": "Santa Bárbara"},
            {"name": "Santa Juana"},
            {"name": "Talcahuano"},
            {"name": "Tirúa"},
            {"name": "Tomé"},
            {"name": "Tucapel"},
            {"name": "Yumbel"}
        ]

comunas_araucania = [
            {"name": "Angol"},
            {"name": "Carahue"},
            {"name": "Cholchol"},
            {"name": "Collipulli"},
            {"name": "Cunco"},
            {"name": "Curacautín"},
            {"name": "Curarrehue"},
            {"name": "Ercilla"},
            {"name": "Freire"},
            {"name": "Galvarino"},
            {"name": "Gorbea"},
            {"name": "Lautaro"},
            {"name": "Loncoche"},
            {"name": "Lonquimay"},
            {"name": "Los Sauces"},
            {"name": "Lumaco"},
            {"name": "Melipeuco"},
            {"name": "Nueva Imperial"},
            {"name": "Padre las Casas"},
            {"name": "Perquenco"},
            {"name": "Pitrufquén"},
            {"name": "Pucón"},
            {"name": "Purén"},
            {"name": "Renaico"},
            {"name": "Saavedra"},
            {"name": "Temuco"},
            {"name": "Teodoro Schmidt"},
            {"name": "Toltén"},
            {"name": "Traiguén"},
            {"name": "Victoria"},
            {"name": "Vilcún"},
            {"name": "Villarrica"}
        ]

comunas_loslagos = [
            {"name": "Ancud"},
            {"name": "Calbuco"},
            {"name": "Castro"},
            {"name": "Chaitén"},
            {"name": "Chonchi"},
            {"name": "Cochamó"},
            {"name": "Curaco de Vélez"},
            {"name": "Dalcahue"},
            {"name": "Fresia"},
            {"name": "Frutillar"},
            {"name": "Futaleufú"},
            {"name": "Hualaihué"},
            {"name": "Llanquihue"},
            {"name": "Los Muermos"},
            {"name": "Maullín"},
            {"name": "Osorno"},
            {"name": "Palena"},
            {"name": "Puerto Montt"},
            {"name": "Puerto Octay"},
            {"name": "Puerto Varas"},
            {"name": "Puqueldón"},
            {"name": "Purranque"},
            {"name": "Puyehue"},
            {"name": "Queilén"},
            {"name": "Quellón"},
            {"name": "Quemchi"},
            {"name": "Quinchao"},
            {"name": "Río Negro"},
            {"name": "San Juan de la Costa"},
            {"name": "San Pablo"}
        ]

comunas_aysen=  [
            {"name": "Aysén"},
            {"name": "Chile Chico"},
            {"name": "Cisnes"},
            {"name": "Cochrane"},
            {"name": "Coyhaique"},
            {"name": "Guaitecas"},
            {"name": "Lago Verde"},
            {"name": "O’Higgins"},
            {"name": "Río Ibáñez"},
            {"name": "Tortel"}
        ]

comunas_magallanes = [
            {"name": "Antártica"},
            {"name": "Cabo de Hornos (Ex Navarino)"},
            {"name": "Laguna Blanca"},
            {"name": "Natales"},
            {"name": "Porvenir"},
            {"name": "Primavera"},
            {"name": "Punta Arenas"},
            {"name": "Río Verde"},
            {"name": "San Gregorio"},
            {"name": "Timaukel"},
            {"name": "Torres del Paine"}
        ]

comunas_metropolitana = [
            {"name": "Alhué"},
            {"name": "Buin"},
            {"name": "Calera de Tango"},
            {"name": "Cerrillos"},
            {"name": "Cerro Navia"},
            {"name": "Colina"},
            {"name": "Conchalí"},
            {"name": "Curacaví"},
            {"name": "El Bosque"},
            {"name": "El Monte"},
            {"name": "Estación Central"},
            {"name": "Huechuraba"},
            {"name": "Independencia"},
            {"name": "Isla de Maipo"},
            {"name": "La Cisterna"},
            {"name": "La Florida"},
            {"name": "La Granja"},
            {"name": "La Pintana"},
            {"name": "La Reina"},
            {"name": "Lampa"},
            {"name": "Las Condes"},
            {"name": "Lo Barnechea"},
            {"name": "Lo Espejo"},
            {"name": "Lo Prado"},
            {"name": "Macul"},
            {"name": "Maipú"},
            {"name": "María Pinto"},
            {"name": "Melipilla"},
            {"name": "Ñuñoa"},
            {"name": "Padre Hurtado"},
            {"name": "Paine"},
            {"name": "Pedro Aguirre Cerda"},
            {"name": "Peñaflor"},
            {"name": "Peñalolén"},
            {"name": "Pirque"},
            {"name": "Providencia"},
            {"name": "Pudahuel"},
            {"name": "Puente Alto"},
            {"name": "Quilicura"},
            {"name": "Quinta Normal"},
            {"name": "Recoleta"},
            {"name": "Renca"},
            {"name": "San Bernardo"},
            {"name": "San Joaquín"},
            {"name": "San José de Maipo"},
            {"name": "San Miguel"},
            {"name": "San Pedro"},
            {"name": "San Ramón"},
            {"name": "Santiago"},
            {"name": "Talagante"},
            {"name": "Tiltil"},
            {"name": "Vitacura"}
        ]

comunas_losrios = [
            {"name": "Corral"},
            {"name": "Futrono"},
            {"name": "La Unión"},
            {"name": "Lago Ranco"},
            {"name": "Lanco"},
            {"name": "Los Lagos"},
            {"name": "Mariquina"},
            {"name": "Máfil"},
            {"name": "Paillaco"},
            {"name": "Panguipulli"},
            {"name": "Río Bueno"},
            {"name": "Valdivia"}
        ]

comunas_arica = [
            {"name": "Arica"},
            {"name": "Camarones"},
            {"name": "General Lagos"},
            {"name": "Putre"}
        ]

comunas_nuble = [
            {"name": "Bulnes"},
            {"name": "Chillán Viejo"},
            {"name": "Chillán"},
            {"name": "Cobquecura"},
            {"name": "Coelemu"},
            {"name": "Coihueco"},
            {"name": "El Carmen"},
            {"name": "Ninhue"},
            {"name": "Ñiquén"},
            {"name": "Pemuco"},
            {"name": "Pinto"},
            {"name": "Portezuelo"},
            {"name": "Quillón"},
            {"name": "Quirihue"},
            {"name": "Ránquil"},
            {"name": "San Carlos"},
            {"name": "San Fabián"},
            {"name": "San Ignacio"},
            {"name": "San Nicolás"},
            {"name": "Treguaco"},
            {"name": "Yungay"}
        ]

comunas_chile = [comunas_tarapaca, comunas_antofagasta, comunas_atacama, comunas_coquimbo, comunas_valparaiso, comunas_ohiggins, comunas_maule, comunas_biobio, comunas_araucania, comunas_loslagos, comunas_aysen, comunas_magallanes, comunas_metropolitana, comunas_losrios, comunas_arica, comunas_nuble]
def lista_nombres(comunas):
    lista =[]
    for dicc in comunas:
        lista.append(dicc['name'])
    return lista

if __name__ == "__main__":
    variable_json =[]
    template = comuna_template()
    file = open('comunas.json', 'a', encoding="utf-8")
    file.write('[')
    i=1
    for lista in comunas_chile:
        l = lista_nombres(lista)
        for comuna in l:
            #variable_json.append(template.substitute(comuna = comuna))
            
            j = {"model":"arriendos.comunas",
                "fields": {"nombre" : comuna,
                        "region" : i}
                }
            file.write(str(j))
            file.write(',\n')
        i+=1
    file.write(']')  
            #variable_json.append(j)
            #print(j)
            #print("\n")
    #print(variable_json)
        
        
    #variable_json = (dict(variable_json))
    #file.write(str(variable_json))
    
    #data = json.dumps(variable_json)
    
    #arreglo=(json.loads(data))
    #print(arreglo)"""
    
    