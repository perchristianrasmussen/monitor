import _csv as csv

import numpy as np

with open('eggs.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        print(row)
        print("phe2w")

