#!/usr/bin/env python3

# Created By: Brandon
# Date: November 11th, 2025
# This program asks the user for the number and then sums all the numbers up


def main():

    # get the age from the user
    number = input("Enter a positive number: ")

    # initialize counter and sum
    counter = 0
    sum = 0

    # Checking if the user entered an integer correctly
    try:
        number = int(number)
        print("You entered a positive number!")

        # determine whether or the not the number is positive
        if number < 0:
            print("Please Enter a positive number")
        else:
            while counter <= number:
                sum = sum + counter
                counter = counter + 1

        print(sum)

    except ValueError:
        print("That is not a valid integer")


# outputs the function
if __name__ == "__main__":
    main()
