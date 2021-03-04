class ProcesarArchivo:
    def __init__(self, matrices):
        self.matrices = matrices
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
            print(fordenadas)
