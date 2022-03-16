# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    'Calculates the total cost of a portfolio from CSV file'
    total_cost = 0

    f = open(filename, 'rt')
    headers = next(f).split(',')

    for line in f:
        row = line.split(',')

        try:
            total_cost = total_cost + (int(row[1]) * float(row[2]))
        except ValueError:
            print('That\'s an oopsie')

    f.close()

    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost {cost:0.2f}')
