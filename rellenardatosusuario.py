from Usuarios import Usuario
from BBDDMongodb import DatabaseManager
import json

pathBBDD="mongodb+srv://fpratsquilez:GTdbIFamKljeyUvs@worldmanagergame.k3rozlq.mongodb.net/?retryWrites=true&w=majority"

db_manager = DatabaseManager(pathBBDD)

usuario="Sandra"

usuario_objeto=Usuario(nombre=usuario,bbdd=db_manager)
usuario_objeto.crear_ciudad(nombreciudad="Utiel",bbdd=db_manager) 
""" usuario_objeto.comprar_tienda(nombreciudad="Utiel",nombretienda="Tienda1",bbdd=db_manager) 
usuario_objeto.comprar_tienda(nombreciudad="Utiel",nombretienda="Tienda2",bbdd=db_manager) 
usuario_objeto.agregar_producto(nombreciudad="Utiel",nombretienda="Tienda2",tipoproducto="Patata")
usuario_objeto.agregar_producto(nombreciudad="Utiel",nombretienda="Tienda2",tipoproducto="Vino")
usuario_objeto.agregar_producto(nombreciudad="Utiel",nombretienda="Tienda1",tipoproducto="Patata") """
usuario_objeto.comprar_parcela(nombreciudad="Utiel",nombreparcela="Parcela2",bbdd=db_manager)
usuario_objeto.agregar_plantacion(nombreciudad="Utiel",nombreparcela="Parcela2",tipoplantacion="Vino",bbdd=db_manager)
""" usuario_objeto.agregar_plantacion(nombreciudad="Utiel",nombreparcela="Parcela1",tipoplantacion="Vino",bbdd=db_manager)
usuario_objeto.contratarempleado(nombreciudad="Utiel",lugar="Parcela1",nombreempleado="Juan",bbdd=db_manager)
usuario_objeto.comprar_casa(nombreciudad="Utiel",nombrecasa="Casa1",bbdd=db_manager)
usuario_objeto.crear_ciudad(nombreciudad="Novelda",bbdd=db_manager)  """
usuario_objeto.mostrar_informacion()
# # Convertir el objeto a un diccionario
# usuario_dict = usuario_objeto.__dict__

# # Convertir el diccionario a JSON
# usuario_json = json.dumps(usuario_dict)

# # Deserializar el JSON de nuevo a un diccionario
# usuario_dict = json.loads(usuario_json)

# Insertar el diccionario en la base de datos
usuario_dict = json.loads(usuario_objeto.mostrar_informacion())
db_manager.rellenarusuario(usuario_dict)  

""" Datosuser = db_manager.obtener_usuario(usuario)

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
            usuario_objeto.agregar_plantacion(nombreciudad=ciudad["nombre"],nombreparcela=parcela["nombre"],tipoplantacion=plantacion["tipo"],bbdd=db_manager)
            usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaplantacion[indexplantacion].factormultiplicacion=plantacion["factormultiplicacion"]
            usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaplantacion[indexplantacion].produccionmes=plantacion["produccionmes"]

        for indexempleadosparcela, empleado in enumerate(parcela["listaempleados"]):
            usuario_objeto.contratarempleado(nombreciudad=ciudad["nombre"],lugar=parcela["nombre"],nombreempleado=empleado["nombre"],bbdd=db_manager)
            usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaempleados[indexempleadosparcela].nombre=empleado["nombre"]          
            usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaempleados[indexempleadosparcela].productividad=empleado["productividad"]  
            usuario_objeto.listaciudades[indexciudad].listaparcelas[indexParcelas].listaempleados[indexempleadosparcela].precio=empleado["precio"]  

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
usuario_objeto.mostrar_informacion() """


