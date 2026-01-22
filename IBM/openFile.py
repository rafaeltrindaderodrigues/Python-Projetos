with open('./IBM/text_to_read.txt', 'r') as file:
    i = 0
    for line in file:
        print('Interation', str(i), ': ', line)
        i += 1
