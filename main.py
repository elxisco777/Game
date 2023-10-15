#from BBDD import DatabaseManager
from Usuarios import Usuario
from Fecha import Fecha
from Parcela import Parcela
from Tienda import Tienda
import threading
import time
from fastapi import FastAPI, WebSocket, WebSocketDisconnect,  Depends, status,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from BBDDMongodb import DatabaseManager
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import ResetApp
import random

from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

multaRobo=20000
maximoRoboCasa=30000
minimoRoboCasa=4000
cantidadMultaParcela=5000
cantidadMultaTienda=5000
cantidadMultaRoboParcela=15000
cantidadMultaRoboTienda=15000

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "201d573bd7d1344d3a3bfce1550b69102fd11be3db6d379508b6cccc58ea230b"

app = FastAPI() 
app.mount("/static",StaticFiles(directory="static"), name="static")
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

# Configurar las opciones CORS
origins = [
    "http://localhost",   # Agrega aquí el dominio desde el cual haces la solicitud
    "http://localhost:8081",  # Ejemplo de otro puerto en el mismo dominio
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ano=2023
mes=8

store = [] 

produccion = {
    "tipo": str,
    "numero": int,
}

usuario_websocket = {
    "IDMessage":str,
    "dinero": float,
    "ano": int,
    "mes": str,
}

listaUsuarios=[]
""" parcelas= [{"latlngs": [
          [39.579050609911903, -1.220224224655142],
          [39.576351044055677, -1.216233073859005],
          [39.574565236362353, -1.218315839408093],
          [39.577960455492203, -1.221456259419051],
          [39.57906273049214, -1.222462465563326],
          [39.579050609911903, -1.220224224655142]
        ],
        "color": "#ff00ff",
        "name": "parcela de Utiel"}] """
parcelas= [{"objeto": [],
        "name": "",
        "precio": 0,
        "tamano": 0}]
json = [ { "name": "Madrid", "coords": [ 40.416775, -3.70379 ], "radius": 10000 }, { "name": "Barcelona", "coords": [ 41.385063, 2.173404 ], "radius": 8000 }, { "name": "Sevilla", "coords": [ 37.389092, -5.984459 ], "radius": 5000 }, { "name": "Valencia", "coords": [ 39.469907, -0.376288 ], "radius": 6000 }, { "name": "Utiel", "coords": [ 39.5671463, -1.2019213 ], "radius": 2000 } ]
usuarioo = {
    "username": "Xisco",
    "full_name": "Xisco",
    "email": "fprats",
    "disabled": False,
}
""" mensajes= [{
        "IDMessage":"",
        "mensaje": "",
        "usuarioRival": "",
        "usuario":"",
        "nombreciudad":"",
        "lugar":"",
        "oferta":0,
        }]  """
mensajes= []
mensajesOfertaAceRech= [{
        "IDMessage":"",
        "mensaje": "",
        "usuarioRival": "",
        "usuario":"",
        "nombreciudad":"",
        "lugar":"",
        "aceptada":False,
        }]  # mensaje cambiar a array

from typing import List




class ConnectionManager:
    def __init__(self):
        self.active_connections: List[dict] = []

    async def connect(self, websocket, clientid):
        await websocket.accept()
        self.active_connections.append({"websocket": websocket, "clientid": clientid})
        print(List)

    def disconnect(self, websocket):
        connection = next((conn for conn in self.active_connections if conn["websocket"] == websocket), None)
        if connection:
            self.active_connections.remove(connection)

    # async def send_personal_message(self, message, clientid):
    #     connection = next((conn for conn in self.active_connections if conn["clientid"] == clientid), None)
    #     if connection:
    #         print(connection["clientid"])
    #         await connection["websocket"].send_text(message)

    async def broadcast(self, message):
        for connection in self.active_connections:
            await connection["websocket"].send_text(message)

    async def send_personal_message(self, message, websocket):
        connection = next((conn for conn in self.active_connections if conn["websocket"] == websocket), None)
        if connection:
            await connection["websocket"].send_text(message)

""" 
List = []
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket, clientid:str):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message) """



async def auth_user(token: str = Depends(oauth2)):

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas",
        headers={"WWW-Authenticate": "Bearer"})

    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception

    except JWTError:
        raise exception

    return usuarioo


