# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if isinstance(lines, str):
        raise RuntimeError("lines argument cannot be a filename (string)")

    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    rows = csv.reader(lines, delimiter=delimiter)

    if has_headers:
        # Read the file headers
        headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries.
    if select:
        indices = [ headers.index(colname) for colname in select ]
        headers = select
    else:
        indices = []
    
    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:     # Skip rows with no data
            continue
        # Filter the row if specific columns were selected
        if indices:
            row = [ row[index] for index in indices ]
        # Apply type casting if types were specified
        if types:
            try:
                row = [ func(val) for func, val in zip(types, row) ]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {rowno} : Couldn't convert {row}")
                    print(f"Row {rowno} : Reason {e}")

        if has_headers:
            # Make a dictionary
            record = dict(zip(headers,row))
        else:
            record = tuple(row)
        records.append(record)

    return records
