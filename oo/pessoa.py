class Pessoa:
    def __init__(self, *filhos, nome=None, idade=33):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == ' main ':
    jaque = Pessoa(nome='Jaque')
    maria = Pessoa(jaque, nome='Maria')
    print(Pessoa.cumprimentar(maria))
    print(id(maria))
    print(maria.cumprimentar())
    print(maria.nome)
    print(maria.idade)

    for filho in maria.filhos:
        print(filho.nome)
    maria.sobrenome = 'Ramalho'
    del  maria.filhos
    print(maria.__dict__)
    print(jaque.__dict__)







