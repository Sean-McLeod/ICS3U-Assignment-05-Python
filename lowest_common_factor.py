#!/usr/bin/env python3

# Created by Sean McLeod
# Created on December 2020
# This program can calculate the lowest common factor


def main():
    # this function can tell the user what the two numbers' LCM is

    print("This program can calculate the LCM of two integers")
    print("\n", end="")

    # input
    first_string = input("Enter in a positive integer: ")
    second_string = input("Enter in a positive integer: ")
    print("\n", end="")

    # process & output
    try:
        first_integer = int(first_string)
        second_integer = int(second_string)

        if first_integer > second_integer:
            greater = first_integer
        else:
            greater = second_integer

        if first_integer == 0 or second_integer == 0:
            print("We can't accept 0. Try again")
        else:
            if first_integer > 0 and second_integer > 0:
                while greater % first_integer != 0 or \
                      greater % second_integer != 0:
                    greater = greater + 1
                print("The lowest common factor is {}".format(greater))
            else:
                print("This is a negative integer")

    except Exception:
        print("This is not an integer")


if __name__ == "__main__":
    main()
