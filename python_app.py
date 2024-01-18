# collect the necessary inputs: principal, annual interest rate,years
# calculate the amaunt of payment
# show to the user
def main():
    print("MONTHLY PAYMENT LOAN CALCULATOR")
    print("-------------------------------")
    principal = float(input("Input the loan amaunt: "))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Input the number of years: "))

    monthly_interest_rate = apr /1200
    amaunt_of_months = years * 12

    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amaunt_of_months))

    print("The monthly payment for this loan is: %.2f"%monthly_payment+"\n")
while True:
    main()