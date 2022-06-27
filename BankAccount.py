from datetime import date

# This program calculates the accumulated interest over a time of 12 months.

# Programmer Information
# Name: FNU Tripti
# A-ID: A20503656
# Course: ITMD-513
# Date: 06/25/2022
# Lab #: 3

print("This program for course ITMD-513 is executed by FNU Tripti (A20503656) on : ", date.today())


# Declaration of function to calculate the interest and the total amount
def calculate_bank_balance():
    # Declaration and initialization of variables to store the bank balance
    bank_balance = 0.0
    bank_balance_grad = 0.0

    # Declaration and initialization of the variable to store the rate of Interest
    rate_of_interest = 0.0
    rate_of_interest_grad = 0.0

    # Prompt user to enter the opening account balance
    print("Please enter the opening balance :")

    bank_balance = float(input())
    bank_balance_grad = bank_balance

    # Prompt the user enter the rate of Interest
    print("Enter the Rate of Interest as a decimal")

    rate_of_interest = float(input())
    rate_of_interest_grad = rate_of_interest

    print("The Opening account balance entered is $%.2f" % bank_balance)
    print("The Rate of Interest enter is %.2f p.a." % rate_of_interest)

    # Calculation of Interest every month and accumulated balance
    # Starting the for loop to run iterations for 12 months of a year
    for x in range(1, 13):
        bank_balance = bank_balance + (bank_balance * rate_of_interest / 12)
        print("Month: ", x, "\t New monthly bal: $%.2f" % bank_balance)

    # Printing Summary as part of Grad work
    print()
    print("Grad Work")
    print("Summary of the program:")
    print("  Month #\t\tInterest Amt\t\t Balance")
    for z in range(1, 13):
        accumulated_interest = (bank_balance_grad * rate_of_interest_grad / 12)
        bank_balance_grad = bank_balance_grad + accumulated_interest
        print("\t", z, "\t\t\t $%.2f" % accumulated_interest, "\t\t\t\t $%.2f" % bank_balance_grad)


# Declaration of variable to store decision of PIN Entering
success = False

# Declaration of variable to store the 4 digit bank PIN Code
bankPinCode = "ft90"

# For loop to implement the correct pin with 3 retries
for y in range(1, 4):
    print("Please enter the 4 digit (alphanumeric) PIN : ")
    enteredPin = input()

    if bankPinCode == enteredPin:
        success = True
        break
    else:
        if y < 3:
            print("PIN entered does not match our records. Please try again.")
            print("Number of retries left are : ", 3 - y)
        else:
            print("3 tries have failed, Please contact system administrator.")

# Calling the method that calculates interest and total amount on the basic of the success variable.
if success:
    calculate_bank_balance()
