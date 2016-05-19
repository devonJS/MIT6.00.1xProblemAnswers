'''
Using bisection method to find the monthly payment to pay off the balance
over the year given apr, within 10 cents error
'''

def bisection_year_payoff(balance, apr):
    low = round(balance / 12, 2)
    high = round((balance * ((1 + (apr / 12)) ** 12)) / 12, 2)    
    remaining_balance = balance
    epsilon = .1
    minimum_monthly_payment = (high + low) / 2
    
    while remaining_balance > 0 or remaining_balance < -epsilon:
        minimum_monthly_payment = (high + low) / 2
        for i in xrange(1, 13):
            subtracted_balance = remaining_balance - minimum_monthly_payment
            remaining_balance = subtracted_balance + subtracted_balance * (apr / 12)
        
        if remaining_balance > 0:
            low = round(minimum_monthly_payment, 2)
            remaining_balance = balance
        elif remaining_balance < -epsilon:
            high = round(minimum_monthly_payment, 2)
            remaining_balance = balance
    
    return round(minimum_monthly_payment, 2)

print "Lowest payment: " + str(bisection_year_payoff(320000, 0.2)) # Expects 29157.09
print "Lowest payment: " + str(bisection_year_payoff(999999, 0.18)) # Expects 90325.03