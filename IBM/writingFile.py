lista = ['This is line A', 'This is line B', 'This is line C']

with open('./IBM/to_write.txt', 'w') as file:
    for line in lista:
        file.write(line + '\n')
        # Automatically close 