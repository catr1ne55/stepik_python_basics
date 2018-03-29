import csv

with open('Crimes.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    headers = reader[0]
    for row in reader:

