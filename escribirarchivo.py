import xml.etree.ElementTree as ET 

class EscribirArchivo:
    matrices = []
    def __init__(self, listaMatrices, invertida):
        self.invertida = invertida

        aux = listaMatrices.primero
        for x in range(listaMatrices.cuenta):
            self.matrices.append(aux.matriz)
            aux = aux.siguiente
        self.generarXML()

    def generarXML(self):
        print('Escribir una ruta especifica:')
        ruta = input()

        matrices = ET.Element('matrices')
        for matriz in self.matrices:
            print(matriz)
            mat = ET.SubElement(matrices, 'matriz', attrib={'nombre': matriz['nombre'], 'n': str(len(matriz['filas'])), 'm': str(len(matriz['filas'][0])), 'g': str(len(matriz['frecuencias']))})
            f = 1
            for fila in matriz['filas']:
                i = 1
                for element in fila:
                    if self.invertida == True:
                        item = ET.SubElement(mat, 'dato', attrib={'x': str(f), 'y': str(i)})
                    else:
                        item = ET.SubElement(mat, 'dato', attrib={'x': str(i), 'y': str(f)})
                    item.text = str(element['valor'])
                    i = i + 1
                f = f + 1
            for frecuencia in matriz['frecuencias']:
                fq = ET.SubElement(mat, 'frecuencia', attrib={'g': str(frecuencia['numFila'])})
                fq.text = str(frecuencia['numRepetidas'])

        data = ET.tostring(matrices)
        content = data.decode('utf-8')
        final = ''
        aux = False
        for x in range(len(content)):
            final = final + content[x]
            if content[x] in ('/'):
                aux = True
            if aux == True and content[x] in ('>'):
                final = final + '\n'
                aux = False

        if ruta == '':
            with open('salida/reducidas.xml', 'w') as archivo:
                archivo.write(final)
        else:
            with open(ruta, 'w') as archivo:
                archivo.write(final)
        print('Se escribió el archivo exitosamente')
            
            