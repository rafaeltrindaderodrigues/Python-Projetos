"""
Iterando strings com while

Enunciado 
1 - Fazer com que a cada iteração com a string aconteça algo, exemplo:
string = 'Pedro lucas'

transformar ela para ficar
string = '*P*e*d*r*o* *l*u*c*a*s' -> tipo isso

"""

# PASSO 1: CRIANDO A VARIÁVEL E A LEITURA DE CARACTERES
nome = 'Rafael Trindade Rodrigues'
quantidade_letras_nome = len(nome) 


# PASSO 2: CRIANDO A REPETIÇÃO PARA BUSCAR CADA INDICE
# O indice começa por zero, então crio uma variável que começa por zero

indice = 0
novo_nome = ''

while indice < quantidade_letras_nome:
    novo_nome += f'*{nome[indice]}'

    indice += 1

print(novo_nome)