async def current_user(user: usuarioo = Depends(auth_user)):
    if user.get("disable"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")

    return user





manager = ConnectionManager()
#pathBBDD="BBDD/GameWorldManager"

pathBBDD="mongodb+srv://fpratsquilez:GTdbIFamKljeyUvs@worldmanagergame.k3rozlq.mongodb.net/?retryWrites=true&w=majority"

db_manager = DatabaseManager(pathBBDD)

def cargarUsuarios():

    for Datosuser in db_manager.GetUsuarios():
        print("usuario")
        usuario_objeto=Usuario(nombre=Datosuser["nombre"],bbdd=db_manager)
        for indexciudad, ciudad in enumerate(Datosuser["listaciudades"]):
            usuario_objeto.crear_ciudad(nombreciudad=ciudad["nombre"],bbdd=db_manager)

            for indextiendas, tienda in enumerate(ciudad["listatiendas"]):
                usuario_objeto.comprar_tienda(nombreciudad=ciudad["nombre"],nombretienda=tienda["nombre"],bbdd=db_manager)
                
                for indexproductos, producto in enumerate(tienda["arrayProductos"]):
                    usuario_objeto.agregar_producto(nombreciudad=ciudad["nombre"],nombretienda=tienda["nombre"],tipoproducto=producto["tipo"])
                
                for indexempleadostiendas, empleado in enumerate(tienda["arrayEmpleados"]):
                    usuario_objeto.contratarempleado(nombreciudad=ciudad["nombre"],lugar=tienda["nombre"],nombreempleado=empleado["nombre"],bbdd=db_manager)
                    usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].listaempleados[indexempleadostiendas].nombre=empleado["nombre"]          
                    usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].listaempleados[indexempleadostiendas].productividad=empleado["productividad"]  
                    usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].listaempleados[indexempleadostiendas].precio=empleado["precio"]  
                    usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].listaempleados[indexempleadostiendas].comunicacion=empleado["comunicacion"]
                    usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].listaempleados[indexempleadostiendas].estudios=empleado["estudios"]
                    usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].listaempleados[indexempleadostiendas].fuerza=empleado["fuerza"]
                    usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].listaempleados[indexempleadostiendas].liderazgo=empleado["liderazgo"]

                usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].nombre=tienda["nombre"]
                usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].tamaño=tienda["tamaño"]
                usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].precio=tienda["precio"]
                usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].numeroEmpleados=tienda["numeroEmpleados"]
                usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].numeroMaximoEmpleados=tienda["numeroMaximoEmpleados"]
                usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].indiceproduccionempleados=tienda["indiceproduccionempleados"]
                usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].indiceTiempo=tienda["indiceTiempo"]
                usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].indiceVariedadProductos=tienda["indiceVariedadProductos"]
                usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].ciudadtienda=tienda["ciudadtienda"]
                usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].indiceproductividadempleados=tienda["indiceproductividadempleados"]
                usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].seguridad=tienda["seguridad"]
                usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].maximaSeguridad=tienda["maximaSeguridad"]
                usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].indiceMaximoTiempo=tienda["indiceMaximoTiempo"]
                
            
            for indexParcelas, parcela in enumerate(ciudad["listaparcelas"]):
                usuario_objeto.comprar_parcela(nombreciudad=ciudad["nombre"],nombreparcela=parcela["nombre"],bbdd=db_manager)
                
                for indexplantacion, plantacion in enumerate(parcela["listaplantacion"]):
                    usuario_objeto.modificar_plantacion(indice=indexplantacion,nombreciudad=ciudad["nombre"],nombreparcela=parcela["nombre"],tipoplantacion=plantacion["tipo"],bbdd=db_manager)
                    usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaplantacion[indexplantacion].factormultiplicacion=plantacion["factormultiplicacion"]
                    usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaplantacion[indexplantacion].produccionmes=plantacion["produccionmes"]
                    usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaplantacion[indexplantacion].urlicono=plantacion["urlicono"]



                for indexempleadosparcela, empleado in enumerate(parcela["listaempleados"]):
                    usuario_objeto.contratarempleado(nombreciudad=ciudad["nombre"],lugar=parcela["nombre"],nombreempleado=empleado["nombre"],bbdd=db_manager)
                    usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaempleados[indexempleadosparcela].nombre=empleado["nombre"]          
                    usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaempleados[indexempleadosparcela].productividad=empleado["productividad"]  
                    usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaempleados[indexempleadosparcela].precio=empleado["precio"]  
                    usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaempleados[indexempleadosparcela].comunicacion=empleado["comunicacion"]
                    usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaempleados[indexempleadosparcela].estudios=empleado["estudios"]
                    usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaempleados[indexempleadosparcela].fuerza=empleado["fuerza"]
                    usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaempleados[indexempleadosparcela].liderazgo=empleado["liderazgo"]

                usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].nombre=parcela["nombre"]
                usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].tamaño=parcela["tamaño"]
                usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].precio=parcela["precio"]
                usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].numeroEmpleados=parcela["numeroEmpleados"]
                usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].numeroMaximoEmpleados=parcela["numeroMaximoEmpleados"]
                usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].indiceproduccionempleados=parcela["indiceproduccionempleados"]
                usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].factorMultiplicacionProducto=parcela["factorMultiplicacionProducto"]
                usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].calidadterreno=parcela["calidadterreno"]
                usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].ciudadParcela=parcela["ciudadParcela"]
                usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].indiceproductividadempleados=parcela["indiceproductividadempleados"]
                usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].seguridad=parcela["seguridad"]
                usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].maximaSeguridad=parcela["maximaSeguridad"]    
            ciudadCasa= ciudad["casa"]
            if ciudadCasa != "":
                usuario_objeto.comprar_casa(nombreciudad=ciudad["nombre"],nombrecasa=ciudadCasa["nombre"],bbdd=db_manager)
                usuario_objeto.listaciudades[indexciudad].casa.precio=ciudadCasa["precio"]
                usuario_objeto.listaciudades[indexciudad].casa.prestigio=ciudadCasa["prestigio"]
            
            usuario_objeto.listaciudades[indexciudad].idioma_principal=ciudad["idioma_principal"]
            usuario_objeto.listaciudades[indexciudad].poblacion=ciudad["poblacion"]
            usuario_objeto.listaciudades[indexciudad].factorMultiplicacionProducto=ciudad["factorMultiplicacionProducto"]
            usuario_objeto.listaciudades[indexciudad].prestigioCasa=ciudad["prestigioCasa"]

        usuario_objeto.prestigio=Datosuser["prestigio"]
        usuario_objeto.dinero=Datosuser["dinero"]
        usuario_objeto.almacen=Datosuser["almacen"]
        usuario_objeto.id=str(Datosuser["_id"])
        usuario_objeto.mostrar_informacion()
        listaUsuarios.append(usuario_objeto)
    return


cargarUsuarios()



async def periodic_broadcast():
    while True:

        await asyncio.sleep(20)  # Espera 20 segundos
        for usuario in listaUsuarios:
            usuario_websocket["IDMessage"]="DatosMensuales"
            usuario_websocket["ano"]=fecha.ano
            if fecha.mes == 1:
                usuario_websocket["mes"]="Ene"
            if fecha.mes == 2:
                usuario_websocket["mes"]="Feb"
            if fecha.mes == 3:
                usuario_websocket["mes"]="Mar"
            if fecha.mes == 4:
                usuario_websocket["mes"]="Abr"
            if fecha.mes == 5:
                usuario_websocket["mes"]="May"
            if fecha.mes == 6:
                usuario_websocket["mes"]="Jun"
            if fecha.mes == 7:
                usuario_websocket["mes"]="Jul"
            if fecha.mes == 8:
                usuario_websocket["mes"]="Ago"
            if fecha.mes == 9:
                usuario_websocket["mes"]="Sep"
            if fecha.mes == 10:
                usuario_websocket["mes"]="Oct"
            if fecha.mes == 11:
                usuario_websocket["mes"]="Nov"
            if fecha.mes == 12:
                usuario_websocket["mes"]="Dic"
            usuario_websocket["dinero"]=usuario.dinero
            usuario_websocket["almacen"]=usuario.almacen
            # await manager.send_personal_message(str(usuario_websocket), usuario.id)

            for connection in manager.active_connections:
                print("id:")
                print(connection["clientid"].replace("{", "").replace("}", "").replace("$", ""))
                if connection["clientid"].replace("{", "").replace("}", "").replace("$", "") == usuario.id:
                    print(connection["clientid"].replace("{", "").replace("}", "").replace("$", ""))
                    await connection["websocket"].send_text(str(usuario_websocket))   
        print(mensajes)
        listaEliminarMensajes=[]
        for index, mensaje in enumerate(mensajes):
            for usuario in listaUsuarios:
                if mensaje["usuarioRival"]==usuario.nombre:
                    for connection in manager.active_connections:
                        print("id:")
                        print(connection["clientid"].replace("{", "").replace("}", "").replace("$", ""))
                        if connection["clientid"].replace("{", "").replace("}", "").replace("$", "") == usuario.id:
                            print(connection["clientid"].replace("{", "").replace("}", "").replace("$", ""))
                            print("mensaje")
                            await connection["websocket"].send_text(str(mensaje))
                            listaEliminarMensajes.append(index)
        
        for index in listaEliminarMensajes:
            mensajes.pop(index)

        print(mensajes)

        

                


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    print("saveid")
    print(client_id)
    await manager.connect(websocket, client_id)
    try:
        await websocket.receive_text()  # Puedes usar esto para mantener la conexión abierta
    except WebSocketDisconnect:
        manager.disconnect(websocket)

