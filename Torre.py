class Torre:
    def __init__(self, id):
        self._id = id
        self._discos = []

    def get_id(self):
        return self._id

    def empilha_disco(self, disco):
        self._discos.append(disco)

    def desempilha_disco(self):
        return self._discos.pop(0)

    def exibe_discos_torre(self):
        print("Torre: " + str(self._id), "\n")

        for disco in self._discos:
            print("Disco: ", disco.get_tamanho())

    def torre_vazia(self):
        return self._discos == []

    def primeiro_disco_da_torre(self):
        return self._discos[len(self._discos) - 1]
