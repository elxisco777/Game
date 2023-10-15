from Parcela import Parcela
from Tienda import Tienda
from Casa import Casa
import json
# from EmpresaElectronica import EmpresaElectronica

class Ciudad():
    def __init__(self, nombre, bbdd):
        self.nombre = nombre
        poblacion, coordenadas_x, coordenadas_y, idioma_principal,indiceproductos = bbdd.obtener_informacion_ciudad(nombre)
        self.poblacion = poblacion
        self.ubicacion = (coordenadas_x, coordenadas_y)
        self.idioma_principal = idioma_principal
        self.listatiendas = []
        self.listaparcelas = []
        self.listaEmpresaElectronica = []
        self.casa: Casa = None
        self.factorMultiplicacionProducto = indiceproductos
        self.prestigioCasa=0
 
    def mostrar_informacion(self):
        print(f"Ciudad: {self.nombre}")
        print(f"Población: {self.poblacion}")
        print(f"Ubicación: {self.ubicacion}")
        print(f"Idioma Principal: {self.idioma_principal}")
        print(f"Productos extra: {self.factorMultiplicacionProducto}")
        print("Parcela:")
        arrayTiendas = []
        arrayParcelas = []
        casavariable = ""
        for parcela in self.listaparcelas:
            arrayParcelas.append(parcela.mostrar_informacion())
        print("Tiendas:")
        for tienda in self.listatiendas:
            arrayTiendas.append(tienda.mostrar_informacion())
        if self.casa != None:
            casavariable=self.casa.mostrar_informacion()   
        print("\n")
        ciudad_dict = {
            "nombre": self.nombre,
            "poblacion": self.poblacion,
            "ubicacion": self.ubicacion,
            "idioma_principal": self.idioma_principal,
            "listatiendas": arrayTiendas,
            "listaparcelas": arrayParcelas,
            "casa": casavariable,
            "factorMultiplicacionProducto": self.factorMultiplicacionProducto,
            "prestigioCasa": self.prestigioCasa,
        }
        
        return ciudad_dict
    
    def comprar_parcela(self, nombre_parcela, bbdd):
        parcela=Parcela(nombre_parcela,self.nombre,self.factorMultiplicacionProducto,bbdd)
        self.listaparcelas.append(parcela)
        return parcela.precio
    
    def eliminar_obtener_parcela(self,nombreparcela):
        for index, parcela in  enumerate(self.listaparcelas):
            if parcela.nombre==nombreparcela:
                break
        self.listaparcelas.pop(index)
        print(parcela.nombre)
        return parcela
    
    def añadir_parcela(self, parcela):
        self.listaparcelas.append(parcela)
        return 

    def comprar_tienda(self, nombretienda, bbdd):
        tienda=Tienda(nombretienda,self.nombre,bbdd)
        self.listatiendas.append(tienda)
        return tienda.precio
    
    def eliminar_obtener_tienda(self,nombretienda):
        for index, tienda in  enumerate(self.listatiendas):
            if tienda.nombre==nombretienda:
                break
        self.listatiendas.pop(index)
        return tienda

    def añadir_tienda(self, tienda):
        self.listatiendas.append(tienda)
        return
    
    def comprar_casa(self, nombrecasa, bbdd):
        self.casa = Casa(nombrecasa,self.nombre,bbdd)
        self.prestigioCasa=self.casa.prestigio
        
"""     def comprar_empresa_electronica(self, nombreempresa, bbdd):
        empresa=EmpresaElectronica(nombreempresa,self.nombre,bbdd)
        self.listaEmpresaElectronica.append(empresa)
        return empresa.precio """