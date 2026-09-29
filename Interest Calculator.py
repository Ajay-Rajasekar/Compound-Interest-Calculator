# Compound Interest Calculator
principal = float(input("Enter the principal amount:"))
while principal < 0:
    print(f"Principal cannot be negative")
    principal = float(input("Enter the principal amount:"))

rate = float(input("Enter the rate of interest:"))
while rate < 0:
    print(f"rate cannot be negative")
    rate = float(input("Enter the rate of interest:"))

time = int(input("Enter the time in years:"))
while time < 0:
    print(f"Time cannot be negative")
    time = int(input("Enter the time in years:"))

amount = principal * pow(1 + rate/100,time)
print(f"The total amount in {time} years at the rate {rate}% : ${amount:,.2f}")