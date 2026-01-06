d = {}

for letra in 'abracadabra':
    d[letra] = d.get(letra, 0) + 1

print(d)