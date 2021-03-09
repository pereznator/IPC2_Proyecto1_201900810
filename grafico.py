from graphviz import Digraph

class Grafica:
    matricesReducidas = []
    matricesOriginales = []
    def __init__(self, matricesReducidas, matircesOriginales):

        redAux = matricesReducidas.primero
        for x in range(matricesReducidas.cuenta):
            self.matricesReducidas.append(redAux.matriz)
            redAux = redAux.siguiente
        oriAux = matircesOriginales.primero
        for x in range(matircesOriginales.cuenta):
            self.matricesOriginales.append(oriAux.matriz)
            oriAux = oriAux.siguiente
        self.generarMatriz()

    def generarMatriz(self):
        print('Ingrese el nombre de la grafica que desea ver')
        nombre = input()
        matriz = {}
        resultado = False
        original = False
        for matrix in self.matricesReducidas:
            if nombre == matrix['nombre']:
                matriz = matrix
                resultado = True
        for matrix in self.matricesOriginales:
            if nombre == matrix['nombre']:
                matriz = matrix
                resultado = True
                original = True
        if not resultado:
            print('No se encontro resultados con el nombre \"'+nombre+'\"')
            return
        mat = Digraph(comment='Comentario')
        mat.node('nombre', matriz['nombre'])
        mat.node('n', 'n=\"'+matriz['n']+'\"')
        mat.node('m', 'm=\"'+matriz['m']+'\"')
        mat.edge('nombre', 'n')
        mat.edge('nombre', 'm')
        if not original:
            f = 0
            for fila in matriz['filas']:
                i = 0
                for item in fila:
                    mat.node(str(item['x'])+str(item['y']), str(item['valor']))
                    if f == 0:
                        mat.edge('nombre', str(item['x'])+str(item['y']))
                    else:
                        mat.edge(str(i+1)+str(f), str(item['x'])+str(item['y']))
                    i = i + 1
                f = f + 1
        else:
            for item in matriz['items']:
                mat.node(str(item['x'])+str(item['y']), str(item['valor']))
                if item['y'] == '1':
                    mat.edge('nombre', str(item['x'])+str(item['y']))
                else:
                    mat.edge(str(item['x'])+str(int(item['y'])-1), str(item['x'])+str(item['y']))

        print(mat.source)

        mat.render('reportes/grafo.gv')
