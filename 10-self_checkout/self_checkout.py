TAX_RATE = 5.5 / 100
subtotal = 0 # Initialize subtotal
for i in range(3):
    while True:
        price = input("Enter the price of item " + str(i+1) + ": ")
        quantity = input("Enter the quantity of item " + str(i+1) + ": ")
        try:
            item_price = float(price)
            item_quantity = float(quantity)
            break
        except ValueError:
            print("Enter valid values")
    
    subtotal += item_price * item_quantity

# Calculate tax and total
tax = subtotal * TAX_RATE
total = subtotal + tax

print(f'Subtotal: ${subtotal:.2f}')
print(f'Tax: ${tax:.2f}')
print(f'Total: ${total:.2f}')


