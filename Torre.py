class Torre:
    def __init__(self, id):
        self._id = id
        self._discos = []

    def empilha_disco(self, disco):
        self._discos.append(disco)

    def desempilha_disco(self):
        return self._discos.pop()

    def exibe_discos_torre(self):
        for disco in self._discos:
            print("Torre : " + str(self._id), "\nDisco: ", disco.get_tamanho(), "\n")

    def torre_vazia(self):
        return self._discos == []

    def primeiro_disco_da_torre(self):
        return self._discos[len(self._discos) - 1]
