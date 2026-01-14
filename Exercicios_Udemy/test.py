def gen1(n=0):
    yield 1
    print('Continua')
    yield 2
    print('para')
    yield 3

gen = iter(gen1())

print(next(gen))                                                            
print(next(gen))                                                            
print(next(gen))                                                            