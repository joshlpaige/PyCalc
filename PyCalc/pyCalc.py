import os

def clear():
    return os.system('cls')

def separator():
    print(40 * '-')

def menu():
    print(5 * '\n')
    separator()
    print('Welcome to pyCalc')
    separator()
    print('[1] - Add')
    print('[2] - Subtract')
    print('[3] - Multiply')
    print('[4] - Divide')
    print('[x] - Exit')

opc = ''
while(opc != 'x'):
    clear()
    menu()
    opc= input('select an option ')
    if(opc == 'x'):
        break

    num1 = float(input('First Number: '))
    num2 = float(input('Second Number: '))

    if(opc == '1'):
        res = num1 + num2
        print('Sum = ' + str(res))
    elif(opc == '2'):
        res = num1 - num2
        print('The Difference: ' + str(res))
    elif(opc == '3'):
        res = num1 * num2
        print('The Product: ' + str(res))
    elif(opc == '4'):
        if(num2 == '0'):
            print("Error: Don't divde by zero!")
        else:
            res = num1 / num2
            print('Result of the division: ' + str(res))


    input('press enter to continue...')

print('Thank You')