# Inicia la tarea periódica
loop = asyncio.get_event_loop()
loop.create_task(periodic_broadcast())



def loop_dinero():
    while True:
            
        time.sleep(20)

        for usuario in listaUsuarios:
            if "Xisco"==str(usuario.nombre):
                break
        print("si")
            
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        asyncio.run(manager.broadcast(f"{usuario.dinero}"))
        loop.close()
            # await manager.broadcast(f"{usuario.dinero}")
        print("si")
         

    
# Define una función asincrónica que ejecuta manager.broadcast
""" async def broadcast_periodically():
    
        
        for usuario in listaUsuarios:
            if "Xisco"==str(usuario.nombre):
                break
        print(usuario.dinero)
        await manager.broadcast(f"{usuario.dinero}") """
        


@app.get("/usuarios")
async def usuarios():

    for usuario in listaUsuarios:
        usuario.mostrar_informacion()

    return usuario.mostrar_informacion()



@app.get("/crearUsuario/")
async def crearUsuario(usuario: str, user: usuarioo = Depends(current_user)):
    usuario_objeto=Usuario(nombre=usuario,bbdd=db_manager)
    # usuariojson = json.dumps(usuario_objeto.__dict__)

    # Convertir el objeto a un diccionario
    usuario_dict = usuario_objeto.__dict__

    # Convertir el diccionario a JSON
    usuario_json = json.dumps(usuario_dict)

    # Deserializar el JSON de nuevo a un diccionario
    usuario_dict = json.loads(usuario_json)

    # Insertar el diccionario en la base de datos
    db_manager.rellenarusuario(usuario_dict)
    return usuario_dict

"""     usuario_objeto=Usuario(nombre=usuario,bbdd=db_manager)
    listaUsuarios.append(usuario_objeto)   
    print(listaUsuarios)
    print(user) 
    return usuario_objeto"""
    

@app.get("/obtenerUsuario/")
async def crearUsuario(usuarioname: str, user: usuarioo = Depends(current_user)):

    
    Datosuser = db_manager.obtener_usuario(usuarioname)

    usuario_objeto=Usuario(nombre=Datosuser["nombre"],bbdd=db_manager)
    for indexciudad, ciudad in enumerate(Datosuser["listaciudades"]):
        usuario_objeto.crear_ciudad(nombreciudad=ciudad["nombre"],bbdd=db_manager)

        for indextiendas, tienda in enumerate(ciudad["listatiendas"]):
            usuario_objeto.comprar_tienda(nombreciudad=ciudad["nombre"],nombretienda=tienda["nombre"],bbdd=db_manager)
            
            for indexproductos, producto in enumerate(tienda["arrayProductos"]):
                usuario_objeto.agregar_producto(nombreciudad=ciudad["nombre"],nombretienda=tienda["nombre"],tipoproducto=producto["tipo"])
            
            for indexempleadostiendas, empleado in enumerate(tienda["arrayEmpleados"]):
                usuario_objeto.contratarempleado(nombreciudad=ciudad["nombre"],lugar=tienda["nombre"],nombreempleado=empleado["nombre"],bbdd=db_manager)
                usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].listaempleados[indexempleadostiendas].nombre=empleado["nombre"]          
                usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].listaempleados[indexempleadostiendas].productividad=empleado["productividad"]  
                usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].listaempleados[indexempleadostiendas].precio=empleado["precio"]  
                usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].listaempleados[indexempleadostiendas].comunicacion=empleado["comunicacion"]
                usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].listaempleados[indexempleadostiendas].estudios=empleado["estudios"]
                usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].listaempleados[indexempleadostiendas].fuerza=empleado["fuerza"]
                usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].listaempleados[indexempleadostiendas].liderazgo=empleado["liderazgo"]

            usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].nombre=tienda["nombre"]
            usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].tamaño=tienda["tamaño"]
            usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].precio=tienda["precio"]
            usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].numeroEmpleados=tienda["numeroEmpleados"]
            usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].numeroMaximoEmpleados=tienda["numeroMaximoEmpleados"]
            usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].indiceproduccionempleados=tienda["indiceproduccionempleados"]
            usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].indiceTiempo=tienda["indiceTiempo"]
            usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].indiceVariedadProductos=tienda["indiceVariedadProductos"]
            usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].ciudadtienda=tienda["ciudadtienda"]
            usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].indiceproductividadempleados=tienda["indiceproductividadempleados"]
            usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].seguridad=tienda["seguridad"]
            usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].maximaSeguridad=tienda["maximaSeguridad"]
            usuario_objeto.listaciudades[indexciudad].listatiendas[indextiendas].indiceMaximoTiempo=tienda["indiceMaximoTiempo"]
            
        
        for indexParcelas, parcela in enumerate(ciudad["listaparcelas"]):
            usuario_objeto.comprar_parcela(nombreciudad=ciudad["nombre"],nombreparcela=parcela["nombre"],bbdd=db_manager)
            
            for indexplantacion, plantacion in enumerate(parcela["listaplantacion"]):
                usuario_objeto.modificar_plantacion(indice=indexplantacion,nombreciudad=ciudad["nombre"],nombreparcela=parcela["nombre"],tipoplantacion=plantacion["tipo"],bbdd=db_manager)
                usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaplantacion[indexplantacion].factormultiplicacion=plantacion["factormultiplicacion"]
                usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaplantacion[indexplantacion].produccionmes=plantacion["produccionmes"]
                usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaplantacion[indexplantacion].urlicono=plantacion["urlicono"]



            for indexempleadosparcela, empleado in enumerate(parcela["listaempleados"]):
                usuario_objeto.contratarempleado(nombreciudad=ciudad["nombre"],lugar=parcela["nombre"],nombreempleado=empleado["nombre"],bbdd=db_manager)
                usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaempleados[indexempleadosparcela].nombre=empleado["nombre"]          
                usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaempleados[indexempleadosparcela].productividad=empleado["productividad"]  
                usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaempleados[indexempleadosparcela].precio=empleado["precio"]  
                usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaempleados[indexempleadosparcela].comunicacion=empleado["comunicacion"]
                usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaempleados[indexempleadosparcela].estudios=empleado["estudios"]
                usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaempleados[indexempleadosparcela].fuerza=empleado["fuerza"]
                usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaempleados[indexempleadosparcela].liderazgo=empleado["liderazgo"]

            usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].nombre=parcela["nombre"]
            usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].tamaño=parcela["tamaño"]
            usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].precio=parcela["precio"]
            usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].numeroEmpleados=parcela["numeroEmpleados"]
            usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].numeroMaximoEmpleados=parcela["numeroMaximoEmpleados"]
            usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].indiceproduccionempleados=parcela["indiceproduccionempleados"]
            usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].factorMultiplicacionProducto=parcela["factorMultiplicacionProducto"]
            usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].calidadterreno=parcela["calidadterreno"]
            usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].ciudadParcela=parcela["ciudadParcela"]
            usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].indiceproductividadempleados=parcela["indiceproductividadempleados"]
            usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].seguridad=parcela["seguridad"]
            usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].maximaSeguridad=parcela["maximaSeguridad"]    
        ciudadCasa= ciudad["casa"]
        if ciudadCasa != "":
            usuario_objeto.comprar_casa(nombreciudad=ciudad["nombre"],nombrecasa=ciudadCasa["nombre"],bbdd=db_manager)
            usuario_objeto.listaciudades[indexciudad].casa.precio=ciudadCasa["precio"]
            usuario_objeto.listaciudades[indexciudad].casa.prestigio=ciudadCasa["prestigio"]
            usuario_objeto.listaciudades[indexciudad].casa.seguridad=ciudadCasa["seguridad"]
        
        usuario_objeto.listaciudades[indexciudad].idioma_principal=ciudad["idioma_principal"]
        usuario_objeto.listaciudades[indexciudad].poblacion=ciudad["poblacion"]
        usuario_objeto.listaciudades[indexciudad].factorMultiplicacionProducto=ciudad["factorMultiplicacionProducto"]
        usuario_objeto.listaciudades[indexciudad].prestigioCasa=ciudad["prestigioCasa"]

    usuario_objeto.prestigio=Datosuser["prestigio"]
    usuario_objeto.dinero=Datosuser["dinero"]
    usuario_objeto.almacen=Datosuser["almacen"]
    usuario_objeto.id=str(Datosuser["_id"])
    usuario_objeto.mostrar_informacion()
    listaUsuarios.append(usuario_objeto)
    return usuario_objeto

