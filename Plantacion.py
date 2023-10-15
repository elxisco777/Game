class Plantacion():
    def __init__(self, tipoplantacion,factormultiplicacion,bbdd):
        self.tipo = tipoplantacion
        self.factormultiplicacion = factormultiplicacion
        self.produccionmes,self.urlicono = bbdd.obtener_informacion_produccion_platacion(tipoplantacion)
        self.select={ "nombre": self.tipo, "urlicono": self.urlicono }
       

    def mostrar_informacion(self):
        print(f"Tipo Plantacion: {self.tipo}")
        print(f"Factor Multiplicacion: {self.factormultiplicacion}")
        print(f"Produccion Mensual: {self.produccionmes}")
        print(f"urlicono: {self.urlicono}")
        print(f"select: {self.select}")
        platacion_dict = {
            "tipo": self.tipo,
            "factormultiplicacion": self.factormultiplicacion,
            "produccionmes": self.produccionmes,
            "urlicono":self.urlicono,
            "select":{ "nombre": self.tipo, "urlicono": self.urlicono }
        }
        return platacion_dict
