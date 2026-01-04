"""
Enunciado: Criar uma calculadora

"""

import time 

# PASSO 1: CRIAÇÃO DAS VARIÁVEL ENTRADA E SAIDA E COMEÇO DA ESTRUTURA DE REPETIÇÃO

while True:
    num1 = input('\nDigite um número: ')
    num2 = input('Digite outro número: ')
    operacao = input("Digite a operação '+-/*': ")


    # Etapa de validação dos valores digitadoes e estruturas de if
    num_validos = None

    try:
        num1 = float(num1)
        num2 = float(num2)
        num_validos = True

    except:
        num_validos = None

    if num_validos is None:
        print('O valor digitado em um ou ambos os números é inválido.')
        continue

    operacao_valida = '+-/*'

    if operacao not in operacao_valida:
        print('Digite uma operação válida.')
        continue

    if len(operacao) > 1:
        print('Digite somente uma operação')
        continue   

    # Agora que passamos pela limpeza de dados e validações, vamos fazer os cálculos
    print('Preparando o resultado...')
    time.sleep(1)
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    
    elif operacao == '*':
        print(f'{num1} * {num2} = {num1 * num2}')
    
    elif operacao == '/':
        print(f'{num1} / {num2} = {num1 / num2}')

    sair = input('Digite para sair s[air]: ').lower().startswith('s')

    if sair:
        break