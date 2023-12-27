import math
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")
print()

#Takes the user's input and converts it to all lower case and removes spaces to avoid errors
option = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower().strip(" ")
print()
if option == "investment":
    #These questions collect the key variables as numbers for our formula later
    amount = int(input("How much money are you depositing? "))
    rate = float(input("What is the interest rate? "))
    #The rate is divided by 100 to turn it into a percentage
    rate = rate / 100
    years = int(input("How many years do you plan on investing? "))
    interest = input("Simple or Compound interest? ").lower().strip(" ")
    
    #this if/elif is within the previous one, as the user has selected "simple" or "compound" within the previous if/elif where they selected "investment" 
    #The simple interest formula
    if interest == "simple":
        total = amount *(1 + rate * years)
        #round the total to two decimal points and print
        total = str(round(total, 2))
        print()
        print (f"At the interest rate of {rate}%, at the end of {years} years you will get back £{total} ")

    #The compound interest formula
    elif interest == "compound":
        total = amount *math.pow((1 + rate), years )
        #round the total to two decimal points and print
        total = str(round(total, 2))
        print()
        print (f"At the interest rate of {rate}%, at the end of {years} years you will get back £{total} ")

elif option == "bond":
    #These questions collect the key variables as numbers for our formula later
    value = float(input("What is the total value of the property? "))
    rate = float(input("What is the interest rate? "))

    #The rate is divided by 100 to turn it into a percentage and then by 12 to get the monthly interest rate
    rate = (rate / 100) / 12
    month = int(input("How many months do you plan to take to repay the bond? "))

    #The bond repayment formula
    repayment = (rate * value) / (1 - (1 + rate) ** (-month))
    repayment = str(round(repayment, 2))
    print()
    print(f"At the interest rate of {rate}%, you will have a monthly repayment of £{repayment} ")

#If neither "investment" or "bond" are entered, the following error message will print
else:
    print("I'm sorry, that doesnt seem to be a valid option, please try again.")