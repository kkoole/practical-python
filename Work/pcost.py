# pcost.py
#
# Exercise 1.27

import sys
import csv
import report


def portfolio_cost(filename):
    'Calculates the total cost of a portfolio from CSV file'
    total_cost = 0

    portfolio = report.read_portfolio(filename)

    for holding in portfolio:
        total_cost += holding['shares'] * holding['price']
            
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost {cost:0.2f}')
