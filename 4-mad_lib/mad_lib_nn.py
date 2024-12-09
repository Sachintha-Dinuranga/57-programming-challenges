from mad_lib_cls import Madlibs

while True:
    noun = str(input("Enter a noun: "))
    verb = str(input("Enter a verb: "))
    adjective = str(input("Enter a adjective: "))
    verb2 = str(input("Enter a another verb: "))

    str_list = {noun, verb, adjective, verb2}

    # Check whether the entered value is digit or not
    isNotDigit = all(i.isdigit() == False for i in str_list)

    if isNotDigit == True:
        madlib = Madlibs(noun, verb, adjective, verb2)
        madlib.first_method()
        madlib.second_method()
        madlib.third_method()
        break
    else:
        print("Enter the correct values!")

