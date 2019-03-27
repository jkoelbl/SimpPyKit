import csv

def load(filename, columns=[], rows=[], headers=True, grouped=True, delimiter=',', quotechar='\"'):
    rows = {r for r in rows}
    with open(filename, newline='') as f:
        reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
        # get headers
        if headers:
            col_names = next(reader)
            if len(columns):
                col_names = [col_names[col] for col in columns]
        # get data
        if len(columns) and len(rows):  data = [[row[col] for col in columns] for row in reader if row in rows]
        elif len(columns):              data = [[row[col] for col in columns] for row in reader]
        elif len(rows):                 data = [row for row in reader if row in rows]
        else:                           data = [row for row in reader]
    return col_names, data

def save(filename, headers=[], data=[], delimiter=',', quotechar='\"', quoting=csv.QUOTE_MINIMAL):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=delimiter, quotechar=quotechar, quoting=quoting)
        if len(headers):
            writer.writerow(headers)
        [writer.writerow(row) for row in data]

def append(filename, data=[], delimiter=',', quotechar='\"'):
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f, delimiter=delimiter, quotechar=quotechar, quoting=quoting)
        [writer.writerow(row) for row in data]
