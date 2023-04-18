import csv

with open('electro.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)