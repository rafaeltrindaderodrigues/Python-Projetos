class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return f'Olá, meu nome é {self.nome} e tenho {self.idade}'
    

pessoa1 = Pessoa('Rafael', 18)

print(pessoa1)
                                                            