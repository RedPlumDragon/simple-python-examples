# imports modules
from Operations import *
import sys

# asks info
math_type = input('''Would you like to 1) add, 2) subtract, 3) multiply, 4) divide,
5) divide with a remainder, or 6) take the power of? → ''')

# lots of elif statements (with one if and one else statement)
if math_type == '1':
    add(numbers())
    sys.exit()

elif math_type == '2':
    subtract(argument2('What is the number you want to subtract from? → ')
             ,argument2('How much do you want to subtract from the first number? → '))
    sys.exit()

elif math_type == '3':
    multiply(argument2('What is the 1st number you would like to multiply? → ')
             ,argument2('What is the 2nd number you would like to multiply? → '))
    sys.exit()

elif math_type == '4':
    divide(argument2('What is the dividend? → ')
           ,argument2('What is the divisor? → '  ))
    sys.exit()

elif math_type == '5':
    divide_with_r(argument2('What is the dividend? → ')
                  ,argument2('What is the divisor? → '))
    sys.exit()

elif math_type == '6':
    power_of(argument2('What is the base? → ')
             ,argument2('What is the exponent? → '))
    sys.exit()

else:
    print('You may have made an input error. Try again.')