@app.get("/obtenerUsuarios/")
async def obtenerUsuarios(usuarioname: str, user: usuarioo = Depends(current_user)):

    for usuario_objeto in listaUsuarios:
        if usuario_objeto.nombre==usuarioname:
            break
    return usuario_objeto

@app.get("/comprarParcela/")
async def comprarParcela(nombreUsuario:str, nombreCiudad: str,nombreParcela:str,precio:int):
    
    for usuario in listaUsuarios:
        if nombreUsuario==str(usuario.nombre):
            break

    if usuario.dinero > precio:   
        usuario.comprar_parcela(nombreciudad=nombreCiudad,nombreparcela=nombreParcela,bbdd=db_manager)
        db_manager.cambiar_propietario_parcela(nombre_ciudad=nombreCiudad,nombre_parcela=nombreParcela,nombre_usuario=usuario.nombre)
        db_manager.updateusuario(usuario)
        return {"mensaje":"Parcela comprada con exito"}
    else:
        return {"mensaje":"No tienes suficiente dinero para comprar la parcela"}

@app.get("/modificarPlantacion/")
async def modificarPlantacion(nombreUsuario:str, nombreCiudad: str,nombreParcela:str, arrayPlantacion:str):
    arrayPlantacion = arrayPlantacion.split(",")
    for usuario in listaUsuarios:
        if nombreUsuario==str(usuario.nombre):
            break   
    for index, plantacion in enumerate(arrayPlantacion):
        print(plantacion)
        usuario.modificar_plantacion(indice=index, nombreciudad=nombreCiudad,nombreparcela=nombreParcela,tipoplantacion=plantacion, bbdd=db_manager)
    db_manager.updateusuario(usuario)
    return {"mensaje":"Plantaciones modificadas con exito"}

@app.get("/comprarTienda/")
async def comprarTienda(nombreUsuario:str, nombreCiudad: str,nombreTienda:str):
    for usuario in listaUsuarios:
        if nombreUsuario==str(usuario.nombre):
            break   
    usuario.comprar_tienda(nombreciudad=nombreCiudad,nombretienda=nombreTienda,bbdd=db_manager)
    db_manager.cambiar_propietario_tienda(nombreCiudad, nombreTienda, usuario.nombre)
    return {"mensaje":"Tienda comprada con exito"}

@app.get("/agregarProducto/")
async def agregarProducto(nombreUsuario:str, nombreCiudad: str,nombreTienda:str, tipoProducto:str):
    for usuario in listaUsuarios:
        if nombreUsuario==str(usuario.nombre):
            break
    usuario.agregar_producto(nombreciudad=nombreCiudad,nombretienda=nombreTienda,tipoproducto=tipoProducto)
    return usuario

@app.get("/modificarProductos/")
async def modificarProductos(nombreUsuario:str, nombreCiudad: str,nombreTienda:str, arrayProductos:str):
    arrayProductos = arrayProductos.split(",")
    for usuario in listaUsuarios:
        if nombreUsuario==str(usuario.nombre):
            break   
    for index, producto in enumerate(arrayProductos):
        usuario.modificar_producto(indice=index, nombreciudad=nombreCiudad,nombreparcela=nombreTienda,tipoproducto=producto, bbdd=db_manager)
    db_manager.updateusuario(usuario)
    return {"mensaje":"Productos modificados con exito"}

@app.get("/contratarEmpleado/")
async def contratarEmpleado(nombreUsuario:str, nombreCiudad: str,Lugar:str, nombreEmpleado:str):
    for usuario in listaUsuarios:
        if nombreUsuario==str(usuario.nombre):
            break   
    usuario.contratarempleado(nombreciudad=nombreCiudad,lugar=Lugar,nombreempleado=nombreEmpleado, bbdd=db_manager)
    db_manager.cambiar_jefe_empleado(nombreCiudad, nombreEmpleado,  usuario.nombre, Lugar)
    db_manager.updateusuario(usuario)
    return {"mensaje":"Empleado contratado con exito"}

@app.get("/obtenerEmpleadosParados/")
async def obtenerEmpleadosParados(nombreCiudad: str):
    return db_manager.obtenerEmpleadosParados(nombreCiudad)

@app.get("/despedirEmpleado/")
async def contratarEmpleado(nombreUsuario:str, nombreCiudad: str,Lugar:str, nombreEmpleado:str):
    db_manager = DatabaseManager(pathBBDD)
    for usuario in listaUsuarios:
        if nombreUsuario==str(usuario.nombre):
            break   
    usuario.despedirempleado(nombreciudad=nombreCiudad,lugar=Lugar,nombreempleado=nombreEmpleado)
    db_manager.cambiar_jefe_empleado(nombreCiudad, nombreEmpleado,  "SinJefe", "Libre")
    return {"mensaje":"Empleado despedido con exito"}

