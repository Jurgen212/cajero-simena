from leer_archivo.lector_archivo import Lector_archivo


class Lista_acciones():

    def __init__(self):
        self.leerArchivo    = Lector_archivo()
        self.lista_acciones1 = []
        self.lista_acciones2 = []
        self.lista_acciones3 = []


    def llenar_lista_acciones1(self):
        lista_sucia = self.leerArchivo.obtener_sentencias1()

        # Eliminar \n
        acciones                = [f'{ accion_valor[:-1] }' for accion_valor in lista_sucia]
        separar_parentesis      = separar_lista_por_parentesis(acciones)
        self.lista_acciones1     = crear_diccionario_acciones( separar_parentesis)

        return self.lista_acciones1
    
    def llenar_lista_acciones2(self):
        lista_sucia = self.leerArchivo.obtener_sentencias2()

        # Eliminar \n
        acciones                = [f'{ accion_valor[:-1] }' for accion_valor in lista_sucia]
        separar_parentesis      = separar_lista_por_parentesis(acciones)
        self.lista_acciones2     = crear_diccionario_acciones( separar_parentesis)

        return self.lista_acciones2
    
    def llenar_lista_acciones3(self):
        lista_sucia = self.leerArchivo.obtener_sentencias3()

        # Eliminar \n
        acciones                    = [f'{ accion_valor[:-1] }' for accion_valor in lista_sucia]
        separar_parentesis          = separar_lista_por_parentesis(acciones)
        self.lista_acciones3        = crear_diccionario_acciones( separar_parentesis)

        return self.lista_acciones3


def crear_diccionario_acciones(separar_parentesis):
    valor_retorno       = [{accion[0].strip(): convertir_string_a_tupla(accion[1])} for accion in separar_parentesis if accion[1][-1] == ')']
    last_e_lista        = separar_parentesis[len(separar_parentesis) - 1]
    valor_retorno.append({last_e_lista[0].strip(): convertir_string_a_tupla(last_e_lista[1])})  # Agregamos ultimo elemento de lista que se queda por fuera

    return valor_retorno


def convertir_string_a_tupla(string):
    string_sin_parentesis       = ''

    if (string[-1] == ')'):
        string_sin_parentesis   = string[:-1].split(',')
    else:
        string_sin_parentesis   = string.split(',')

    return tuple([int(valor.strip()) for valor in string_sin_parentesis])


def separar_lista_por_parentesis(acciones):
    return [accion.split('(') for accion in acciones]
