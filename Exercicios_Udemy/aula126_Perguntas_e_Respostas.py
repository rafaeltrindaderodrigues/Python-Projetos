# Exercício - sistema de perguntas e respostas

import os
import time

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0

for valores in perguntas:
    os.system('clear')
    print(f'\n{valores['Pergunta']}: ')

    print('\nOpções')
    quantidade_respostas = len(valores['Opções'])

    for i, opcao in enumerate(valores['Opções']):
        print(f'{i}) {opcao}')

    resposta = input('\nEscolha uma opção: ')

    if resposta not in valores['Opções']:
        print('O valor que você digitou não está entre as opções')
        time.sleep(1.5)
        
        
    if resposta == valores['Resposta']:
        print('Você acertou, parabéns 🔥')
        acertos += 1
        time.sleep(1.5)
    
    else: 
        print('Você errou ❌')
        time.sleep(1.5)

print(f'\nVocê teve {acertos} acertos')