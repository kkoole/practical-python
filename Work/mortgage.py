# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months_paid = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if principal < payment:
        payment = principal
        principal = principal - payment
        total_paid = total_paid + payment
    elif (months_paid >= extra_payment_start_month and months_paid <= extra_payment_end_month):
        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + (payment + extra_payment)
    else: 
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    months_paid = months_paid + 1
    
    print(f'Month {months_paid}, paid ${total_paid:0.2f}, left ${principal:0.2f}')

print(f'Total paid ${total_paid:0.2f}\nMonths {months_paid}')
