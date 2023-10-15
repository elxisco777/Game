class Casa():
    def __init__(self, nombrecasa,nombreciudad,bbdd):
        self.nombrecasa = nombrecasa
        self.precio,self.prestigio = bbdd.obtener_informacion_casa(nombrecasa,nombreciudad)
        self.seguridad = 0

    def mostrar_informacion(self):
        print(f"Nombre Casa: {self.nombrecasa}")
        print(f"Precio: {self.precio}")
        print(f"Prestigio: {self.prestigio}")
        print(f"Seguridad: {self.seguridad}")
        casa_dict = {
            "nombre": self.nombrecasa,
            "precio": self.precio,
            "prestigio": self.prestigio,
            "seguridad": self.seguridad
        }
        return casa_dict

    def cambiarSeguridad(self,indice):
        self.seguridad=indice