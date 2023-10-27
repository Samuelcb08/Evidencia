from Vehiculo import Vehiculo

class Marca(Vehiculo):
    def __init__(self,tipo,marca,modelo,precio,correo,contrasena,seguridad):
        super().__init__(tipo,marca,modelo,precio,correo,contrasena)
        self._seguridad = seguridad

    @property
    def seguridad(self):
        return self._seguridad

    @seguridad.setter
    def seguridad(self, seguridad):
        self._seguridad = seguridad    

    def registrar_vehiculo(self):
       self._correo = input("Ingrese el correo del usuario:")
       self._contrasena = input("Ingrese la contraseña del usuario: ")
       self._tipo= input("Ingrese el tipo del vehiculo: ")
       self._marca= input("Ingrese la marca del vehiculo: ")
       self._modelo= input("Ingrese el modelo del vehiculo: ")
       self._precio = input(f"Ingrese el precio del vehiculo: ")    
       self._seguridad = input("Cuantas estrellas de seguridad?: ")

    def imprimir_registro(self):
        super().imprimir_registro()   
        print(f"Seguridad: {self._seguridad}")
        

    def iniciar_sesion(self):
        correo_emp = input("Ingrese el correo registrado: ")
        contras_emp = input("Ingrese la contraeña: ")

        if correo_emp == self._correo and contras_emp == self._contrasena:
            return True
        else:
            return False

    def appMarca(self, iniciar_sesion, imprimir_registro):
        iniciar_sesion()== True
        print("Has iniciado sesion")
        super().imprimir_registro()    