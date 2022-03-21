#!/usr/bin/env python3
# report.py
#
# Exercise 2.4

import csv
import fileparse


def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = fileparse.parse_csv(filename, select=['name', 'shares', 'price'], types=[str, int, float])

    return portfolio


def read_prices(filename):
    '''Reads the prices from a prices file'''
    pricelist = fileparse.parse_csv(filename, types=[str, float], has_headers=False) 
    prices = dict(pricelist)

    return prices


def make_report(portfolio, prices):
    '''Creates a report on the porfolio using prices'''
    report = []

    for share in portfolio:
        holding = (share['name'], share['shares'], prices[share['name']], (prices[share['name']] - share['price']))
        report.append(holding)

    return report


def print_report(report):
    '''Prints the report'''
    headers = ('Name', 'Shares', 'Price', 'Change')

    print('%10s %10s %10s %10s' % headers)
    print('---------- ' * len(headers))

    for name, shares, price, change in report:
        price_dollar = f'${price:.2f}'
        print(f'{name:>10s} {shares:>10d} {price_dollar:>10} {change:>10.2f}')

def portfolio_report(portfolio_csv, prices_csv):
    '''Processes a report on a portfolio using the portfolio and prices CSV files as input'''
    portfolio = read_portfolio(portfolio_csv)
    prices = read_prices(prices_csv)
    report = make_report(portfolio, prices)
    print_report(report)


def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfile pricefile')

    portfolio_report(argv[1], argv[2])


if __name__ == '__main__':
    import sys
    main(sys.argv)
