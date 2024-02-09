# This program will allow a user to choose between 1 of 2 calculators
# Investment Calculator: Calculates the amount of interest earned based on
# The user's deposit, interest rate, and investment period.
# Bond Calculator: Computes the monthly repayment amount for a home loan
# Based on the house value, interest rate, and repayment period.

import math

print("Hello, please choose one of the calculators listed below: ") # Welcome message and ask user to choose from one calculator below
print() # Blank line for presentation

while True:
    print("Investment - To calculate the amount of interest you'll earn on your investment") # Definition for investment calculator
    print("Bond - To calculate the amount you'll have to pay on a home loan\n") # Definition for Bond calculator
    choice = "Please select either Investment or Bond to continue: " # User input their choice of calculators
    
    # Replace and lower function input so program still works regardless of case sensitivity and spaces
    selection = input(choice).lower().replace(" ", "") 

    
    # Conditional statement to determine output actions depending on users choice
    if selection == "investment":
        print("Thank you for choosing the investment calculator") # Print confirmation Investment calculator was chosen
        
        deposit = float(input("Please enter the amount you would like to invest: ")) # Ask user to input investment deposit
        interest_rate = float(input("Please enter the interest rate: ")) # Ask user to specify interest rate
        time_of_investment = int(input("Please enter the number of years you would like to invest: ")) # Ask user confirm the number of years they would like to invest
        interest = input("Please choose either simple or compound interest: ") # Ask user to choose between simple or compound interest
    
        if interest == "simple": # Indented conditional statement if simple interest is chosen
            simple_total = deposit*(1 + interest_rate/100*time_of_investment) # Formulae for simple interest
            print(f"At the end of the term your investment will be worth £{simple_total}") # Print investment value at the end of the term
            break # Break loop

        elif interest == "compound": # Indented conditional statement if compound interest is chosen
            compound_total = round(deposit*math.pow((1+interest_rate/100),time_of_investment), 2) # Formulae for compound interest
            print(f" At the end of the term your investment will be worth £{compound_total}") # Print investment value at the end of the term
            break

    elif selection == "bond": # Indented conditional statement if Bond calculator is chosen
        print() # Blank line for presentation
        print("Thank you for choosing the bond calculator") # Print confirmation that Bond calcualtor was chosen
        
        house_value = float(input("Please enter the value of your house: ")) #Ask user to input house value
        house_interest = float(input("Please enter the interest rate: ")) # Ask user to input interest rate
        length_of_bond = int(input("Please enter the number of months to repay the bond: ")) # Ask user to input length left to repay bond
        repayment_amount = round((house_interest/100/12 * house_value) / (1 - (1 + house_interest/100/12)**(-length_of_bond)), 2) # Formulae for bond repayment
        
        print(f"Your monthly repayment amount for the home loan will be £{repayment_amount}") # Print monthly repayment for legnth of the term
        break # Break loop



    else: 
        print("Sorry, invalid input please choose again") # If none of the 3 options above is chosen display error message