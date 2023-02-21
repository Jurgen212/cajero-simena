class Lector_archivo:

    def __init__(self):
        self.sentencias1     = []
        self.sentencias2     = []
        self.sentencias3     = []
        self.archivo1_txt    = open('./leer_archivo/archivos/BancoPython1.txt', mode='r')
        self.archivo2_txt    = open('./leer_archivo/archivos/BancoPython2.txt', mode='r')
        self.archivo3_txt    = open('./leer_archivo/archivos/BancoPython3.txt', mode='r')

    def verificar_archivo(self):
        print(self.archivo_txt.readable())

    def obtener_sentencias1(self):
        self.sentencias1 = self.archivo1_txt.readlines()
        self.archivo1_txt.close()
        return self.sentencias1


    def obtener_sentencias2(self):
        self.sentencias2 = self.archivo2_txt.readlines()
        self.archivo2_txt.close()
        return self.sentencias2
    
    def obtener_sentencias3(self):
        self.sentencias3 = self.archivo3_txt.readlines()
        self.archivo3_txt.close()
        return self.sentencias3