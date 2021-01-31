'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

# Collecting the data
amount = float(input("Please enter your investment amount: "))
interest_rate = float(input("Please enter the interest rate in percentage: "))
years = float(input("Please tell us the number of years you wish to invest: "))

# Calculating the future value

final = amount * (1 + interest_rate / 100) ** years

# Printing the values to the console

print(f"If you invest ${amount:.2f} with an interest rate of {interest_rate}% over {years} years, your future value will be ${final:.2f}")