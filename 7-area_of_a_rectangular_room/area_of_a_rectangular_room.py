length_of_the_room = input("What is the length of the room in feet? ")
width_of_the_room = input("What is the width of the room in feet? ")
choosed_value = input("Do you want the output in feet or meter or both? ")

CONVERSION_FACTOR = 0.09290304

if(length_of_the_room.isnumeric() and width_of_the_room.isnumeric()):
    length = int(length_of_the_room)
    width = int(width_of_the_room)

    area_in_square_feet = length * width
    area_in_square_meters = area_in_square_feet * CONVERSION_FACTOR

    if choosed_value.lower() == 'feet':
        output = (
            f'You entered dimensions of {length} feet by {width} feet.\n'
            f'The area is\n'
            f'{area_in_square_feet} square feet\n'
        )
        print(output)
    elif choosed_value.lower() == 'meter':
        output = (
            f'You entered dimensions of {length} feet by {width} feet.\n'
            f'The area is\n'
            f'{area_in_square_meters:.3f} square meters'
        )
        print(output)
    elif choosed_value.lower() == 'both':
        output = (
        f'You entered dimensions of {length} feet by {width} feet.\n'
        f'The area is\n'
        f'{area_in_square_feet} square feet\n'
        f'{area_in_square_meters:.3f} square meters'
    )
        print(output)
    else:
        print("Please select the output format you want")
else:
    print("Please entered valid input values")

