from Ciudad import Ciudad
import json

lista_produccion = []
lista_venta = []
produccion = {
    "tipo": str,
    "numero": int,
}
venta = {
    "tipo": str,
    "numero": int,
}
random_anual=3
prestigiobase = 0.5
maximoprestigio = 1.0
divisionprestigocasa=10
dineroinicial=200000.0
precioMejoraCalidadTerreno=12000
precioMejoraSeguridad=15000
incrementoPrestigioCasa=1

class Usuario():
    nombre:str
    def __init__(self, nombre, bbdd):
        self.nombre = nombre
        edad = bbdd.obtener_datos_usuario(nombre)
        self.edad = edad
        self.listaciudades = [] 
        self.prestigio = prestigiobase
        self.dinero = dineroinicial
        self.almacen = [
            {"tipo": "Vino", "numero": 100, "precio":20, "urlicono": 'http://localhost:8083/vino.PNG'},
            {"tipo": "Patata", "numero": 50, "precio":2, "urlicono": 'http://localhost:8083/patata.PNG'},
            {"tipo": "Almendros", "numero": 200, "precio":5, "urlicono": 'http://localhost:8083/almendras.PNG'}
        ] 
        self.id=""

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print("Ciudades:")
        arraylistaciudades = []
        for ciudad in self.listaciudades:
            arraylistaciudades.append(ciudad.mostrar_informacion())
        print(f"prestigio: {self.prestigio}")
        print(f"dinero: {self.dinero}")
        print(f"almacen: {self.almacen}")
        print(f"id: {self.id}")
        listaciudades_json = json.dumps(arraylistaciudades)
        usuario_dict = {
            "nombre": self.nombre,
            "edad": self.edad,
            "listaciudades": json.loads(listaciudades_json),
            "prestigio": self.prestigio,
            "dinero": self.dinero,
            "almacen": self.almacen,
            "id":self.id
        }
        # Convertir el diccionario a JSON
        usuario_json = json.dumps(usuario_dict)
        return usuario_json
        

    


    def crear_ciudad(self, nombreciudad,bbdd):
        ciudad=Ciudad(nombreciudad,bbdd)
        self.listaciudades.append(ciudad)

    def comprar_parcela(self, nombreciudad,nombreparcela,bbdd):
        for ciudad in self.listaciudades:
            if ciudad.nombre == nombreciudad:
                self.dinero -=ciudad.comprar_parcela(nombreparcela,bbdd)
    
    def eliminar_obtener_parcela(self, nombreciudad,nombreparcela):
        for ciudad in self.listaciudades:
            if ciudad.nombre == nombreciudad:
                return ciudad.eliminar_obtener_parcela(nombreparcela)
        return None              

    def añadir_parcela(self, nombreciudad,parcela):
        for ciudad in self.listaciudades:
            if ciudad.nombre == nombreciudad:
                ciudad.añadir_parcela(parcela)
        return 
    
    def agregar_plantacion(self, nombreciudad,nombreparcela,tipoplantacion,bbdd):
        for ciudad in self.listaciudades:
            if ciudad.nombre == nombreciudad:
                for parcela in ciudad.listaparcelas:
                    if parcela.nombre == nombreparcela:
                        parcela.agregar_plantacion(tipoplantacion,bbdd)
    
    def modificar_plantacion(self, indice, nombreciudad,nombreparcela,tipoplantacion,bbdd):
        for ciudad in self.listaciudades:
            if ciudad.nombre == nombreciudad:
                for parcela in ciudad.listaparcelas:
                    if parcela.nombre == nombreparcela:
                        parcela.modificar_plantacion(indice,tipoplantacion, bbdd)

    def modificar_producto(self, indice, nombreciudad,nombretienda,tipoproducto,bbdd):
        for ciudad in self.listaciudades:
            if ciudad.nombre == nombreciudad:
                for tienda in ciudad.listaparcelas:
                    if tienda.nombre == nombretienda:
                        tienda.modificar_producto(indice,tipoproducto, bbdd)

    def produccion(self,fecha):
        lista_produccion = []
        for ciudad in self.listaciudades:
            for parcela in ciudad.listaparcelas:
                if  parcela.habilitacionproduccionmes==True:
                    for plantacion in parcela.listaplantacion:  
                        produccion = {}  # Crear un nuevo diccionario para cada plantación   
                        produccion["tipo"] = plantacion.tipo
                        print(fecha, plantacion.tipo, parcela.nombre, ciudad.nombre)
                        print(random_anual , plantacion.produccionmes[1] )
                        produccion["numero"] = random_anual * plantacion.factormultiplicacion * plantacion.produccionmes[fecha.mes] * parcela.indiceproduccionempleados * parcela.calidadterreno * parcela.indiceproductividadempleados
                        print(produccion["numero"], random_anual, plantacion.factormultiplicacion, plantacion.produccionmes[fecha.mes], parcela.indiceproduccionempleados, parcela.calidadterreno, parcela.indiceproductividadempleados)
                        lista_produccion.append(produccion)
                    parcela.habilitacionproduccionmes==True
        return lista_produccion

    def comprar_tienda(self, nombreciudad,nombretienda,bbdd):
        for ciudad in self.listaciudades:
            if ciudad.nombre == nombreciudad:
                self.dinero -= ciudad.comprar_tienda(nombretienda,bbdd)

    def eliminar_obtener_tienda(self, nombreciudad,nombretienda):
        for ciudad in self.listaciudades:
            if ciudad.nombre == nombreciudad:
                return ciudad.eliminar_obtener_tienda(nombretienda)
        return None 
    
    def añadir_tienda(self, nombreciudad,tienda):
        for ciudad in self.listaciudades:
            if ciudad.nombre == nombreciudad:
                ciudad.añadir_tienda(tienda)
        return 
    
    def agregar_producto(self, nombreciudad,nombretienda,tipoproducto):
        for ciudad in self.listaciudades:
            if ciudad.nombre == nombreciudad:
                for tienda in ciudad.listatiendas:
                    if tienda.nombre == nombretienda:
                        tienda.agregar_producto(tipoproducto)   

    def venta(self):
        for ciudad in self.listaciudades:
            for tienda in ciudad.listatiendas:
                for producto in tienda.listaproductos:
                        venta = {}  # Crear un nuevo diccionario para cada plantación   
                        venta["tipo"] = producto.tipo
                        venta["numero"] = tienda.indiceproduccionempleados * tienda.indiceTiempo * tienda.indiceVariedadProductos * self.prestigio * tienda.indiceproductividadempleados
                        print(tienda.indiceproduccionempleados, tienda.indiceTiempo, tienda.indiceVariedadProductos, self.prestigio, tienda.indiceproductividadempleados)
                        lista_venta.append(venta)
        return lista_venta
    
    def empleados_gastos_mes(self):
        cantidadgastomensual=0.0
        for ciudad in self.listaciudades:

            for parcela in ciudad.listaparcelas:
                for empleado in parcela.listaempleados:
                    cantidadgastomensual += empleado.precio

            for tienda in ciudad.listatiendas:
                for empleado in tienda.listaempleados:
                    cantidadgastomensual += empleado.precio

        return cantidadgastomensual
    
    def incremento_prestigio_tiendas(self):
        for ciudad in self.listaciudades:
            for tienda in ciudad.listatiendas:
                tienda.incremento_prestigio_tienda()
    
    def incrementar_prestigio(self):
        if self.prestigio < maximoprestigio:
            self.prestigio =self.prestigio+ 0.02
    
    def decrementar_prestigio(self):
        if 0 < self.prestigio:
            self.prestigio =self.prestigio- 0.02

    def contratarempleado(self, nombreciudad,lugar,nombreempleado,bbdd):
        for ciudad in self.listaciudades:
            if ciudad.nombre == nombreciudad:
                for tienda in ciudad.listatiendas:
                    if tienda.nombre == lugar:
                        tienda.contratar_empleado(nombreempleado,bbdd)
                for parcela in ciudad.listaparcelas:
                    if parcela.nombre == lugar:
                        parcela.contratar_empleado(nombreempleado,bbdd)
                for empresaelectronica in ciudad.listaEmpresaElectronica:
                    if empresaelectronica.nombre == lugar:
                        empresaelectronica.contratar_empleado(nombreempleado,bbdd)

    def despedirempleado(self, nombreciudad,lugar,nombreempleado):
        for ciudad in self.listaciudades:
            if ciudad.nombre == nombreciudad:
                for tienda in ciudad.listatiendas:
                    if tienda.nombre == lugar:
                        tienda.despedir_empleado(nombreempleado)
                for parcela in ciudad.listaparcelas:
                    if parcela.nombre == lugar:
                        parcela.despedir_empleado(nombreempleado)
                for empresaelectronica in ciudad.listaEmpresaElectronica:
                    if empresaelectronica.nombre == lugar:
                        empresaelectronica.despedir_empleado(nombreempleado)
    
    def comprar_casa(self, nombreciudad,nombrecasa,bbdd):
        for ciudad in self.listaciudades:
            if ciudad.nombre == nombreciudad:
                ciudad.comprar_casa(nombrecasa,bbdd)
                # self.prestigio = self.prestigio + incrementoPrestigioCasa
                self.dinero =self.dinero-float(ciudad.casa.precio)
                    
    
    def comprar_empresaelectronica(self, nombreciudad,nombreempresa,bbdd):
        for ciudad in self.listaciudades:
            if ciudad.nombre == nombreciudad:
                self.dinero =self.dinero-float(ciudad.comprar_empresa_electronica(nombreempresa,bbdd))
        
    def agregar_proyecto_electronica(self, nombreciudad,nombreempresaelectronica,nombreproyecto):
        for ciudad in self.listaciudades:
            if ciudad.nombre == nombreciudad:
                for empreselectronica in ciudad.listaEmpresaElectronica:
                    if empreselectronica.nombre == nombreempresaelectronica:
                        empreselectronica.agregar_proyecto(nombreproyecto)   

    def cambiarSeguridad(self, nombreciudad,lugar,indice):
        for ciudad in self.listaciudades:
            if ciudad.nombre == nombreciudad:
                for tienda in ciudad.listatiendas:
                    if tienda.nombre == lugar:
                        tienda.cambiarSeguridad(indice)
                for parcela in ciudad.listaparcelas:
                    if parcela.nombre == lugar:
                        parcela.cambiarSeguridad(indice)
                for empresaelectronica in ciudad.listaEmpresaElectronica:
                    if empresaelectronica.nombre == lugar:
                        empresaelectronica.cambiarSeguridad(indice)
        self.dinero=self.dinero-float(precioMejoraSeguridad)
        
    def incrementarCalidadTerreno(self, nombreciudad,lugar,indice):
        for ciudad in self.listaciudades:
            if ciudad.nombre == nombreciudad:
                for parcela in ciudad.listaparcelas:
                    if parcela.nombre == lugar:
                        parcela.incrementarCalidadTerreno(indice)
        
        self.dinero=self.dinero-float(precioMejoraCalidadTerreno)
        