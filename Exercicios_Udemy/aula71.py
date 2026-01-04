frase = 'Eu tenho essas frases aqui né' \
        'vou adicionar esse também' \
        'E essa por fim'

i = 0
letra_atual = ''
maior_valor = 0

while i < len(frase):
    valor_atual = frase.count(frase[i])

    if frase[i] == ' ':
        i += 1
        continue

    if maior_valor < valor_atual:
        maior_valor = valor_atual
        maior_valor = valor_atual
        maior_valor = valor_atual
        maior_valor = valor_atual
        letra_atual = frase[i]

    i += 1

print(letra_atual, maior_valor)