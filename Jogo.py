from Torre import Torre
from Disco import Disco


class Jogo:
    def __int__(self):
        pass

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


    def menu(self):
        while True:
            if self.quantidade_discos < 3 or self.quantidade_discos > 8:
                print("Quantidade inválida, favor inserir a quantidade correta para jogar!")
            else:
                for i in range(self.quantidade_discos):
                    self.torre1.empilha_disco(self.disco[i])
                    break
