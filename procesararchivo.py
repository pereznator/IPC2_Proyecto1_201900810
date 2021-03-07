class ProcesarArchivo:
    matricesOrdenadas = []
    matricesBinarias = []
    matricesReducidas = []
    resultado = []
    def __init__(self, matrices):
        self.matrices = matrices
        print(matrices)
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
        for matriz in self.matricesBinarias:
            filas = []
            n = 0
            filasRepetidas = []
            noRepetidas = []
            for fila in matriz:
                repetida = False
                i = 0
                for f in filas:
                    if fila == f:
                        repetida = True
                        filasRepetidas.append({'original': i, 'repetida': n})
                    i = i + 1
                if not repetida:
                    filas.append(fila)
                    noRepetidas.append(n)
                n = n + 1
            self.matrizReducida(m, noRepetidas, filasRepetidas)
            m = m + 1
        
        x = 0
        for matriz in self.matrices:
            self.resultado.append({'nombre': matriz['nombre']+'-reducida', 'n': str(len(self.matricesReducidas[x])), 'm': matriz['m'], 'filas': self.matricesReducidas[x]})
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

