
from area import area
import json 
import random
from pymongo import MongoClient
import json

class DatabaseManager:
    def __init__(self, db_name):
        self.db_client = MongoClient(db_name).test

    def insert_enpleadoselectronica(self, parcelas):
        self.db_client.casas.insert_many(parcelas)
    def deleteallparcelas(self):
        myquery = { "nombre_ciudad": "Novelda" }
        self.db_client.casas.delete_many(myquery)
    def insert_enpleados(self, parcelas):
        self.db_client.tiendas.insert_many(parcelas)
    def deletealltiendas(self):
        myquery = { "nombre_ciudad": "Novelda" }
        self.db_client.tiendas.delete_many(myquery)

pathBBDD = "mongodb+srv://fpratsquilez:GTdbIFamKljeyUvs@worldmanagergame.k3rozlq.mongodb.net/?retryWrites=true&w=majority"


casas = []
tiendas = []
listageojson=["Novelda"]
listanombrescasas=["Casa del Sol","Villa Serenidad","Rincón Acogedor","Morada Tranquila",
"Jardín Secreto","Refugio Verde","Pueblo Encantado","Rinconcito Azul","Palacio de Sueños","Cabaña del Bosque",
"Oasis de Paz","Escondite del Mar","Dulce Morada","Hogar de las Estrellas","Villa del Horizonte"]

listanombrestiendas=["Delicias Gourmet",
"Abasto Fresco",
"Mercado Sabroso",
"Sabor Natural",
"Rincón Delicatessen",
"La Despensa de Sabores",
"Selección de Sabores",
"Gusto en Casa",
"La Cocina de Tradición",
"Rincón Gastronómico",
"Alimenta Bienestar",
"Bocado de Sazón",
"Comida con Amor",
"Delicias de la Tierra",
"Sabores del Mundo"]

for ciudad in listageojson:
    ruta_archivo = f'C:/Users/xisco/Documents/GameManagerWorld/DatosJuego/{ciudad}Casas.geojson'
    
    # Si el GeoJSON está en un archivo
    with open(ruta_archivo, 'r') as archivo:
        geojson = json.load(archivo)

       # Iterar sobre todos los features
    for index,feature in enumerate(geojson['features']):
        precio=random.randint(25000, 120000)
        json={
            "id": index,
            "nombre_casa":random.choice(listanombrescasas),
            "nombre_ciudad":ciudad,
            "precio":precio,
            "prestigio":int(precio/10000),
            "propietario":"Libre",
            "coordenadas_x":feature['geometry']['coordinates'][1],
            "coordenadas_y":feature['geometry']['coordinates'][0],
            "seguridad":0
        }
        casas.append(json)
    print(casas)
    db = DatabaseManager(pathBBDD)
    db.insert_enpleadoselectronica(casas)

""" for ciudad in listageojson:   
    ruta_archivo = f'C:/Users/xisco/Documents/GameManagerWorld/DatosJuego/{ciudad}Tiendas.geojson'
    print(ruta_archivo)
        # Si el GeoJSON está en un archivo
    with open(ruta_archivo, 'r') as archivo2:
        geojson = json.load(archivo2)

        # Iterar sobre todos los features
    for index,feature in enumerate(geojson['features']):
        print(int(area(feature['geometry'])/10000))

        precio=random.randint(25000, 120000)        
        json={
                "id": index,
                "nombre_tienda":random.choice(listanombrestiendas),
                "nombre_ciudad":ciudad,
                "tamano":int(precio/5000),
                "precio":precio,
                "propietario":"Libre",
                "coordenadas_x":feature['geometry']['coordinates'][1],
                "coordenadas_y":feature['geometry']['coordinates'][0],
                "seguridad":0
            }
        tiendas.append(json)
    print(tiendas)
    db = DatabaseManager(pathBBDD)
    db.insert_enpleados(tiendas)  """ 

# db = DatabaseManager(pathBBDD)   
# db.deleteallparcelas()
# db.deletealltiendas()