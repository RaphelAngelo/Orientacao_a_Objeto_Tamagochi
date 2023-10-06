# 1. Crie uma classe para representar um Tamagochi, com os seguintes atributos
# - nome
# - fome (0 a 100, onde 0 é faminto e 100 é satisfeito)
# - energia (0 a 100, onde 0 é exausto e 100 energizado)
#
# 2. Crie os seguintes métodos para o Tamagochi
# - comer() -> Aumenta o status de fome + 10, não pode passar de 100
# - dormir() -> Aumenta o status de energia + 15, não pode passar de 100
# - status() -> Imprime o nome, a fome e a energia do Tamagochi

class Tamagochi:
    def __init__(self, nome, fome, energia):
        self.nome = nome
        self.fome = fome
        self.energia = energia

    def status(self):
        print(f"Nome: {self.nome}")
        print(f"Fome: {self.fome}%")
        print(f"Energia: {self.energia}%")

    def comer(self):
        if self.fome + 10 <= 100:
            self.fome += 10
            print(f'Comendo... fome: {self.fome}%')
        else:
            self.fome = 100
            print('Bucho cheio!')

    def dormir(self):
        if self.energia + 15 <= 100:
            self.energia += 15
            print(f'Zzzzz... Energia: {self.energia}%')
        else:
            self.energia = 100
            print('Estou energizado!!!!')


pet = Tamagochi('PetInfinity', 50, 100)
pet.status()
pet.dormir()
pet.comer()
pet.comer()
pet.comer()