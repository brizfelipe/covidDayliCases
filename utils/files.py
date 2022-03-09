
from posixpath import split
import sys
import csv
import os 


def readCSV(file):
    maxInt = sys.maxsize
    while True:
        try:
            csv.field_size_limit(maxInt)
            break
        except OverflowError:
            maxInt = int(maxInt/10)

    results = []

    with open(file, encoding="utf-8") as inFile:
        reader = csv.reader(inFile,delimiter=';')
        data = [row[0].split(',') for row in reader]
        results.append(data[1:])

        print('Arquivo' + file + ' baixado')

        return results[0]