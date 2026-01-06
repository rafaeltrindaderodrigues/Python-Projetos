import os
import time

estoque = {
    'tomate': [1000, 2.30],
    'alface': [500, 0.45],
    'batata': [2001, 1.20],
    'feijão': [100, 1.50]
}

venda = []

while True:
# Adicionar no array venda
    os.system('clear')
    produto_nome = input('Nome do produto: ').lower()

    # Já fazer a verificação direta se existe ou não o produto no estoque
    if produto_nome not in estoque:
        print('Este produto não existe em nosso estoque\n')
        time.sleep(2)

    else: 
        try:
            quantidade_produto = int(input(f'Quantidade comprada de {produto_nome}: '))
        
        except ValueError:
            print('Digite um número, por favor.\n')
            time.sleep(2)
            continue

        # validações de tamanho de compras
        if quantidade_produto > estoque[produto_nome][0]:
            print('Você está pedindo mais do que temos em estoque')
        
        else: 
            venda.append([produto_nome, quantidade_produto])


            total = 0
            print("Vendas:\n")

            for operacao in venda: 
                produto, quantidade = operacao
                preco = estoque[produto][1]
                custo = preco * quantidade
                print(f'{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}')
                estoque[produto][0] -= quantidade
                total += custo

            print(f'\nCusto total: {total:21.2f}\n')
            print('Estoque:\n')

            for chave, dados in estoque.items():
                print('Descrição: ', chave)
                print('Quantidade: ', dados[0])
                print(f'preço: {dados[1]:6.2f}\n')
            
            time.sleep(10)




