

class Limpiar_impresiones:

    def __init__(self):
        return
    
    def limpiar_diccionario( peticion ):
        # {'Inicio': (0, 0, 0, 0, 0, 0, 0)}
        data = str( peticion ).replace("{", "")
        data = data.replace("'", "")
        data = data.replace("}", "")
        data = data.replace(":", "")
        data = data.replace(" ", "")
        return data