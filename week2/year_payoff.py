'''
Finds the minimum monthly payment to pay off a balance with given apr, 
that is a multiple of 10
'''

def year_payoff(balance, apr):
    minimum_monthly_payment = 10
    remaining_balance = balance
    
    while remaining_balance > 0:
        for i in xrange(1, 13):
            subtracted_balance = remaining_balance - minimum_monthly_payment                
            remaining_balance = subtracted_balance + subtracted_balance * (apr / 12)
        if(remaining_balance > 0):
            remaining_balance = balance
            minimum_monthly_payment += 10
            
    return minimum_monthly_payment
    
print "Lowest payment: " + str(year_payoff(3329, 0.2)) # Expects 310
print "Lowest payment: " + str(year_payoff(4773, 0.2)) # Expects 440
print "Lowest payment: " + str(year_payoff(3926, 0.2)) # Expects 360