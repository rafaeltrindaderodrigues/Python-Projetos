import math as mt

def square():
    try:    
        number = float(input('Type a number to see its square root: '))
        print(mt.sqrt(number))

    except ValueError:
        print('The number could not be less than zero / and cannot be a string as well')



square()


