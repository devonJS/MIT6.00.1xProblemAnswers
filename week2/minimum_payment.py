'''
Given int or float, balance, apr and minimum_monthly_rate, 
this function prints your monthly minimum payment, and remaining balance
assuming you pay the minimum payment and interest is added on a month to month basis
'''

def minimum_payment(balance, apr, minimum_monthly_rate):
    total_paid = 0
    for i in xrange(1, 13):
        minimum_payment = balance * minimum_monthly_rate
        balance = (balance - minimum_payment)
        remaining_balance = balance + (balance * (apr / 12))
        balance = remaining_balance
        
        print "Month: " + str(i)
        print "Minimum monthly payment: " + str(round(minimum_payment, 2))
        print "Remaining balance: " + str(round(remaining_balance, 2))
        
        total_paid += minimum_payment
    
    print "Total paid: " + str(round(total_paid, 2))
    print "Remaining balance: " + str(round(remaining_balance, 2))

minimum_payment(4213, 0.2, 0.04)
minimum_payment(4842, 0.2, 0.04)