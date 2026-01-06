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

count = 0

def condicionais(i, resposta_user):
    if i == 0:
        if resposta_user == '3':
            print('Você acertou')
            count += 1
            time.sleep(2)
        else: 
            print('Você errou')
            time.sleep(2)
    
    elif i == 1:
        if resposta_user == '1':
            print('Você acertou')
            count += 1
            time.sleep(2)
        else: 
            print('Você errou')
            time.sleep(2)

    elif i == 2:
        if resposta_user == '2':
            print('Você acertou')
            count += 1
            time.sleep(2)
        else: 
            print('Você errou')
            time.sleep(2)

for i, pergunta in enumerate(perguntas):
    
    # salvar cada key em perguntas dentro de uma variável
    Pergunta = pergunta['Pergunta']
    opcoes = pergunta['Opções']
    resposta = pergunta['Resposta']

    # fazer as perguntas para o usuário e mostrando as opções
    os.system('clear')
    print(f'\n{i + 1}) {Pergunta}\n')
    

    # para mostrar as opções, preciso acessar o array/lista que está dentro da variável
    for index, opcao in enumerate(opcoes):
        print(f'{index + 1}) {opcao}')

    # preciso pegar a resposta dele agora
    resposta_user = input('\nEscolha uma opção: ')

    condicionais(i, resposta_user)

os.system('clear')
print(f'\nVocê acertou {count}')


