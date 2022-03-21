#!/usr/bin/env python3
# report.py
#
# Exercise 2.4

import csv
import fileparse
import stock


def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    with open(filename) as f:
        portdicts = fileparse.parse_csv(f, select=['name', 'shares', 'price'], types=[str, int, float])
    portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts ]

    return portfolio


def read_prices(filename):
    '''Reads the prices from a prices file'''
    with open(filename) as f:
        pricelist = fileparse.parse_csv(f, types=[str, float], has_headers=False) 
        prices = dict(pricelist)

    return prices


def make_report(portfolio, prices):
    '''Creates a report on the porfolio using prices'''
    report = []

    for stock in portfolio:
        stock_holding = (stock.name, stock.shares, prices[stock.name], (prices[stock.name] - stock.price))
        report.append(stock_holding)

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
