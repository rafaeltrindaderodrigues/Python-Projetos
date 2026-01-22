def safe_devide(num1, num2):
    try:
        return num1 / num2
    
    except ZeroDivisionError:
        return None


num1 = int(input('Type a number: '))
num2 = int(input('Type a number: '))

gen = safe_devide(num1, num2) 

if gen is None:
    print('Cannot be divided by 0')
else:
    print(gen)
