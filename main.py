from procesar_peticiones.Cajero import Cajero
from impresiones.Impresion      import imprimir_inicio, imprimir_solicitar_consola, imprimir_consignaciones, recibir_numeros_consola, ingrese_data_correcta

archivo = Cajero()

def ejecutar_programa():
    buena_eleccion = True

    while buena_eleccion:
        imprimir_inicio()
        eleccion = input(" --> ")

        if eleccion != "1" and eleccion != "2":
            ingrese_data_correcta()

        else:
            buena_eleccion = False

            if eleccion == "1":
                solicitar_data_consola()

            elif eleccion == "2":
                archivo.ejecutar_cajero_archivo( archivo )
        
    

def solicitar_data_consola():
    correr_programa = True
    
    archivo.ejecutar_cajero_consola(recibir_numeros_consola( "Inicio" ), "1")

    while correr_programa:

        imprimir_solicitar_consola()
        eleccion = input("--->")

        if eleccion == "1":
            archivo.ejecutar_cajero_consola( recibir_numeros_consola("Consignación") , "2")

        elif (eleccion == "2"):
            print("Seleccionaste Retiro, debes ingresar una cantidad valida")
            eleccion = input(" --> ")

            if (int(eleccion) <= 1000 and isinstance(int(eleccion), int)):
                ingrese_data_correcta()
            else:
                peticion = {'Retiro': (int(eleccion),)}
                archivo.ejecutar_cajero_consola(peticion, "3")

        elif (eleccion == "3"):
            print("Seleccionaste ver las denominaciones ( papi aquí lo que hay es billete )")
            print(archivo.get_denominaciones())

        elif (eleccion == "4"):
            imprimir_consignaciones( archivo )

        else:
            print("Adios :)")
            correr_programa = False

ejecutar_programa()