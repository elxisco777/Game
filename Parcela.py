
from Plantacion import Plantacion
from Empleados import Empleados
import random
import json

indiceNumeroMaximoEmpleados=40

class Parcela():
    def __init__(self, nombreparcela, nombreciudad, factorMultiplicacionProducto,bbdd):
        self.nombre = nombreparcela
        precio,tamaño,numeroplantaciones = bbdd.obtener_informacion_parcela(nombreparcela,nombreciudad)
        self.tamaño = tamaño
        self.precio = precio
        self.listaplantacion = []
        self.listaempleados = []
        self.factorMultiplicacionProducto = factorMultiplicacionProducto.split(",")
        self.numeroEmpleados = 0
        self.numeroMaximoEmpleados = int((tamaño*numeroplantaciones)/indiceNumeroMaximoEmpleados)
        self.indiceproduccionempleados = 1
        self.calidadterreno = int(random.uniform(0, 3))
        self.ciudadParcela = nombreciudad
        self.indiceproductividadempleados = 1
        self.seguridad = 0
        self.maximaSeguridad = 3
        self.numeroplantaciones = numeroplantaciones
        for index in range(numeroplantaciones):
            self.agregar_plantacion("Libre", bbdd)
        self.habilitacionproduccionmes=True

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Calidad Terreno: {self.calidadterreno}")
        print(f"Precio: {self.precio}")
        arrayPlantacion=[]
        arrayEmpleados=[]
        for plantacion in self.listaplantacion:
            arrayPlantacion.append(plantacion.mostrar_informacion())
        for empleado in self.listaempleados:
            arrayEmpleados.append(empleado.mostrar_informacion())
        calidadterrenofrase="Mala Calidad"
        if(self.calidadterreno==0):
            calidadterrenofrase="Mala Calidad"
        if(self.calidadterreno==1):
            calidadterrenofrase="Calidad Media" 
        if(self.calidadterreno==2):
            calidadterrenofrase="Buena Calidad"   
        if(self.calidadterreno==3):
            calidadterrenofrase="Calidad Excelente"  
        parcela_dict = {
            "nombre": self.nombre,
            "tamaño": self.tamaño,
            "precio": self.precio,
            "listaplantacion": arrayPlantacion,
            "listaempleados": arrayEmpleados,
            "factorMultiplicacionProducto": self.factorMultiplicacionProducto,
            "numeroEmpleados": self.numeroEmpleados,
            "numeroMaximoEmpleados": self.numeroMaximoEmpleados,
            "indiceproduccionempleados": self.indiceproduccionempleados,
            "calidadterreno": self.calidadterreno,
            "ciudadParcela": self.ciudadParcela,
            "indiceproductividadempleados": self.indiceproductividadempleados,
            "seguridad": self.seguridad,
            "maximaSeguridad": self.maximaSeguridad,
            "numeroplantaciones": self.numeroplantaciones,
            "calidadterrenofrase":calidadterrenofrase,
        }
        return parcela_dict
    

    def agregar_plantacion(self, tipoplantacion,bbdd):
        factormultiplicacion=1
        for factor in self.factorMultiplicacionProducto:
            if (tipoplantacion == factor):
                factormultiplicacion=2
        plantacion=Plantacion(tipoplantacion,factormultiplicacion,bbdd)
        self.listaplantacion.append(plantacion)

    def modificar_plantacion(self, index, tipoplantacion,bbdd):
        factormultiplicacion=1
        for factor in self.factorMultiplicacionProducto:
            if (tipoplantacion == factor):
                factormultiplicacion=2
        plantacion=self.listaplantacion[index]
        plantacion.tipo=tipoplantacion
        plantacion.urlicono="http://localhost:8083/"+tipoplantacion+".PNG"
        plantacion.factormultiplicacion=factormultiplicacion
        plantacion.produccionmes = bbdd.obtener_informacion_produccion_platacion_meses(tipoplantacion)
        self.listaplantacion[index] = plantacion

    def contratar_empleado(self,nombre_empleado, bbdd):
        if self.numeroEmpleados < self.numeroMaximoEmpleados:
            self.numeroEmpleados += 1
        else:
            print("no se puede contratar a mas personas")
        self.indiceproduccionempleados = self.numeroMaximoEmpleados/self.numeroEmpleados
        empleado=Empleados(nombre_empleado,self.ciudadParcela, bbdd)
        self.listaempleados.append(empleado)
        productividad=0
        for empleado in self.listaempleados:
            productividad += empleado.fuerza
        self.indiceproductividadempleados = productividad/self.numeroEmpleados

    def despedir_empleado(self,nombre_empleado):
        if self.numeroEmpleados != 0:
            self.numeroEmpleados -= 1
        else:
            print("no se puede despedir a mas personas")
        # self.indiceproduccionempleados = self.numeroMaximoEmpleados/self.numeroEmpleados
        for empleado in self.listaempleados:
            if empleado.nombre == nombre_empleado:
                self.listaempleados.remove(empleado)
        productividad=0
        for empleado in self.listaempleados:
            productividad += empleado.productividad
        # self.indiceproductividadempleados = productividad/self.numeroEmpleados

    def cambiarSeguridad(self,indice):
        self.seguridad=indice

    def incrementarCalidadTerreno(self,indice):
        if indice==1:
            self.calidadterreno=1
        if indice==2:
            self.calidadterreno=2
        if indice==3:
            self.calidadterreno=3
