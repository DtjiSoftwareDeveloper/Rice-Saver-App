"""
This file contains code for the application "Rice Saver App".
Author: DtjiSoftwareDeveloper
"""


# Importing necessary library


import sys


# Creating main function to run the application


def main():
    """
    This main function is used to run the application.
    :return: None
    """

    print("Welcome to 'Rice Saver App' by 'DtjiSoftwareDeveloper'.")
    print("This application helps you save rice by knowing how many cups of rice and for how long you need to cook.")
    print("Notes: 1 cup or rice = 200 grams. More information about rice conversion is in ")
    print("https://www.traditionaloven.com/conversions_of_measures/rice_amounts_converter.html.")
    print("Enter 'Y' for yes.")
    print("Enter anything else for no.")
    continue_using: str = input("Do you want to continue using 'Rice Saver App'? ")
    while continue_using == "Y":
        weight: float = float(input("How many kilograms of rice do you need to cook? "))
        cups: int = int(weight * 5)
        minutes_needed: int = cups * 5
        print("Cook " + str(cups) + " cups of rice for " + str(minutes_needed) + " minutes!")
        print("Enter 'Y' for yes.")
        print("Enter anything else for no.")
        continue_using = input("Do you want to continue using 'Rice Saver App'? ")
    sys.exit()


if __name__ == '__main__':
    main()
