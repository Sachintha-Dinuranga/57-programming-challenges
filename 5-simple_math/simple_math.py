number1 = input("What is the first number? ")
number2 = input("What is the second number? ")

if (number1.isnumeric() and number2.isnumeric()):
    num1 = int(number1)
    num2 = int(number2)

    if num1 > 0 and num2 > 0:
        sum = num1 + num2
        difference = num1 - num2
        product = num1 * num2
        quotient = num1 / num2

        output = (
            f'{num1} + {num2} = {sum}\n'
            f'{num1} - {num2} = {difference}\n'
            f'{num1} * {num2} = {product}\n'
            f'{num1} / {num2} = {quotient:.2f}\n'
        )
        print(output)
    else:
        print("Please enter positive numbers only")
else:
    print("Please enter numeric value")
