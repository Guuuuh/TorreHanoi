from Disco import Disco
from Torre import Torre
from Hanoi import Hanoi


def menu():
    quantidade_discos = int(input("Com quantos discos deseja jogar? "))


def exibir_status_torre(Torre):
    return


if __name__ == '__main__':


    torre1 = Torre(1)
    torre2 = Torre(2)
    torre3 = Torre(3)

    disco1 = Disco("1")
    disco2 = Disco("2")
    disco3 = Disco("3")

    torre1.empilha_disco(disco3)
    torre1.empilha_disco(disco2)
    torre1.empilha_disco(disco1)

    torre1.exibe_discos_torre()

    hanoi = Hanoi()

    hanoi.retira_disco_da_torre(torre1)
    hanoi.insere_disco_na_torre(torre2)

    torre1.exibe_discos_torre()
