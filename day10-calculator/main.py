"""
Calculator Project
"""
#Imports the art.py file that contains the projects logo
import art

#Define functions for each math operation
def add(n1, n2):
    print(f"{n1} + {n2} = {n1 + n2}")
    return n1 + n2

def subtract(n1, n2):
    print(f"{n1} - {n2} = {n1 - n2}")
    return n1 - n2

def multiply(n1, n2):
    print(f"{n1} * {n2} = {n1 * n2}")
    return n1 * n2

def divide(n1, n2):
    print(f"{n1} / {n2} = {n1 / n2}")
    return n1 / n2

def continue_calculating(n1):
    print("+\n-\n*\n/")
    op = input("Pick an operation: ")
    while op not in ["+", "-", "*", "/"]:
        op = input("Pick an operation: ")
    n2 = int(input("What's the next number?: "))
    if op == "+":
        new_result = add(n1, n2)
    elif op == "-":
        new_result = subtract(n1, n2)
    elif op == "*":
        new_result = multiply(n1, n2)
    else:
        new_result = divide(n1, n2)
    return new_result

#Sets the initial calculator loop
reset = False

#Main program loop
while not reset:

    #Prints calculator logo
    print(art.logo)

    #Gets first integer
    n1 = int(input("What's the first number?: "))

    #Shows available operators
    print("+\n-\n*\n/")

    #Gets operator that the user wants to use
    op = input("Pick an operation: ")

    #While loop to make sure user chose a correct operation
    while op not in ["+", "-", "*", "/"]:
        op = input("Pick an operation: ")

    #Gets second integer
    n2 = int(input("What's the second number?: "))

    #If/else branch deciding what operation to use
    if op == "+":
        result = add(n1, n2)
    elif op == "-":
        result = subtract(n1, n2)
    elif op == "*":
        result = multiply(n1, n2)
    else:
        result = divide(n1, n2)

    #Prompts user to see if they want to keep calculating with the existing result
    keep_calculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    #Make's sure user enters the correct input
    while keep_calculating not in ["y", "n"]:
        print(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    #Performs additional calculations
    while keep_calculating == "y":
        result = continue_calculating(result)
        keep_calculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        while keep_calculating not in ["y", "n"]:
            print(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    #Ends current calculation
    print("\n" * 100)
