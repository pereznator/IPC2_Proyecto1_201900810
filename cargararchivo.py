import xml.etree.ElementTree as ET
from listacircular import ListaCircular

class CargarArchivo:
    error = False
    def __init__(self):
        print('Ingrese la ruta del archivo')
        ruta = input()
        self.leerArchivo(ruta)

    def leerArchivo(self, ruta):
        try:
            doc = ET.parse(ruta)
            raiz = doc.getroot()
            matrices = []
            listaMatrices = ListaCircular()
            for matriz in raiz:
                if matriz.tag == 'matriz':
                    nmatriz = {'nombre': matriz.attrib['nombre'], 'n': matriz.attrib['n'], 'm': matriz.attrib['m'], 'items': [] }    
                    for x in matriz:
                        if x.tag == 'dato':
                            x.attrib['valor'] = x.text
                            nmatriz['items'].append(x.attrib)
                    matrices.append(nmatriz)
                    listaMatrices.agregarFinal(nmatriz)
            #print(matrices)
            self.matrices = matrices
            self.listaMatrices = listaMatrices
        except:
            print('No se pudo cargar el archivo en: ', ruta)
            self.error = True

        
        