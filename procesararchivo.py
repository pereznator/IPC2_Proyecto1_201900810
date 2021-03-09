from listacircular import ListaCircular
class ProcesarArchivo:
    matrices = []
    matricesOrdenadas = []
    matricesBinarias = []
    matricesReducidas = []
    resultado = []
    listaReducidas = ListaCircular()
    def __init__(self, listaMatrices, invertida):
        #self.matrices = matrices
        self.invertida = invertida
        aux = listaMatrices.primero
        for m in range(listaMatrices.cuenta):
            p = {'nombre': aux.matriz['nombre'], 'n': aux.matriz['n'], 'm': aux.matriz['m'], 'items': []}
            for i in aux.matriz['items']:
                ni = {'x': i['x'], 'y': i['y'], 'valor': i['valor']}
                p['items'].append(ni)
            self.matrices.append(p)
            aux = aux.siguiente
        print('Procesando...')
        self.procesar()

    def procesar(self):
        for matriz in self.matrices:
            numfilas = int(matriz['n'])
            farr = []
            for x in range(numfilas):
                farr.append([])
            for item in matriz['items']:
                farr[int(item['y']) - 1].append(item)

            fordenadas = []
            for fila in farr:
                fordenada = []
                for x in range(len(fila)):
                    fordenada.append({})
                for item in fila:
                    fordenada[int(item['x']) - 1] = item
                fordenadas.append(fordenada)
            #print(fordenadas)
            self.matricesOrdenadas.append(fordenadas)
        self.binaria()

    def binaria(self):
        print('Calculando matriz binaria...')
        for matriz in self.matricesOrdenadas:
            mbinaria = []
            for fila in matriz:
                fbinaria = []
                for item in fila:
                    nitem = ''
                    if item['valor'] == '0':
                        nitem = '0'
                    else:
                        nitem = '1'
                    fbinaria.append(nitem)
                mbinaria.append(fbinaria)
            self.matricesBinarias.append(mbinaria)
        self.reducir()

    def reducir(self):
        m = 0
        setFrecuencias = []
        for matriz in self.matricesBinarias:
            filas = []
            n = 0
            filasRepetidas = []
            noRepetidas = []
            frecuencias = []
            for fila in matriz:
                repetida = False
                i = 0
                frecuencia = {'numFila': '', 'numRepetidas': 0, 'fila': fila}
                for f in filas:
                    if fila == f:
                        repetida = True
                        filasRepetidas.append({'original': i, 'repetida': n})
                        for x in frecuencias:
                            if x['fila'] == f:
                                x['numRepetidas'] += 1
                    i = i + 1
                if not repetida:
                    frecuencia['numFila'] = n + 1
                    frecuencia['numRepetidas'] += 1
                    frecuencias.append(frecuencia) 
                    filas.append(fila)
                    noRepetidas.append(n)
                n = n + 1
            setFrecuencias.append(frecuencias)
            self.matrizReducida(m, noRepetidas, filasRepetidas)
            m = m + 1
        
        x = 0
        for matriz in self.matrices:
            matrix = {'nombre': matriz['nombre']+'-reducida', 'n': str(len(self.matricesReducidas[x])), 'm': matriz['m'], 'filas': self.matricesReducidas[x], 'frecuencias': setFrecuencias[x]}
            self.resultado.append(matrix)
            self.listaReducidas.agregarFinal(matrix)
            x = x + 1


    def matrizReducida(self, noMatriz, noRepetidas, repetidas):
        print('Calculando matriz reducida...')
        x = 0
        finales = []
        for fila in self.matricesOrdenadas[noMatriz]:
            for num in noRepetidas:
                if x == num:
                    finales.append(fila)
            x = x + 1

        i = 0
        for fila in self.matricesOrdenadas[noMatriz]:
            for rep in repetidas:
                if i == rep['repetida']:
                    for item in fila:
                        finales[rep['original']][int(item['x']) - 1]['valor'] = int(finales[rep['original']][int(item['x']) - 1]['valor']) + int(item['valor'])
                        
            i = i + 1

        self.matricesReducidas.append(finales)

