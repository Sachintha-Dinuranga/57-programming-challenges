import math

room_type = input("What is the room type (square/round)? ")
ONE_GALLON = 350
PI = 3.14
if room_type.lower() == 'square':
    length = input("Enter length: ")
    width = input("Enter width: ")

    if(length.isnumeric() and width.isnumeric()):
        new_length = int(length)
        new_width = int(width)

        area = new_length * new_width
        num_of_gallons = area / ONE_GALLON
        num_of_gallons = math.ceil(num_of_gallons)

        print(f'You will need to purchase {num_of_gallons} gallons of paint to cover {area} square feet.')
    else:
        print("Please enter numeric values")
elif room_type.lower() == 'round':
    radius = input("Enter radius: ")

    if(radius.isnumeric()):
        new_radius = int(radius)

        area = PI * new_radius * new_radius
        num_of_gallons = area / ONE_GALLON
        num_of_gallons = math.ceil(num_of_gallons)

        print(f'You will need to purchase {num_of_gallons} gallons of paint to cover {area} square feet')
    else:
        print("Please enter numeric values")
else:
    print("Please select a room type")