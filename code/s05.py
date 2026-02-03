# A product costs $100, how much tax do we pay?

product = 100
tax_rate = 0.0625
tax = product * tax_rate
print(f'The tax for a product which costs ${product} is ${tax}.') #f-string

def calc_tax(price): 
    """Calculate product tax based on given price and return the tax amount."""
    tax_rate = 0.0625
    tax = price * tax_rate
    # print(f'The tax for a product which costs ${product} is ${tax}.')
    # print(tax)
    # if the function does not explicitly return any value, it will return None
    return tax

computer_price = float(input('Enter product price:'))

# calc_tax(100)
# calc_tax(20)
# 
tax_computer = calc_tax(computer_price)
print(tax_computer)