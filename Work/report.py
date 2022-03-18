# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            holding = {'name': record['name'], 'shares': int(record['shares']), 'price': float(record['price'])}
            portfolio.append(holding)

    return portfolio


def read_prices(filename):
    '''Reads the prices from a prices file'''
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) < 2:
               pass 
            else:
                prices[str(row[0])] = float(row[1])

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


portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
