from Vehiculo import Vehiculo
from Marca import Marca

Marca = Marca(tipo = None,
                    marca = None,
                    modelo=None,
                    precio=None,
                    correo=None, 
                    contrasena=None,
                    seguridad=None)
def menuApp():
    print("Inicialice con 1: ")

    init = int(input("Escriba 1: "))

    while init != 0:

        print(
            "\n Seleccione 1 para registrar empleado\n",
            "Seleccione 2 para Iniciar sesion\n",
            "Seleccion 3 para salir\n",
        )

        opc = int(input("Ingrese una opcion: "))

        if opc == 1:
            Marca.registrar_vehiculo()
        elif opc == 2:
            Marca.appMarca(Marca.iniciar_sesion, Marca.imprimir_registro)
        elif opc == 3:
            print("Salir")
            init = 0


menuApp()
