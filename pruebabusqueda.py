from Usuarios import Usuario
from BBDDMongodb import DatabaseManager
import json

pathBBDD="mongodb+srv://fpratsquilez:GTdbIFamKljeyUvs@worldmanagergame.k3rozlq.mongodb.net/?retryWrites=true&w=majority"

db_manager = DatabaseManager(pathBBDD)

print(db_manager.leer_parcelasPropia("Utiel","Parcela1","Xisco"))