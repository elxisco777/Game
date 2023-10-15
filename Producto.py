class Producto():
    def __init__(self, tipoproducto):
        self.tipo = tipoproducto
        #añadir parametro factor localizacion

    def mostrar_informacion(self):
        print(f"Tipo Producto: {self.tipo}")
        producto_dict = {
            "tipo": self.tipo
        }
        return producto_dict