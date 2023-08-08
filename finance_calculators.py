#This program allows the user to access two different ﬁnancial calculators: either investment or home loan repayment

#Adding colours to the display options
GREEN = '\033[92m'
RED = '\033[91m'
WHITE = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

#Importing library to support calculators' operations
import math

#?Displaying main menu
print(f"{GREEN}{BOLD}╔═════════════════════════════════════════════════════════════════════════════════════╗")
print(f"║   {WHITE}Choose either 'investment' or 'bond' from the menu below to proceed:              {GREEN}{BOLD}║")
print(f"║   {WHITE}{BOLD}{UNDERLINE}investment{WHITE} - to calculate the amount of interest you'll earn on your investment   {GREEN}{BOLD}║")
print(f"║   {WHITE}{BOLD}{UNDERLINE}bond{WHITE}       - to calculate the amount you'll have to pay on a home loan            {GREEN}{BOLD}║")
print(f"╚═════════════════════════════════════════════════════════════════════════════════════╝")

#Getting user's choice
calculator_choice = input(f"\n{WHITE}Type your choice here: ").upper()

while True:
    #Checking user's choice is a valid one
    if calculator_choice == 'INVESTMENT' or calculator_choice == 'BOND':

        if calculator_choice == 'INVESTMENT':

            #Getting input from the user
            deposit = float(input("How much money do you wish to deposit? "))
            annual_interest_rate = float(input("At what interest (%) rate? "))
            investment_years = int(input("How many years are you planning on investing with us? "))
            interest = input(f"Do you want {BOLD}{UNDERLINE}'simple'{WHITE} or {BOLD}{UNDERLINE}'compound'{WHITE} interest? ").upper()
            r = annual_interest_rate / 100

            if interest == 'SIMPLE' or interest == 'COMPOUND':

                if interest == 'SIMPLE':
                    total_amount = deposit * (1 + r * investment_years)
                    print(f"\nThe total amount once the simple interest has been applied is {GREEN}{BOLD}{UNDERLINE}{total_amount}")
                    break

                elif interest == 'COMPOUND':
                    total_amount = deposit * math.pow((1 + r), investment_years)
                    print(f"\nThe total amount once the compound interest has been applied is {GREEN}{BOLD}{UNDERLINE}{round(total_amount, 2)}")
                    break

            else:
                print(f"{RED}{BOLD}{UNDERLINE}Invalid input!{WHITE}\nLet's start again...\n")
                continue

        elif calculator_choice == 'BOND':

            #Getting input from the user
            house_value = float(input("What's is the current value (in sterling pounds) of your house? "))
            annual_interest_rate = float(input("What annual interest (%) rate applies to your loan? "))
            months_to_repay = int(input("How many months would take you to pay back the loan? "))

            i = annual_interest_rate / 100
            i = i / 12
            monthly_repayment = (i * house_value) / (1 - (1 + i) ** (-months_to_repay))

            print(f"\nYour monthly repayment would be {GREEN}{BOLD}{UNDERLINE}£{round(monthly_repayment, 2)}")
            break

        else:

            print(f"{RED}{BOLD}{UNDERLINE}Invalid input!{WHITE}\nLet's start again...\n")
            continue

    else:
        print(f"{RED}{BOLD}{UNDERLINE}Invalid input!\n")
        calculator_choice = input(f"{WHITE}Please choose between {BOLD}{UNDERLINE}investment{WHITE} or {BOLD}{UNDERLINE}bond{WHITE} to proceed: ").upper()
        continue