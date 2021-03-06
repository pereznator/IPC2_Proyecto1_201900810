from cargararchivo import CargarArchivo
from procesararchivo import ProcesarArchivo as Proceso
from escribirarchivo import EscribirArchivo as Escribir
from grafico import Grafica

class Main:
    matrices = []
    invertida = False
    def __init__(self):
        self.listaMatrices = None
        self.listaReducidas = None
        self.menu()

    def menu(self):
        while True:
            print('''
======================================================================================================================
1. Cargar Archivo
2. Procesar Archivo
3. Escribir Archivo de Salida
4. Mostrar Datos del Estudiante
5. Generar Grafica
6. Invertir coordenadas
7. Salida
            ''')
            opcion = input()
            if opcion == '1':
                print('Cargar Archivo')
                archivo = CargarArchivo()
                if not archivo.error:
                    print('Archivo cargado exitosamente')
                    self.matrices = archivo.matrices
                    self.listaMatrices = archivo.listaMatrices
                    #self.listaMatrices.recorrer()
            elif opcion == '2':
                print('Procesar archivo')
                if self.listaMatrices.cuenta == 0:
                    print('Se debe cargar un archivo primero')
                else:
                    pa = Proceso(self.listaMatrices, self.invertida)
                    self.listaReducidas = pa.listaReducidas
                    self.listaReducidas.recorrer()
            elif opcion == '3':
                if not self.listaReducidas:
                    print('Debe haber generado matrices reducidas primero')
                else:
                    print('Escribir archivo de salida')
                    escribir = Escribir(self.listaReducidas, self.invertida)
            elif opcion == '4':
                print('''
                >   Jorge Antonio Pérez Ordóñez
                >   201900810
                >   Introduccion a la Programacion y Computacion 2 Seccion E
                >   Ingenieria en Ciencias y Sistemas
                >   4to Semestre
                ''')
            elif opcion == '5':
                print('Generar Grafica')
                if not self.listaReducidas and not self.listaMatrices:
                    print('Debe haber matrices reducidas en memoria primero')
                else:
                    graph = Grafica(self.listaReducidas, self.listaMatrices)

            elif opcion == '6':
                if self.listaMatrices != None:
                    self.invertida = True
                    aux = self.listaMatrices.primero
                    for x in range(self.listaMatrices.cuenta):
                        t = aux.matriz['m']
                        aux.matriz['m'] = aux.matriz['n']
                        aux.matriz['n'] = t
                        for item in aux.matriz['items']:
                            c = item['x']
                            item['x'] = item['y']
                            item['y'] = c

                        aux = aux.siguiente
                else:
                    print('Debe haber cargado una matriz primero')
            elif opcion == '7':
                print('Adios')
                break
            else:
                print('Debe ingresar alguna de las opciones disponibles')

m = Main()
            
