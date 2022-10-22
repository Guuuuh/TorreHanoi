from Disco import Disco
from Torre import Torre
from Hanoi import Hanoi

torre1 = Torre(1)
torre2 = Torre(2)
torre3 = Torre(3)

disco = Disco(0)
disco1 = Disco(1)
disco2 = Disco(2)
disco3 = Disco(3)
disco4 = Disco(4)
disco5 = Disco(5)
disco6 = Disco(6)
disco7 = Disco(7)
disco8 = Disco(8)

quantidade_discos = int(input("Com quantos discos deseja jogar? (min:3 max:8)"))


def menu():
    if quantidade_discos < 3 or quantidade_discos > 8:
        print("Quantidade inválida, favor inserir a quantidade correta para jogar!")
    else:
        for i in range(quantidade_discos):
            torre1.empilha_disco(disco[i])


if __name__ == '__main__':
    menu()

    # torre1.exibe_discos_torre()
    # torre2.exibe_discos_torre()
    #
    # hanoi = Hanoi()
    #
    # hanoi.transfere_disco_de_torre(torre1, torre2)
    #
    #torre1.exibe_discos_torre()
    # torre2.exibe_discos_torre()