@app.get("/comprarCasa/")
async def comprarCasa(nombreUsuario:str, nombreCiudad: str,nombreCasa:str,precio:int):
    
    for usuario in listaUsuarios:
        if nombreUsuario==str(usuario.nombre):
            break

    if usuario.dinero > precio:
        usuario.crear_ciudad(nombreciudad=nombreCiudad,bbdd=db_manager)   
        usuario.comprar_casa(nombreciudad=nombreCiudad,nombrecasa=nombreCasa,bbdd=db_manager)
        db_manager.cambiar_propietario_casa(nombreCiudad, nombreCasa,  usuario.nombre)
        return {"mensaje":"Casa comprada con exito"}
    else:
        return {"mensaje":"No tienes suficiente dinero para comprar la casa"}
    

@app.get("/CoordenadasCiudad/")
async def CoordenadasCiudad(nombreCiudad: str):
    return db_manager.leer_ciudad(nombreCiudad)


@app.get("/Parcelas/")
async def leerparcelas(ciudad,nombreUsuario):

    parcelas=db_manager.leer_parcelas(ciudad,nombreUsuario)
    print("parcela")
    print(parcelas)
    return parcelas


@app.get("/obtenerParcelaPropietario/")
async def leerparcelas(nombreCiudad,nombreParcela,nombreUsuario):
    return db_manager.leer_parcelasPropia(nombreCiudad,nombreParcela,nombreUsuario)

@app.get("/obtenerParcelaItems/")
async def obtenerParcelaItems(nombreCiudad,nombreParcela,nombreUsuario):
    selects=[]
    parcela=db_manager.leer_parcelasPropia(nombreCiudad,nombreParcela,nombreUsuario)
    print("parcela.listaplantacion")
    for producto in parcela['listaplantacion']:
        item={"nombre": producto['tipo'], "urlicono": producto['urlicono']}
        print(item)
        selects.append(item)

    print(selects)
    return selects

@app.get("/obtenerTiendaItems/")
async def obtenerTiendaItems(nombreCiudad,nombreTienda,nombreUsuario):
    selects=[]
    tienda=db_manager.leerTiendaPropia(nombreCiudad,nombreTienda,nombreUsuario)
    for producto in tienda['arrayproductos']:
        item={"nombre": producto['tipo'], "urlicono": producto['urlicono']}
        selects.append(item)
    return selects

@app.get("/obtenerParcelaRival/")
async def obtenerParcelaRival(nombreCiudad,nombreParcela,nombreUsuario):
    return db_manager.leer_parcelasRival(nombreCiudad,nombreParcela,nombreUsuario)

@app.get("/obtenerCasaPropietario/")
async def obtenerCasaPropietario(nombreCiudad,nombreCasa,nombreUsuario):
    return db_manager.leerCasaPropia(nombreCiudad,nombreCasa,nombreUsuario)

@app.get("/obtenerCasaRival/")
async def obtenerCasaRival(nombreCiudad,nombreCasa,nombreUsuario):
    return db_manager.leerCasaRival(nombreCiudad,nombreCasa,nombreUsuario)

@app.get("/obtenerTiendaPropietario/")
async def obtenerTiendaPropietario(nombreCiudad,nombreTienda,nombreUsuario):
    return db_manager.leerTiendaPropia(nombreCiudad,nombreTienda,nombreUsuario)

@app.get("/obtenerTiendaRival/")
async def obtenerParcelaRival(nombreCiudad,nombreTienda,nombreUsuario):
    return db_manager.leerTiendaRival(nombreCiudad,nombreTienda,nombreUsuario)

@app.get("/RobarParcela/")
async def leerparcelas(nombreUsuario,nombreCiudad,nombreParcela,nombreUsuarioRival):
    mensaje={
        "IDMessage":"RoboParcela",
        "mensaje": "",
        "usuarioRival": "",
        "usuario":"",
        "nombreciudad":"",
        "lugar":"",
        }
    print(nombreUsuario,nombreCiudad,nombreParcela,nombreUsuarioRival)
    mensajeRobo=""
    lista_produccion = []
    roboOK=False
    for usuario in listaUsuarios:
        if usuario.nombre == nombreUsuarioRival:    
            for ciudad in usuario.listaciudades:
                if ciudad.nombre == nombreCiudad:
                    for parcela in ciudad.listaparcelas:
                        if parcela.nombre == nombreParcela: 
                            if  random.uniform(0, 4.5) > parcela.seguridad:
                                parcela.habilitacionproduccionmes=False
                                for plantacion in parcela.listaplantacion:  
                                    produccion = {}  # Crear un nuevo diccionario para cada plantación   
                                    produccion["tipo"] = plantacion.tipo
                                    produccion["numero"] = 1 * plantacion.factormultiplicacion * plantacion.produccionmes[fecha.mes] * parcela.indiceproduccionempleados * parcela.calidadterreno * parcela.indiceproductividadempleados
                                    print(produccion["numero"], "random_anual", plantacion.factormultiplicacion, plantacion.produccionmes[fecha.mes], parcela.indiceproduccionempleados, parcela.calidadterreno, parcela.indiceproductividadempleados)
                                    lista_produccion.append(produccion)
                                    mensajeRobo=mensajeRobo+str(produccion["numero"])+" de "+produccion["tipo"]+". "
                                mensajeRobo="Robo con exito, has conseguido "+mensajeRobo
                                roboOK=True
                                mensaje["mensaje"]="El contrincante "+nombreUsuario+" te ha robado en "+nombreParcela+" del municipio de "+nombreCiudad+": "+mensajeRobo
                            else:
                                mensajeRobo="Te han pillado robando, vas a tener una multa de "+ str(multaRobo)
                                for usuario in listaUsuarios:
                                    if usuario.nombre == nombreUsuario:
                                        usuario.dinero=-multaRobo
                                mensaje["mensaje"]="El contrincante "+nombreUsuario+" te ha intentado robar en "+nombreParcela+" del municipio de "+nombreCiudad+". La policia le ha pillado."
                            break
                        
    if roboOK==True:
        for usuario in listaUsuarios:
            if usuario.nombre == nombreUsuario:
                for producto in lista_produccion:
                    elemento = {}  
                    for idx, elemento in enumerate(usuario.almacen):
                        if elemento["tipo"] == producto["tipo"]:
                            elemento["numero"] = elemento["numero"] + producto["numero"]
                            usuario.almacen[idx]["numero"] = elemento["numero"]

    mensaje["usuarioRival"]=nombreUsuarioRival
    mensaje["usuario"]=nombreUsuario
    mensaje["nombreciudad"]=nombreCiudad
    mensaje["lugar"]=nombreParcela
    mensajes.append(mensaje)
    print(mensajes)             
    
    if roboOK==True:
        return {"mensaje":mensajeRobo,"resultado":True}
    else:
        usuario.dinero=usuario.dinero-cantidadMultaRoboParcela
        return {"mensaje":"La policia te ha pillado robandp la parcela. Te han multado con 15000 euros","resultado":False}



