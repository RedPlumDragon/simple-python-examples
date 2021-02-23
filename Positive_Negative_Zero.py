try:
    number = float(input("Enter a number. → "))

except:
    print("You did not enter a number.")

if number > 0:
    print("The number is positive.")

elif number < 0:
    print("The number is negative.")

else:
    print("The number is 0.")
