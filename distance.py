# you will need to know the pythogarean theorem for this
import math
from decimal import Decimal

print('This is a program to find the distance between 2 points.')
x1 = input('What is the x of the first point? → ')
y1 = input('What is the y of the first point? → ')
x2 = input('What is the x of the second point? → ')
y2 = input('What is the y of the second point? → ')

distance = math.sqrt(math.pow(Decimal(x1) - Decimal(x2), 2) + math.pow(Decimal(y1) - Decimal(y2), 2))

print('The distance between the 2 points is: ' + str(distance))