@app.get("/RobarCasa/")
async def RobarCasa(nombreUsuario,nombreCiudad,nombreCasa,nombreUsuarioRival):
    mensaje={
        "IDMessage":"RoboCasa",
        "mensaje": "",
        "usuarioRival": "",
        "usuario":"",
        "nombreciudad":"",
        "casa":"",
        }
    mensajeRobo=""
    for usuario in listaUsuarios:
        if usuario.nombre == nombreUsuarioRival:    
            for ciudad in usuario.listaciudades:
                if ciudad.nombre == nombreCiudad:
                    if  random.uniform(0, 4.5) > ciudad.casa.seguridad:
                        cantidadRobo=random.uniform(minimoRoboCasa, maximoRoboCasa)
                        usuario.dinero=-cantidadRobo
                        mensajeRobo="Robo con exito, has conseguido "+str(cantidadRobo)
                        
                        mensaje["mensaje"]="El contrincante "+nombreUsuario+" te ha robado en "+nombreCasa+" del municipio de "+nombreCiudad+" una cantidad de "+str(cantidadRobo)+" Euros."
                    else:
                        mensajeRobo="Te han pillado robando, vas a tener una multa de "+ str(multaRobo)
                        for usuario in listaUsuarios:
                            if usuario.nombre == nombreUsuario:
                                usuario.dinero=-multaRobo
                        mensaje["mensaje"]="El contrincante "+nombreUsuario+" te ha intentado robar en "+nombreCasa+" del municipio de "+nombreCiudad+". La policia le ha pillado."
                    break

    
    mensaje["usuarioRival"]=nombreUsuarioRival
    mensaje["usuario"]=nombreUsuario
    mensaje["nombreciudad"]=nombreCiudad
    mensaje["casa"]=nombreCasa
    mensajes.append(mensaje)
    print(mensajes)                
    
    return mensaje

@app.get("/RobarTienda/")
async def RobarTienda(nombreUsuario,nombreCiudad,nombreTienda,nombreUsuarioRival):
    roboOK=False
    mensaje={
        "IDMessage":"RoboTienda",
        "mensaje": "",
        "usuarioRival": "",
        "usuario":"",
        "nombreciudad":"",
        "tienda":"",
        }
    print(nombreUsuario,nombreCiudad,nombreTienda,nombreUsuarioRival)
    mensajeRobo=""

    for usuario in listaUsuarios:
        if usuario.nombre == nombreUsuarioRival:    
            for ciudad in usuario.listaciudades:
                if ciudad.nombre == nombreCiudad:
                    for tienda in ciudad.listatiendas:
                        if tienda.nombre == nombreTienda: 
                            if  random.uniform(0, 4.5) > tienda.seguridad:
                                cantidadRobo=random.uniform(minimoRoboCasa, maximoRoboCasa)
                                usuario.dinero=-cantidadRobo
                                mensajeRobo="Robo con exito, has conseguido "+str(cantidadRobo)
                                roboOK=True
                                mensaje["mensaje"]="El contrincante "+nombreUsuario+" te ha robado en "+nombreTienda+" del municipio de "+nombreCiudad+" una cantidad de "+str(cantidadRobo)+" Euros."
                            else:
                                mensajeRobo="Te han pillado robando, vas a tener una multa de "+ str(multaRobo)
                                for usuario in listaUsuarios:
                                    if usuario.nombre == nombreUsuario:
                                        usuario.dinero=-multaRobo
                                mensaje["mensaje"]="El contrincante "+nombreUsuario+" te ha intentado robar en "+nombreTienda+" del municipio de "+nombreCiudad+". La policia le ha pillado."
                            break

    
    mensaje["usuarioRival"]=nombreUsuarioRival
    mensaje["usuario"]=nombreUsuario
    mensaje["nombreciudad"]=nombreCiudad
    mensaje["tienda"]=nombreTienda
    mensajes.append(mensaje)
    print(mensajes)                
    
    if roboOK==True:
        return {"mensaje":mensajeRobo,"resultado":True}
    else:
        usuario.dinero=usuario.dinero-cantidadMultaRoboTienda
        return {"mensaje":mensajeRobo,"resultado":False}

@app.get("/OfertaParcela/")
async def OfertaParcela(nombreUsuario,nombreCiudad,nombreParcela,nombreUsuarioRival,oferta):
    mensaje={
        "IDMessage":"",
        "mensaje": "",
        "usuarioRival": "",
        "usuario":"",
        "nombreciudad":"",
        "lugar":"",
        "oferta":0,
        }
     
    mensaje["mensaje"]="El contrincante "+nombreUsuario+" te ha realizado una oferta por la "+nombreParcela+" de municipio de "+nombreCiudad+" por "+str(oferta)+" Euros"
    mensaje["usuarioRival"]=nombreUsuarioRival
    mensaje["usuario"]=nombreUsuario
    mensaje["IDMessage"]="Oferta"
    mensaje["nombreciudad"]=nombreCiudad
    mensaje["lugar"]=nombreParcela
    mensaje["oferta"]=oferta
    mensajes.append(mensaje)
    return {"mensaje":"Oferta enviada correctamente"} 

@app.get("/OfertaTienda")
async def OfertaTienda(nombreUsuario,nombreCiudad,nombreTienda,nombreUsuarioRival,oferta):
    mensaje={
        "IDMessage":"",
        "mensaje": "",
        "usuarioRival": "",
        "usuario":"",
        "nombreciudad":"",
        "lugar":"",
        "oferta":0,
        }
     
    mensaje["mensaje"]="El contrincante "+nombreUsuario+" te ha realizado una oferta por la "+nombreTienda+" de municipio de "+nombreCiudad+" por "+str(oferta)+" Euros"
    mensaje["usuarioRival"]=nombreUsuarioRival
    mensaje["usuario"]=nombreUsuario
    mensaje["IDMessage"]="Oferta"
    mensaje["nombreciudad"]=nombreCiudad
    mensaje["lugar"]=nombreTienda
    mensaje["oferta"]=oferta
    mensajes.append(mensaje)
    print(mensajes)
    return {"mensaje":"Oferta enviada correctamente"} 

