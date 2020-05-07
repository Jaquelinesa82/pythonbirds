class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=33, ):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == ' main ':
    jaque = Pessoa(nome='jaque')
    maria = Pessoa(jaque, nome='maria')
    print(Pessoa.cumprimentar(maria))
    print(id(maria))
    print(maria.cumprimentar())
    print(maria.nome)
    print(maria.idade)
    for filho in maria.filhos:
        print(filho.nome)
    maria.sobrenome = 'Santos'
    del maria.filhos
    maria.olhos = 1
    del maria.olhos
    print(maria.__dict__)
    print(jaque.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(maria.olhos)
    print(jaque.olhos)
    print(id(Pessoa.olhos), id(maria.olhos), id(jaque.olhos))







