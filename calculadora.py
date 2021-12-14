def calculate():
    operation = input('''
Por favor, digite a operação matemática que você gostaria de fazer:
+ para adicao
- para subitracao
* para multiplicacao
/ para divisao
''')

    number_1 = int(input('Porfavor digite o primeiro numero: '))
    number_2 = int(input('Porfavor digite o segundo numero: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Não digitou um operador válido, por favor execute novamente o programa.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Voce quer usar a calculadora novamente?
Por favor digite S para Sim ou N para NAO.
''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('Ate logo!')
    else:
        again()

calculate()





