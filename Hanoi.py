from Torre import Torre
from Disco import Disco


class Hanoi:
    def __int__(self):
        pass


    def transfere_disco_de_torre(self, torre_origem, torre_destino):
        if torre_origem.torre_vazia():
            return -1

        disco_armazenado = Torre.desempilha_disco(torre_origem)
        disco_tamanho = Disco.get_tamanho(disco_armazenado)
        primeiro_disco_torre_origem = Disco.get_tamanho(Torre.primeiro_disco_da_torre(torre_origem))

        if disco_tamanho < primeiro_disco_torre_origem:
            torre_destino.empilha_disco(disco_armazenado)
