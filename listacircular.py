from nodo import Nodo

class ListaCircular:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.cuenta = 0

    def vacia(self):
        return self.primero == None

    def agregarFinal(self, matriz):
        if self.vacia():
            self.primero = self.ultimo = Nodo(matriz)
            self.ultimo.siguiente = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(matriz)
            self.ultimo.siguiente = self.primero
        self.cuenta += 1

    def recorrer(self):
        aux = self.primero
        for x in range(self.cuenta):
            print(aux.matriz)
            aux = aux.siguiente


        