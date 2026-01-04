# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função que fala se um número é impar ou par.
# Retorne se o número é ímpar ou par

import sys

# Segundo exercicio
def qual_e(num):
    if num % 2 == 0:
        return 'Par'
    return 'Impar'

valor1 = qual_e(5231)
valor2 = qual_e(23013900)
print(valor1)
print(valor2)

sys.exit()

# Primeiro ex
def multiplica(*elementos):
    resultado = 1
    for elemento in elementos:
        resultado *= elemento
    return resultado


variavel1 = multiplica(1, 2, 3)
variavel2 = multiplica(10, 12, 2)

print(variavel1)
print(variavel2)