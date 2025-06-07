class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar (self):
        print(f'meu naomo é {self.nome} e minha idade é {self.idade}')
