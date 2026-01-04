
"""

Faça um programa que peça ao usuário para digitar um número inteiro,

informe se este número é par ou ímpar. Caso o usuário não digite um número

inteiro, informe que não é um número inteiro.


try:  
    num_inteiro = int(input('Digite um número inteiro: '))
    if num_inteiro % 2 == 0:
        print('O número é par')
    else:
        print('O número é impar') 

except:
    print('O valor digitado não foi inteiro')
"""

"""

Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 

descrito, exiba a saudação apropriada. Ex. 

Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.


from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

hours = now.strftime("%H")
hours = int(hours)
if hours >= 0 and hours <= 6:
    print('Boa madrugada!')
elif hours > 6 and hours <= 12:
    print('Bom dia!')
elif hours > 12 and hours <= 6:
    print('Boa tarde!')
else:
    print('Boa noite')

print(now.strftime('%d-%m-%Y'))

"""



"""

Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 

menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 

"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

"""

try: 
    nome_user = str(input('Digite seu nome: '))
    espaco_count = nome_user.count(' ')

    cont_letras_nome = len(nome_user) - espaco_count

    if cont_letras_nome <= 4:
        print('Nome muito curto')
    elif cont_letras_nome <= 6:
        print('Nome normal')
    else:
        print('Seu nome é muito grande')

except:
    print('Você não digitou um nome válido')