# Gerar uma lista, com a possibilidade de inserir, apagar e listar

import os

lista_compras = []

while True:

    print("\nSelecione uma opção")
    escolha_usuario = input("[i]nserir [a]pagar l[istar]: ").lower()

    if escolha_usuario not in 'ial':
        print('Você não digitou corretamente.')
        continue
    
    if len(escolha_usuario) > 1:
        print('Digite apenas um por vez.')
        continue

    if escolha_usuario == 'i':
        os.system('clear')
        inserir_dados = input('Valor: ').capitalize()
        lista_compras.append(inserir_dados)
        
    if escolha_usuario == 'a':
        os.system('clear')

        for i, compras in enumerate(lista_compras):
            print(i, compras)
        
        apagar_indice = input('\nEscolha o índice para apagar: ')

        try:
            apagar_indice = int(apagar_indice)
            if apagar_indice > len(lista_compras) - 1:
                print('Não existe esse indice na lista')
                continue
            
            else:
              del lista_compras[apagar_indice]
        
        except:
            print('O valor digitado não foi numérico')
        

    
    if escolha_usuario == 'l':
        os.system('clear')

        for i, compras in enumerate(lista_compras):
            print(i, compras)
    