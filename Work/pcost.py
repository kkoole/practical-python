# pcost.py
#
# Exercise 1.27

import sys
import csv


def portfolio_cost(filename):
    'Calculates the total cost of a portfolio from CSV file'
    total_cost = 0

    f = open(filename, 'rt')
    rows = csv.reader(f)
    headers = next(rows)

    for row in rows:
        try:
            total_cost = total_cost + (int(row[1]) * float(row[2]))
        except ValueError:
            print('That\'s an oopsie')

    f.close()

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost {cost:0.2f}')
