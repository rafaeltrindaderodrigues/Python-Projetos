pessoa = {
    'name': 'Rafael',
    'nacionalidade': 'Brasileiro',
    'UF': 'SP',
    'idade': 20
}

if pessoa.get('idade') is None:
    print('Não existe a chave idade')
else:
    print(pessoa['idade'])