import csv

from models import Portfolio


def import_shares_data(file) -> Portfolio:
    """Import shares data from a file and return three lists of names, prices, profits"""
    names, prices, profits = [], [], []
    with open(file, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            if row[0] != 'name':
                names.append(row[0])
            if row[1] != 'price':
                prices.append(float(row[1]))
            if row[2] != 'profit':
                profits.append(float(row[2]))
    market = Portfolio()
    market.add_shares_from_data(names, prices, profits)
    market.remove_ineffective_shares()
    return market
