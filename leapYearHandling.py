# Gets input from the user for the year, ensures it is in a valid range,
# and returns the value as an integer to main
def get_year():

    while (True):
        year_input = input("Enter a year between 0-2021.")
        if (int(year_input) > 0 and int(year_input) <= 2021):
            break
    
    return int(year_input)

# Determines if the given year is a leap year, based on assignment constraints
def is_leap_year(year):

    #If the year is divisible by 400, it is a LY
    if (year % 400 == 0):
        return 1

    else:
        #If the year is divisible by 4 and NOT 100, it is a LY   
        if (year % 4 == 0 and year % 100 != 0):
            return 1

        #If the year is divisible by 4 and 100 or not divisible by 4, NOT a LY
        else:
            return 0

# This program will get input from a user for a positive year and inform
# the user whether or not it is a leap year.
def main():

    year = get_year()

    if (is_leap_year(year)):
        print(str(year) + " is a leap year!")
    else:
        print(str(year) + " is not a leap year!")

main()