from cargararchivo import CargarArchivo
from procesararchivo import ProcesarArchivo as Proceso
from escribirarchivo import EscribirArchivo as Escribir
from grafico import Grafica

class Main:
    matrices = []
    def __init__(self):
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
6. Salida
            ''')
            opcion = input()
            if opcion == '1':
                print('Cargar Archivo')
                archivo = CargarArchivo()
                if not archivo.error:
                    self.matrices = archivo.matrices
            elif opcion == '2':
                print('Procesar archivo')
                if len(self.matrices) == 0:
                    print('Se debe cargar un archivo primero')
                else:
                    pa = Proceso(self.matrices)
                    self.matricesReducidas = pa.resultado
            elif opcion == '3':
                if not self.matricesReducidas:
                    print('Debe haber generado matrices reducidas primero')
                else:
                    print('Escribir archivo de salida')
                    escribir = Escribir(self.matricesReducidas)
            elif opcion == '4':
                print('Mostrar datos del Estudiante')
            elif opcion == '5':
                print('Generar Grafica')
                if not self.matricesReducidas and not self.matrices:
                    print('Debe haber matrices reducidas en memoria primero')
                else:
                    graph = Grafica(self.matricesReducidas, self.matrices)
            elif opcion == '6':
                print('Adios')
                break
            else:
                print('Debe ingresar alguna de las opciones disponibles')

m = Main()
            
