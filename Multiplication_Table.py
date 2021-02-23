import sys

try:
    number = int(input("Enter the number you want multiplied. → "))

except:
    print("You did not enter a number.")
    sys.exit()


try:
    for multiplication in range(int(input("How many times do you want your number multiplied? → "))):
        multiplication = multiplication + 1
        product = number * multiplication
        print(number, "x", multiplication, "=", product)

except:
    print("You did not enter a number.")
    sys.exit()
