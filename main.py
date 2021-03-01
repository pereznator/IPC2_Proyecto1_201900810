from cargar-archivo import CargarArchivo
class Main:
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
            elif opcion == '2':
                print('Procesar archivo')
            elif opcion == '3':
                print('Escribir archivo de salida')
            elif opcion == '4':
                print('Mostrar datos del Estudiante')
            elif opcion == '5':
                print('Generar Grafica')
            elif opcion == '6':
                print('Adios')
                break
            else:
                print('Debe ingresar alguna de las opciones disponibles')

m = Main()
            
