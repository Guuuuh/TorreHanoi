from Disco import Disco
from Torre import Torre
from Hanoi import Hanoi

torre1 = Torre(1)
torre2 = Torre(2)
torre3 = Torre(3)


def menu():
    print("Bem Vindo ao Jogo Torre de Hanoi!!!")
    quantidade_discos = int(input("Com quantos discos deseja jogar? (min:3 max:8)"))
    if quantidade_discos < 3 or quantidade_discos > 8:
        print("Quantidade inválida, favor inserir a quantidade correta para jogar!")

    for i in range(1, quantidade_discos + 1):
        torre1.empilha_disco(Disco(i))

    torre1.exibe_discos_torre()


if __name__ == '__main__':
    menu()

