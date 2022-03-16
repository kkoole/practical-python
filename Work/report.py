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
            holding = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
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


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

report = make_report(portfolio, prices)
headers = ('Name', 'Shares', 'Price', 'Change')

print('%10s %10s %10s %10s' % headers)
print('---------- ' * len(headers))

for name, shares, price, change in report:
    price_dollar = f'${price:.2f}'
    print(f'{name:>10s} {shares:>10d} {price_dollar:>10} {change:>10.2f}')

#value = 0
#change = 0
#
#for share in portfolio:
#    share_change = prices[share['name']] - share['price']
#
#    value += prices[share['name']] * share['shares']
#    change += share_change * share['shares']
#
#print(f'Current value of portfolio ${value:0.2f}\nChange ${change:0.2f}')
