#!/usr/bin/env python3
# report.py
#
# Exercise 2.4

import csv
import fileparse
import stock
import tableformat


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


def print_report(reportdata, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.HTMLTableFormatter()
    print_report(report, formatter)


def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfile pricefile')

    portfolio_report(argv[1], argv[2])


if __name__ == '__main__':
    import sys
    main(sys.argv)
