import json
from Usuarios import Usuario
from BBDDMongodb import DatabaseManager

pathBBDD="mongodb+srv://fpratsquilez:GTdbIFamKljeyUvs@worldmanagergame.k3rozlq.mongodb.net/?retryWrites=true&w=majority"

db_manager = DatabaseManager(pathBBDD)

json_data = db_manager.obtener_usuario("Xisco")


print(json_data)

user=Usuario(nombre=json_data["nombre"],bbdd=db_manager)

user.listaciudades=json_data["listaciudades"]
for ciudad in user.listaciudades:
    user.crear_ciudad(ciudad.nombre,db_manager)

user.prestigio=json_data["prestigio"]
user.dinero=json_data["dinero"]
user.almacen=json_data["almacen"]

print(user.dinero)


user.crear_ciudad(nombreciudad="Utiel",bbdd=db_manager)   
user.comprar_casa(nombreciudad="Utiel",nombrecasa="Casa1",bbdd=db_manager)
""" db_manager.cambiar_propietario_casa(nombreCiudad, nombreCasa,  usuario.nombre)
db_manager.cerrar_conexion() """


# Convertir el objeto a un diccionario
usuario_dict = user.__dict__

# Convertir el diccionario a JSON
usuario_json = json.dumps(usuario_dict)

# Deserializar el JSON de nuevo a un diccionario
usuario_dict = json.loads(usuario_json)

# Insertar el diccionario en la base de datos
db_manager.rellenarusuario(usuario_dict)

Datosuser = db_manager.obtener_usuario("Xisco")

print(Datosuser)
