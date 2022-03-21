#!/usr/bin/env python3
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

    for stock in portfolio:
        total_cost += stock.shares * stock.price
            
    return total_cost


def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfile')
    
    cost = portfolio_cost(argv[1])
    print(f'Total cost {cost:0.2f}')


if __name__ == '__main__':
    import sys
    main(sys.argv)
