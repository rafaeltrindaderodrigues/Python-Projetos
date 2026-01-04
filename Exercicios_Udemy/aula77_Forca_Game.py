"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import random
import os

palavra_correta = ['Apple', 'Judge', 'Accomplishment', 'Unknow', 'Beach', 'Umbrella', 'Crazy', 'Castle',
                   'Island', 'Kind', 'Sword', 'Cup', 'Guitar'
]

take_one_word = random.choice(palavra_correta).lower()
letras_acertadas = ''
numero_tentativas = 0

while True:
    player_move = input('Digite uma letra e tente acertar: ')
    numero_tentativas += 1

    if len(player_move) > 1:
        print('Digite apenas uma letra')
        continue

    if player_move in take_one_word:
        letras_acertadas += player_move

    palavra_formada = ''
    for letra_secreta in take_one_word:
        
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta 
        
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == take_one_word:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', take_one_word)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0

        
