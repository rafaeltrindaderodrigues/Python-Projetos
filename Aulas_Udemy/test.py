lista = [
    {"name": "Pendente"},
    {"name": "concluido"},
    {"name": "Realizando"}
]

lista[0]["name"] = "Concluido"
valor = list(lista[0].keys())[0]
print(lista[0][valor])