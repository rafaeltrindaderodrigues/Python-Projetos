"""

Exercício

Peça ao usuário para digitar seu nome

Peça ao usuário para digitar sua idade

Se nome e idade forem digitados:

    Exiba:

        Seu nome é {nome}

        Seu nome invertido é {nome invertido}

        Seu nome contém (ou não) espaços

        Seu nome tem {n} letras

        A primeira letra do seu nome é {letra}

        A última letra do seu nome é {letra}

Se nada for digitado em nome ou idade: 

    exiba "Desculpe, você deixou campos vazios."

"""

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

if nome and idade:
    print(f'Seu nome é: "{nome}"')
    print(f'Seu nome invertido é: {nome[::-1]}')
    print(f'Seu nome contém espaços?: {' ' in nome}')
    nomesplit = nome.split()
    qntdname = 0

    # como não sabia um jeito de remover todos os espaços, separei por split e percorri todos os elementos
    # assim somei cada letra dos elementos, eliminando os espaços

    for nameqnt in nomesplit:
        qntdname = qntdname + len(nameqnt)
    print(f'A quantidade de letras em seu nome é: {qntdname}')
    print(f'The first letter from your name is: {nome[0]}')
    print(f'The last letter is: {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios!')
        