@app.get("/aceptarOferta/")
async def aceptarOferta(nombreUsuario,usuarioRival,nombreCiudad,lugar,oferta):
    tipo=""
    for usuario in listaUsuarios:
        if nombreUsuario==str(usuario.nombre):
            break
    
    if usuario.dinero>oferta:
        print(nombreUsuario,usuarioRival,nombreCiudad,lugar,oferta)
        for usuario in listaUsuarios:
            if usuario.nombre==usuarioRival:
                for ciudad in usuario.listaciudades:
                    if ciudad.nombre==nombreCiudad:
                        for parcela in ciudad.listaparcelas:
                            if parcela.nombre == lugar:
                                db_manager.cambiar_propietario_parcela(nombreCiudad, lugar, nombreUsuario)
                                for empleado in parcela.listaempleados:
                                    db_manager.cambiar_jefe_empleado( nombreCiudad, empleado.nombre,  nombreUsuario, lugar)
                                tipo="parcela"
                                break
                        for tienda in ciudad.listatiendas:
                            if tienda.nombre == lugar:
                                db_manager.cambiar_propietario_tienda(nombreCiudad, lugar, nombreUsuario)
                                for empleado in parcela.listaempleados:
                                    db_manager.cambiar_jefe_empleado( nombreCiudad, empleado.nombre,  nombreUsuario, lugar)
                                tipo="tienda"
                                break
        

        for Rival in listaUsuarios:
            if usuarioRival==str(Rival.nombre):
                Rival.dinero=+int(oferta)
                break  
        
        for usuario in listaUsuarios:
            if nombreUsuario==str(usuario.nombre):
                usuario.dinero=-int(oferta)
                break


        if tipo == "parcela":        
            parcela=Rival.eliminar_obtener_parcela(nombreciudad=nombreCiudad,nombreparcela=lugar) 
            usuario.añadir_parcela(nombreCiudad,parcela)

        if tipo == "tienda":        
            tienda=Rival.eliminar_obtener_tienda(nombreciudad=nombreCiudad,nombretienda=lugar) 
            usuario.añadir_tienda(nombreCiudad,tienda)


        for Rival in listaUsuarios:
            if usuarioRival==str(Rival.nombre):
                break  
        
        for usuario in listaUsuarios:
            if nombreUsuario==str(usuario.nombre):
                break


        db_manager.updateusuario(usuario)
        db_manager.updateusuario(Rival) 
        usuario.mostrar_informacion()
        Rival.mostrar_informacion()
        # db_manager.cambiarPropiedad(nombreUsuario,usuarioRival,nombreCiudad,lugar,tipo)

        mensajeAceptadaOferta={
            "IDMessage":"OfertaRespuesta",
            "mensaje":"El contrincante "+nombreUsuario+" ha aceptado la oferta por la "+lugar+" de municipio de "+nombreCiudad,
            "usuarioRival": usuarioRival,
            "usuario":nombreUsuario,
            "nombreciudad":nombreCiudad,
            "lugar":lugar,
            "aceptada":"aceptada"
            }
        mensajes.append(mensajeAceptadaOferta)
        return {"mensaje":"Oferta aceptada","aceptada":True}
    else:
        return {"mensaje":"No tienes suficiente dinero para aceptar la oferta","aceptada":False}

@app.get("/rechazarOferta/")
async def rechazarOferta(nombreUsuario,usuarioRival,nombreCiudad,lugar,oferta):
    mensajeRechazoOferta={
        "IDMessage":"OfertaRespuesta",
        "mensaje":"El contrincante "+usuarioRival+" ha rechazado la oferta por la "+lugar+" de municipio de "+nombreCiudad,
        "usuarioRival": nombreUsuario,
        "usuario":usuarioRival,
        "nombreciudad":nombreCiudad,
        "lugar":lugar,
        "aceptada":"rechazada"
        }
    mensajes.append(mensajeRechazoOferta)
    return {"mensaje":"Oferta rechazada"}


@app.get("/EspiarParcela/")
async def EspiarParcela(nombreCiudad,nombreParcela,nombreUsuarioRival):
    print(nombreCiudad,nombreParcela,nombreUsuarioRival)
    for usuario in listaUsuarios:
        if usuario.nombre == nombreUsuarioRival:    
            for ciudad in usuario.listaciudades:
                if ciudad.nombre == nombreCiudad:
                    for parcela in ciudad.listaparcelas:
                        if parcela.nombre == nombreParcela:
                            if random.uniform(0, 1)  > 0.5:  
                                return {"parcela":parcela,"mensaje":"Espionaje con exito","resultado":True}
    usuario.dinero=usuario.dinero-cantidadMultaParcela
    return {"parcela":parcela,"mensaje":"La policia te ha pillado espiando la parcela. Te han multado con 5000 euros","resultado":False}

@app.get("/EspiarCasa/")
async def EspiarCasa(nombreCiudad,nombreCasa,nombreUsuarioRival):
    print(nombreCiudad,nombreCasa,nombreUsuarioRival)
    for usuario in listaUsuarios:
        if usuario.nombre == nombreUsuarioRival:    
            for ciudad in usuario.listaciudades:
                if 1*random.uniform(0.5, 1)  > 0.5:  #revisar
                    return ciudad.casa
    return None

@app.get("/EspiarTienda/")
async def EspiarTienda(nombreCiudad,nombreTienda,nombreUsuarioRival):
    print(nombreCiudad,nombreTienda,nombreUsuarioRival)
    for usuario in listaUsuarios:
        if usuario.nombre == nombreUsuarioRival:    
            for ciudad in usuario.listaciudades:
                if ciudad.nombre == nombreCiudad:
                    for tienda in ciudad.listatiendas:
                        if tienda.nombre == nombreTienda:
                            if random.uniform(0, 1)  > 0.5:  
                                return {"tienda":tienda,"mensaje":"Espionaje con exito","resultado":True}
    usuario.dinero=usuario.dinero-cantidadMultaTienda
    return {"tienda":tienda,"mensaje":"La policia te ha pillado espiando la tienda. Te han multado con 5000 euros","resultado":False}


@app.get("/Fruterias/")
async def leerfruterias(ciudad,nombreUsuario):
    return db_manager.leer_fruterias(ciudad,nombreUsuario)

@app.get("/Casas/")
async def leercasas(ciudad,nombreUsuario):
    return db_manager.leer_casas(ciudad,nombreUsuario)

@app.get("/ciudades/")
async def leerciudades():    
    ciudades=db_manager.leer_ciudades()
    return (ciudades) 

