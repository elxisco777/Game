class Empleados():
    def __init__(self, nombreempleado,ciudad,bbdd):
        self.nombre = nombreempleado
        self.productividad,self.precio,self.comunicacion,self.estudios,self.fuerza,self.liderazgo = bbdd.obtener_informacion_empleado(nombreempleado, ciudad)
       

    def mostrar_informacion(self):
        print(f"Nombre Empleado: {self.nombre}, Productividad: {self.productividad}, Precio: {self.precio}, Comunicacion: {self.comunicacion}, Estudios: {self.estudios},Fuerza: {self.fuerza},Liderazgo: {self.liderazgo}")
        empleados_dict = {
            "nombre": self.nombre,
            "productividad": self.productividad,
            "precio": self.precio,
            "comunicacion":self.comunicacion,
            "estudios":self.estudios,
            "fuerza":self.fuerza,
            "liderazgo":self.liderazgo,
        }
        return empleados_dict