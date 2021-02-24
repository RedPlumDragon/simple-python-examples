# imports module
from decimal import Decimal

# payment
payment = input('What is the original price? → ')

# discount percentage
discount = input('What is the percent discount? → ')

# amount of discount
amount = (Decimal(discount) / 100) * Decimal(payment)

# what you have to pay
after_discount = Decimal(payment) - Decimal(amount)

# result
print('The amount you have to pay is', after_discount)
