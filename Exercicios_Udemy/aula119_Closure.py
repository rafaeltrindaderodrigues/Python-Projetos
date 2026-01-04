# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def criar_multiplicador(multiplicador):
    def multiplicar(num):
        return num * multiplicador
    return multiplicar

multiplicador_1 = criar_multiplicador(1)
multiplicador_2 = criar_multiplicador(2)
multiplicador_3 = criar_multiplicador(3)

print(multiplicador_1(10))
print(multiplicador_2(10))
print(multiplicador_3(10))




