from Disco import Disco
from Torre import Torre
from Hanoi import Hanoi

torre1 = Torre(1)
torre2 = Torre(2)
torre3 = Torre(3)

hanoi = Hanoi()


def menu():
    print("Bem-Vindo ao Jogo Torre de Hanoi!!!")
    quantidade_discos = int(input("Com quantos discos deseja jogar? (min:3 max:8): "))
    if quantidade_discos < 3 or quantidade_discos > 8:
        print("Quantidade inválida, favor inserir a quantidade correta para jogar!")

    for i in range(1, quantidade_discos + 1):
        torre1.empilha_disco(Disco(i))

    torre1.exibe_discos_torre()
    while True:
        if len(torre3) == quantidade_discos:
            break

        seleciona_torre()



def seleciona_torre():
    torre_origem = int(input("Selecione qual torre deseja retirar o disco: "))
    torre_destino = int(input("Selecione qual torre deseja colocar o disco: "))
    if torre_origem == 1:
        torre_origem = torre1
    elif torre_origem == 2:
        torre_origem = torre2
    elif torre_origem == 3:
        torre_origem = torre3
    else:
        print("Torre inválida! insira 1, 2 ou 3 para selecionar a torre")

    if torre_destino == 1:
        torre_destino = torre1
    elif torre_destino == 2:
        torre_destino = torre2
    elif torre_destino == 3:
        torre_destino = torre3
    else:
        print("Torre inválida! insira 1, 2 ou 3 para selecionar a torre")

    hanoi.transfere_disco_de_torre(torre_origem, torre_destino)


if __name__ == '__main__':
    menu()

