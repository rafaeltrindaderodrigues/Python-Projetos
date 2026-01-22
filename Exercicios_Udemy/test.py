# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Passo a passo
# Exercício 1 
# Aumentando o preço dos produtos em 10%
# Cálculo para fazer isso é ((valor x 10) / 100)

produtos_aumento_10 = []

for item in produtos:
    item['preco'] = round(item['preco'] * 1.10)
    produtos_aumento_10.append({'nome': item['nome'], 'preco': item['preco']})



# Exercício 2
# Novos produtos por deep copy
# Importar a biblioteca e dar copy.deepcopy

import copy

tabela = copy.deepcopy(produtos_aumento_10)

tabela[0]['nome'] = 'Melancia'


def ordenarLista(list):
    for item in list:
        return sorted(item['preco'])

print(ordenarLista(tabela))