import csv
import numpy as np

with open('name.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    coefficients = []
    results = []
    for row in csv_reader:
        calc = row[0] + "x"
        for column in row[1:-1]:
            if column[0] == "-":
                calc += column + "x"
                continue
            calc += "+" + column + "x"
        calc += "=" + row[-1]
        print(calc)

        line = []
        for column in row[0:-1]:
            line.append(int(column))
        coefficients.append(line)
        results.append(int(row[-1]))
    print("\n----------------")
    
    a = np.array(coefficients)
    b = np.array(results)
    x = np.linalg.solve(a,b)
    for num in range(len(row)-1):
        print('X' + str(num) + " = " + str(x[num]))