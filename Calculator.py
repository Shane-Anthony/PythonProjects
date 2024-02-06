  
print('''
          Welcome to Calculator
          ''')
def calculate():
  
    print('''Please pick the correct symbol for the operation you would like to perform:
            + for Addition
            - for Subtraction
            / for Division
            * for Multiplication
            ''')

    num1= int(input("Please input your first number: "))

    operand= input("Which operation would you like to perform? ")

    num2= int(input("Please input your second number: "))


    if operand == '+':
        print(' {} + {} = '.format(num1,num2))
        print (num1 + num2)
    elif operand == '-':
        print ('{} - {} = '.format(num1,num2))
        print(num1 - num2)
    elif operand == '/':
        print('{} / {} = '.format(num1,num2))
        print(num1/num2)
    elif operand == '*':
        print('{} * {} = '.format(num1,num2))
        print(num1*num2)
    else:
        print('You have input an invalid command. Please try again')
    
    again()

def again():
    another = input('Would you like to calculate some more? Yes / No : '.lower())
    if another == 'yes':
        calculate()
    elif another == 'no':
        print('Calculator Closing.')
    else:
        again()

calculate()