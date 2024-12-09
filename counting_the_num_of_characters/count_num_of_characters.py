while True:

    input_string = input("What is the input string? ").strip()

    # Replace space with empty string
    input_string = input_string.replace(" ", "") 

    # Check whether the input is empty
    if len(input_string) == 0:
        print("You need to enter a string in to the program.")
    else:   
        # Calculate length of the string 
        num_of_characters = len(input_string) 
        print(input_string + " has " + str(num_of_characters) + " characters.")
        break