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
        data = [row[0] for row in reader]
        results.append(data[1:])

        print('Arquivo' + file + ' baixado')

        return results[0]
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
        data = [row[0] for row in reader]
        results.append(data[1:])

        print('Arquivo' + file + ' baixado')

        return results[0]


def saveCSVFile(path,nameFile,fileLista):
    with open(path+'\\'+nameFile,mode='w',encoding='utf-8',newline='\n') as f:
        try :
            for row in fileLista:
                f.write(str(row)+'\n')
        except:
            return -1
    return 1