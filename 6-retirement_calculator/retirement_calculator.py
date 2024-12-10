from datetime import date

current_age = input("What is your current age? ")
retirement_age = input("At what age would you like to retire? ")

todays_date = date.today()
current_year = todays_date.year

if (current_age > retirement_age):
    print("You can already retire")
else:
    years_left = int(retirement_age) - int(current_age)
    retirement_year = todays_date.year + years_left

    print("You have " + str(years_left) + " years left until you can retire.")
    print("It's " + str(current_year) + ", so you can retire in " + str(retirement_year) + ".")