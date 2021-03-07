import xml.etree.ElementTree as ET 

class EscribirArchivo:
    def __init__(self, matrices):
        self.matrices = matrices
        self.generarXML()

    def generarXML(self):
        matrices = ET.Element('matrices')
        for matriz in self.matrices:
            print(matriz)
            mat = ET.SubElement(matrices, 'matriz', attrib={'nombre': matriz['nombre'], 'n': str(len(matriz['filas'])), 'm': str(len(matriz['filas'][0]))})
            f = 1
            for fila in matriz['filas']:
                i = 1
                for element in fila:
                    item = ET.SubElement(mat, 'item', attrib={'x': str(i), 'y': str(f)})
                    item.text = str(element['valor'])
                    i = i + 1
                f = f + 1

        data = ET.tostring(matrices)
        print(data)
        with open('salida/reducidas.xml', 'w') as archivo:
            archivo.write(data.decode('utf-8'))
            