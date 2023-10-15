from pymongo import MongoClient

db_client=MongoClient("mongodb+srv://fpratsquilez:GTdbIFamKljeyUvs@worldmanagergame.k3rozlq.mongodb.net/?retryWrites=true&w=majority").test

def resetpropiedades():
    query = {
        "nombre_ciudad": "Utiel"
    }
    update = {
        "$set": {
            "objeto.0.features.0.properties.name": "Libre"
        }
    }

    # Actualizar los documentos que cumplan con la consulta
    result = db_client.tiendas.update_many(query, update)
    result = db_client.casas.update_many(query, update)
    result = db_client.parcelas.update_many(query, update)
    update = {
        "$set": {
            "propietario": "Libre"
        }
    }

    # Actualizar los documentos que cumplan con la consulta
    result = db_client.tiendas.update_many(query, update)
    result = db_client.casas.update_many(query, update)
    result = db_client.parcelas.update_many(query, update)
    query = {
        "objeto.0.nombre_ciudad": "Novelda"
    }
    update = {
        "$set": {
            "objeto.0.features.0.properties.name": "Libre"
        }
    }

    result = db_client.tiendas.update_many(query, update)
    result = db_client.casas.update_many(query, update)
    result = db_client.parcelas.update_many(query, update)
    update = {
        "$set": {
            "propietario": "Libre"
        }
    }
    result = db_client.tiendas.update_many(query, update)
    result = db_client.casas.update_many(query, update)
    result = db_client.parcelas.update_many(query, update)

#documento_encontrado=db_client.ciudades.find_one({"nombre": "Utiel"})
#print(documento_encontrado.get("poblacion"))
