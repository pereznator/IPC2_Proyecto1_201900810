import xml.etree.ElementTree as ET 

class EscribirArchivo:
    def __init__(self, matrices):
        self.matrices = matrices
        

    def generarXML(self):
        matrices = ET.Element('matrices')
        for matriz in self.matrices:
            pass
