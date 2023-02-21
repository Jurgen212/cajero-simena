from procesar_peticiones.Limpiar_impresiones import *

class Escribir_archivo:
    

    def __init__(self):
        self.limpiar_peticiones = Limpiar_impresiones()
        
    def escribir_en_archivo( self, peticion, opcion ):

        archivo = open('./leer_archivo/Registro.txt', mode='a')
        with archivo as file:
            if( opcion == "1" ):
                file.write( Limpiar_impresiones.limpiar_diccionario( peticion )  + "\r\n")
            elif( opcion == "2" ):
                
                file.write( Limpiar_impresiones.limpiar_diccionario( peticion ) + "\r\n")
            elif( opcion == "3" ):
                file.write( Limpiar_impresiones.limpiar_diccionario( peticion ) + "\r\n")
        

        archivo.close()

        


    
        