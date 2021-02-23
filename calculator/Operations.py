# imports modules
import sys
import time
# functions
# for functions that only take 2 arguments
def argument2(Question):
    try:
        number = float(input(Question))
        return number
    except:
        print("You did not enter a number.")
        sys.exit()

# to check how many numbers to use
def numbers():
    try:
        amount = int(input("How many numbers would you like to use? → "))
        if amount < 2:
            print("You did not enter a valid value. The question will be asked again.")
            time.sleep(0.5)
            numbers()
            sys.exit()
        nums = []
        for i in range(amount):
            nums.append(i)
            nums[i] = float(input("What is a number you would like to use? → "))
        return nums
    except:
        print("You may have made an input error. The questions will be asked again.")
        time.sleep(1)
        numbers()


# to divide with remainder
def divide_with_r(num1, num2):
    answer = divmod(num1, num2)
    print(num1, "÷", num2, "=", answer[0], "with a remainder of", answer[1])

# to subtract
def subtract(num1, num2):
    difference = num1-num2
    print(num1, "-", num2,"=", difference)

# to add
def add(numbers):
    list_of = numbers
    iter_of = iter(list_of)
    len_of_numbers = len(list_of)
    sum_of = sum(list_of)
    for i in range(len_of_numbers):
        if len_of_numbers -1 == i:
            print(next(iter_of), end = " ")
        else:
            print(next(iter_of), "+", end = " ")
    print("=", sum_of)


# to divide
def divide(num1, num2):
    quotient = num1/num2
    print(num1,"÷", num2,"=", quotient)
# to multiply
def multiply(num1, num2):
    product = num1 * num2
    print(num1, "x", num2, "=", product)

# to take the power of
def power_of(number, power):
    answer = pow(number, power)
    print(number, "to the power of", power, "is", answer)
