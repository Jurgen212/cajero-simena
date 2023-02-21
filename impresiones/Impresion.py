from os import system


def imprimir_inicio():
    
    print("\n----------------- // -----------------")
    print("Bienvenido al cajero automatico")
    print("¿Desea ingresar sus propios datos o utilizar el archivo de texto?")
    print("Para sus propios datos ingrese ( aún sigue en desarrollo por falta de tiempo ) ( 1 ), de lo contrario para archivos txt ( 2 )")


def imprimir_solicitar_consola():
    print("\nSeleccione una de las siguientes opciones: ")
    print("Para realizar consignacion               --> 1 ")
    print("Para realizar retiro                     --> 2 ")
    print("Para observar denominaciones actuales    --> 3 ")
    print("Para observar cuanto se ha retirado y depositado en total, ademas el total actual--> 4 ")
    print("\nCualquier otra letra para salir")

def imprimir_consignaciones( archivo ):
    print("Seleccionaste ver consignaciones totales, dinero total y retiro total)")
    print("Denominaciones ", archivo.get_denominaciones() )
    print("Total consignado: "      , archivo.get_total_consignado  ()  )
    print("Total retirado: "        , archivo.get_total_retirado    ()  )
    print("Total dinero actual: "   , archivo.get_total_dinero      ()  )


def recibir_numeros_consola( tipo_peticion ):
    print("Seleccionaste consignar, debes ingresar un monto inicial de 7 digitos separados por comas(,)")

    data_correcta = True

    while( data_correcta ):
        try:
            eleccion        = input("(x,y,z,k,l,m,n) --> ").split(",")
            eleccion        = [ int( value ) for value in eleccion ]
            data_correcta   = False
        except: 
            system("cls")
            system("clear")
            ingrese_data_correcta()
            print("Vuelva a consignar")

 
    return  {f'{tipo_peticion}': ( eleccion[0], eleccion[1],eleccion[2],eleccion[3],eleccion[4],eleccion[5],eleccion[6] )}


def ingrese_data_correcta():
    print("Por favor ingrese una opción valida")