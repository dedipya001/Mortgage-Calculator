
months = int(input("Enter mortgage term (in months): "))
rate = float(input("Enter interest rate: "))
loan = float(12input("Enter loan value: "))

monthly_rate = rate / 100 / 12
payment = (monthly_rate / (1 - (1 + monthly_rate)**(-months))) * loan

print ("Monthly payment for a $%.2f %s year mortgage at %.2f%% interest rate is: $%.2f" % (loan, (months / 12), rate, payment))