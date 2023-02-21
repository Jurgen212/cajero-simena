import math
from leer_archivo.Lista_acciones    import Lista_acciones
from leer_archivo.Escribir_archivo  import Escribir_archivo
from procesar_peticiones.Limpiar_impresiones import Limpiar_impresiones
from impresiones.Impresion                   import imprimir_consignaciones

escribir    = Escribir_archivo()
impresion   = Limpiar_impresiones()


valores_predeterminados = { "100k"  :   100, "50k"   :   100, "20k"   :   100,  "10k"   :   100, "5k"    :   100, "2k"    :   100, "1k"    :   100 }
valores = {"100k": 100000,"50k": 50000, "20k": 20000,"10k": 10000,"5k": 5000,"2k": 2000,"1k": 1000 }

class Cajero():

    def __init__(self):
        Lista                      = Lista_acciones()
        self.peticiones1            = Lista.llenar_lista_acciones1()
        self.peticiones2            = Lista.llenar_lista_acciones2()
        self.peticiones3            = Lista.llenar_lista_acciones3()

        self.total_denominaciones  = valores_predeterminados  
        self.retiros_totales       = 0
        self.consignaciones_totales= 0 
        self.saltar = True

    
    def ejecutar_cajero_archivo( self, archivo ):
        
        print("Archivo - 1")
        
        for peticion in self.peticiones1:
            if('Inicio' in peticion ):
                self.inicio( peticion )
            
            elif('Consignación' in peticion ):
                self.consignacion( peticion )
            
            elif('Retiro' in peticion ):
                self.retiro_de_dinero( peticion )
        imprimir_consignaciones( archivo )
        

        print("\n")
        self.asignar_valores_predeterminados()
        print("Archivo - 2")
        
        for peticion in self.peticiones2:
            if('Inicio' in peticion ):
                self.inicio( peticion )
            
            elif('Consignación' in peticion ):
                self.consignacion( peticion )
            
            elif('Retiro' in peticion ):
                self.retiro_de_dinero( peticion )
        imprimir_consignaciones( archivo )
        

        print("\n")
        self.asignar_valores_predeterminados()
        print("Archivo - 3")
        
        for peticion in self.peticiones3:
            if('Inicio' in peticion ):
                self.inicio( peticion )
            
            elif('Consignación' in peticion ):
                self.consignacion( peticion )
            
            elif('Retiro' in peticion ):
                print("Denominaciones: ", self.get_denominaciones())
                self.retiro_de_dinero( peticion )
        imprimir_consignaciones( archivo )

        


    def ejecutar_cajero_consola( self, peticion, opcion):
        
        
        if( opcion == "1" ):
            self.inicio( peticion )
            escribir.escribir_en_archivo( peticion , "1")
        
        elif( opcion == "2"):
            self.consignacion( peticion )
            escribir.escribir_en_archivo( peticion , "2")

        elif( opcion == "3"):
            self.retiro_de_dinero( peticion )
            escribir.escribir_en_archivo( peticion , "3")

    def inicio( self, peticion ):
        self.asignar_valores_predeterminados()
        self.sumar_consignacion_totales((100,100,100,100,100,100,100))
        self.modificar_consignacion( peticion["Inicio"] )

    def consignacion( self, peticion ):
        
        # print( peticion )
        print("\nConsignacion --> " , peticion["Consignación"] ) 
        self.modificar_consignacion( peticion["Consignación"] )
    
    def modificar_consignacion(self, valores_peticion  ):
        self.asignar_numero_denominaciones( valores_peticion)
        self.sumar_consignacion_totales( valores_peticion )


    def asignar_numero_denominaciones( self, tupla_valores ):

        self.total_denominaciones = {
            "100k"  :   tupla_valores[0] + self.total_denominaciones["100k"],
            "50k"   :   tupla_valores[1] + self.total_denominaciones["50k"] ,
            "20k"   :   tupla_valores[2] + self.total_denominaciones["20k"] ,
            "10k"   :   tupla_valores[3] + self.total_denominaciones["10k"] ,
            "5k"    :   tupla_valores[4] + self.total_denominaciones["5k"]  ,
            "2k"    :   tupla_valores[5] + self.total_denominaciones["2k"]  ,
            "1k"    :   tupla_valores[6] + self.total_denominaciones["1k"]
        }


    def asignar_numero_denominaciones_retiro( self, tupla_valores ):
        self.total_denominaciones = {
            "100k"  : self.total_denominaciones["100k"] - tupla_valores["100k"],
            "50k"   : self.total_denominaciones["50k"]  - tupla_valores["50k"],
            "20k"   : self.total_denominaciones["20k"]  - tupla_valores["20k"],
            "10k"   : self.total_denominaciones["10k"]  - tupla_valores["10k"],
            "5k"    : self.total_denominaciones["5k"]   - tupla_valores["5k"],
            "2k"    : self.total_denominaciones["2k"]   - tupla_valores["2k"],
            "1k"    : self.total_denominaciones["1k"]   - tupla_valores["1k"]
        }

    
    def sumar_consignacion_totales( self, tupla_valores ):
        

        print("\n")
        self.consignaciones_totales += tupla_valores[0] * 100000
        self.consignaciones_totales += tupla_valores[1] * 50000
        self.consignaciones_totales += tupla_valores[2] * 20000
        self.consignaciones_totales += tupla_valores[3] * 10000
        self.consignaciones_totales += tupla_valores[4] * 5000
        self.consignaciones_totales += tupla_valores[5] * 2000
        self.consignaciones_totales += tupla_valores[6] * 1000
        
        # print("Total de consignaciones: ", self.consignaciones_totales )


    def asignar_valores_predeterminados( self ):
        self.consignaciones_totales = 0
        self.retiros_totales        = 0
        self.total_denominaciones   = valores_predeterminados



    def retiro_de_dinero( self, peticion ):   
        cantidad_retirar = int( peticion["Retiro"][0] )
        print("\n------- Retiro( ", cantidad_retirar, " )")
        
        cantidades_billetes     = { "100k": 0, "50k" : 0, "20k" : 0, "10k" : 0, "5k"  : 0, "2k"  : 0, "1k"  : 0 }
        suma_cantidad_billetes  = 0
        
        denominacion_max = self.obtener_denominacion_max( cantidad_retirar )
        
        for denominacion in self.total_denominaciones:

            #solo hacemos operaciones con numeros menores a la cantidad necesitada
            if( ( denominacion == denominacion_max ) or valores[ denominacion_max ] >= valores[denominacion] ):
            
                suma_cantidad_billetes = self.sumatoria_parcial( cantidades_billetes, denominacion_max  );
                cantidad_restante = cantidad_retirar - suma_cantidad_billetes

                #a partir de aca, añadimos N-1 de la denominacion max ( si es 150k, se añaden 0 de 100k )
                if( denominacion == denominacion_max ): 
                    cantidades_billetes[ denominacion_max ] = self.cantidad_billetes_denominacion_max( denominacion_max, cantidad_retirar )
                

                #Numeros diferentes a denominacion max
                if( denominacion != "5k" and denominacion != "2k" and denominacion != "1k"  ):
                    cantidades_billetes[ denominacion ] = self.llamada_numeros_grandes( denominacion, cantidad_restante )

                #Tres ultimas denominaciones
                elif( self.saltar ):
                    cantidades_billetes[ denominacion ] = self.llamada_numeros_pequeños( denominacion, cantidad_restante )

        print("Billetes entregados -->  ", cantidades_billetes)
        self.asignar_numero_denominaciones_retiro( cantidades_billetes )

        if( self.saltar):
            print("Entro")
            self.retiros_totales = self.retiros_totales + cantidad_retirar



    def restar_cantidades_usadas( self, cantidades_billetes ):

        for denominacion in self.total_denominaciones:
            self.total_denominaciones[ denominacion ] -= cantidades_billetes[ denominacion ]


    def llamada_numeros_pequeños( self, denominacion, cantidad_restante ):

        contador = 0
        #Validamos que exista el numero
        if(( valores[denominacion] <= cantidad_restante and self.total_denominaciones[ denominacion ] != 0 and ( cantidad_restante / valores[ denominacion]) <= self.total_denominaciones[ denominacion ] )):

            if( denominacion != "1k"):
                for i in range( valores[denominacion], cantidad_restante, valores[ denominacion ] ):
                    contador += 1
            else:
                for i in range( 0, cantidad_restante, valores[ denominacion ]):
                    contador += 1

        return contador
            
    def llamada_numeros_grandes( self, denominacion, cantidad_restante ):

        contador = 0
        
        
        if( cantidad_restante >= valores[denominacion ]):
            for i in range( valores[denominacion], cantidad_restante - 1, valores[ denominacion ] ):
            #Verificamos que se pueda usar ese billete y que existan suficientes
                if( self.total_denominaciones[ denominacion ] != 0 and ( cantidad_restante / valores[ denominacion]) <= self.total_denominaciones[ denominacion ] ):
                    contador += 1
        
        return contador
            
        
    def obtener_denominacion_max( self, cantidad_retirar ):

        for denominacion in self.total_denominaciones:

            numero_billetes = self.total_denominaciones[denominacion]
            if(  numero_billetes != 0 and valores[denominacion] <= cantidad_retirar  ): return denominacion

    def sumatoria_parcial( self, cantidad_billetes, denominacion_max ):
        suma_parcial = 0

        for denominacion in cantidad_billetes:
            
            if( valores[denominacion ] <= valores[ denominacion_max ]):
                suma_parcial += valores[denominacion] * cantidad_billetes[denominacion]
        
        return suma_parcial 

    def cantidad_billetes_denominacion_max( self, denominacion_max, cantidad_retirar ):
        
        cantidad_restantes = self.total_denominaciones[ denominacion_max ]        
        cantidad_utilizar  = math.floor( cantidad_retirar / valores[ denominacion_max ] )
 
        if( cantidad_restantes != 0 and ( cantidad_restantes >= cantidad_utilizar )): 
            self.saltar = True
            return cantidad_utilizar - 1
        else:
            print("No hay tanto dinero papi, Adios :)")
            self.saltar = False
            return cantidad_restantes


    def get_denominaciones(self ):
        return self.total_denominaciones
    
    def get_total_consignado( self ):
        return self.consignaciones_totales
    
    def get_total_retirado( self ):
        return self.retiros_totales
    
    def get_total_dinero( self ):
        values = valores
        data = []
        
        data.append( self.total_denominaciones["100k"] * values["100k"] )
        data.append( self.total_denominaciones["50k"] * values["50k"] )
        data.append( self.total_denominaciones["20k"] * values["20k"] )
        data.append( self.total_denominaciones["10k"] * values["10k"] )
        data.append( self.total_denominaciones["5k"] * values["5k"] )
        data.append( self.total_denominaciones["2k"] * values["2k"] )
        data.append( self.total_denominaciones["1k"] * values["1k"] )
        
        return ( sum( data ) )
    
