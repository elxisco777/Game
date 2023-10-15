
from area import area
import json 
import random
from pymongo import MongoClient
import json

class DatabaseManager:
    def __init__(self, db_name):
        self.db_client = MongoClient(db_name).test

    def insert_enpleadoselectronica(self, parcelas):
        self.db_client.parcelas.insert_many(parcelas)
    def deleteallparcelas(self):
        myquery = { "nombre_ciudad": "Novelda" }
        self.db_client.parcelas.delete_many(myquery)

pathBBDD = "mongodb+srv://fpratsquilez:GTdbIFamKljeyUvs@worldmanagergame.k3rozlq.mongodb.net/?retryWrites=true&w=majority"


parcelas = []
listageojson=["Novelda"]
listanombresparcela=["El Vergel Verde","Tierra Fértil","La Granja Encantada","Campo Dorado","La Huerta Serena"
"El Oasis Agrícola","Finca Bella Vista","Rancho Aromático","Cosecha de Sueños","Jardín de la Abundancia","La Colina Productiva"
"Granja Armoniosa","La Parcela del Sol","Vereda del Trigo","Tierras de Esperanza"]
for ciudad in listageojson:
    ruta_archivo = f'C:/Users/xisco/Documents/GameManagerWorld/DatosJuego/{ciudad}.geojson'
    
    # Si el GeoJSON está en un archivo
    with open(ruta_archivo, 'r') as archivo:
        geojson = json.load(archivo)

       # Iterar sobre todos los features
    for feature in geojson['features']:
        print(int(area(feature['geometry'])/10000))
       
        feature['properties']['name']="Libre"
        feature['properties']['tipo']="Parcela"        
        json={
        "objeto":[{"type":"FeatureCollection","features":[feature]}],
        "nombre_ciudad":ciudad,
        "nombre_parcela":random.choice(listanombresparcela),
        "precio":int(area(feature['geometry'])/10000)*random.randint(10000, 13000),
        "tamano":int(area(feature['geometry'])/10000),
        "propietario":"Libre",
        "numeroplantaciones":random.randint(4, 10)
        }
        parcelas.append(json)
    
    db = DatabaseManager(pathBBDD)
    db.insert_enpleadoselectronica(parcelas)   

# db = DatabaseManager(pathBBDD)   
# db.deleteallparcelas()