@app.get("/ciudadesUsuario/")
async def leerciudades(nombreCiudad,nombreUsuario):    
    ciudades={"resultado":db_manager.leer_ciudades_usuario(nombreUsuario,nombreCiudad)}
    return (ciudades) 

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    print(form.username)
    user_db = db_manager.buscar_usuario(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    ID_Usuario = db_manager.buscar_IDusuario(form.username)
    print(user_db['_id'])
    if not crypt.verify(form.password, user_db["password"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")

    access_token = {"sub": user_db["nombre"],
                    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}
    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer", "user_id": ID_Usuario}

@app.get("/registrarse/")
async def registrarse(nombreUsuario:str,contrasena:str):
    mensaje={"mensaje":db_manager.registrarse(nombreUsuario,crypt.hash(contrasena))}
    
    return mensaje
    

@app.get("/getItemsPlantaciones/")
async def getItemsPlantaciones():
    return db_manager.getItemsPlantaciones()

@app.get("/incrementarSeguridad/")
async def incrementarSeguridad(nombreUsuario:str, nombreCiudad: str,Lugar:str, indice:int,precio:int):
    if usuario.dinero > precio:
        for usuario in listaUsuarios:
            if nombreUsuario==str(usuario.nombre):
                break   
        usuario.cambiarSeguridad(nombreciudad=nombreCiudad,lugar=Lugar,indice=indice)
        return {"mensaje":"Se ha mejorado la seguridad"}
    else:
        return {"mensaje":"No tienes suficiente dinero para mejorar la seguridad"}

@app.get("/incrementarCalidadTerreno/")
async def incrementarSeguridad(nombreUsuario:str, nombreCiudad: str,Lugar:str, indice:int,precio:int):
    if usuario.dinero > precio:
        for usuario in listaUsuarios:
            if nombreUsuario==str(usuario.nombre):
                break   
        usuario.incrementarCalidadTerreno(nombreciudad=nombreCiudad,lugar=Lugar,indice=indice)
        return {"mensaje":"Se ha mejorado la calidad del terreno"}
    else:
        return {"mensaje":"No tienes suficiente dinero para mejorar la calidad del terreno"}
    

@app.get("/users/me")
async def me(user: usuarioo = Depends(current_user)):
    print("user")
    return user

@app.get("/actualizarclasificacion/")
async def actualizarclasificacion():
    clasificacion = []  # Inicializa una lista vacía

    for usuario in listaUsuarios:
        posicion = {
            "nombre": usuario.nombre,
            "dinero": usuario.dinero,
            "iniciales": usuario.nombre[:2],
        }
        clasificacion.append(posicion)

        # Ordena la lista por el valor de 'dinero' en orden descendente
    clasificacion = sorted(clasificacion, key=lambda x: x['dinero'], reverse=True)
    
    print(clasificacion)
    return clasificacion

""" 
@app.get("/comprarEmpresaElectronica/")
async def comprarEmpresaElectronica(nombreUsuario:str, nombreCiudad: str,nombreEmpresa:str):
    db_manager = DatabaseManager(pathBBDD)
    for usuario in listaUsuarios:
        if nombreUsuario==str(usuario.nombre):
            break
    usuario.crear_ciudad(nombreciudad=nombreCiudad,bbdd=db_manager)   
    usuario.comprar_empresaelectronica(nombreciudad=nombreCiudad,nombreempresa=nombreEmpresa,bbdd=db_manager)
    db_manager.cerrar_conexion()
    return usuario

@app.get("/contratarEmpleadoElectronica/")
async def contratarEmpleadoElectronica(nombreUsuario:str, nombreCiudad: str,Lugar:str, nombreEmpleado:str):
    db_manager = DatabaseManager(pathBBDD)
    for usuario in listaUsuarios:
        if nombreUsuario==str(usuario.nombre):
            break   
    usuario.contratarempleado(nombreciudad=nombreCiudad,lugar=Lugar,nombreempleado=nombreEmpleado, bbdd=db_manager)
    db_manager.cerrar_conexion()
    return usuario

@app.get("/agregarProyectoElectronica/")
async def agregarProyectoElectronica(nombreUsuario:str, nombreCiudad: str,nombreEmpresaElectronica:str, nombreProyecto:str):
    for usuario in listaUsuarios:
        if nombreUsuario==str(usuario.nombre):
            break
    usuario.agregar_proyecto_electronica(nombreciudad=nombreCiudad,nombreEmpresaElectronica=nombreEmpresaElectronica,nombreProyecto=nombreProyecto)
    return usuario """

def main2():
    
    db_manager = DatabaseManager(pathBBDD)


    nombreUsuario1 = "Xisco"
    nombreUsuario2 = "Sandra"

    usuario1=Usuario(nombreUsuario1,db_manager)
    #usuario2=Usuario(nombreUsuario2,db_manager)
    listaUsuarios.append(usuario1)
    #listaUsuarios.append(usuario2)
    
    usuario1.crear_ciudad("Novelda",db_manager)
    usuario1.crear_ciudad("Utiel",db_manager)
    #usuario2.crear_ciudad("Utiel",db_manager)

    usuario1.comprar_parcela("Utiel","Parcela1",db_manager)
    #usuario2.comprar_parcela("Utiel","Parcela2",db_manager)

    usuario1.agregar_plantacion("Utiel","Parcela1","Vino",db_manager)
    usuario1.agregar_plantacion("Utiel","Parcela1","Patata",db_manager)
    usuario1.agregar_plantacion("Utiel","Parcela1","Almendros",db_manager)
    usuario1.agregar_plantacion("Utiel","Parcela1","Vino",db_manager)
    
    usuario1.contratarempleado("Utiel","Parcela1","Juan",db_manager)

    usuario1.comprar_tienda("Utiel","Tienda1",db_manager)
    #usuario2.comprar_tienda("Utiel","Tienda2",db_manager)

    usuario1.agregar_producto("Utiel","Tienda1","Vino")
    usuario1.agregar_producto("Utiel","Tienda1","Patata")
    usuario1.agregar_producto("Utiel","Tienda1","Almendros")
    usuario1.agregar_producto("Utiel","Tienda1","Vino")

    for usuario in listaUsuarios:
        usuario.mostrar_informacion()

    db_manager.cerrar_conexion()

fecha=Fecha(ano,mes)

def ejecutar_metodo(clase_instancia):

    while True:
        store=clase_instancia.incrementar(listaUsuarios,db_manager)
        time.sleep(20)


# Crear un hilo para ejecutar el método cada 20 segundos
hilo = threading.Thread(target=ejecutar_metodo, args=(fecha,))
hilo.daemon = True
hilo.start()

""" async def main():
    task = asyncio.create_task(broadcast_periodically(manager))
    # Puedes seguir realizando otras tareas aquí si es necesario
    await task

# Ejecutar el loop de eventos de asyncio
if __name__ == "__main__":
    asyncio.run(main()) """

# Mantener el programa en ejecución
""" try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    
    pass """