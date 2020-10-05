import csv
import os
import matplotlib.pyplot as plot
import math

counter = 0

l1 = []
l2 = []

for csvfile in os.listdir("."):
    if csvfile.endswith(".py"): continue
    counter += 6
    with open(csvfile) as file:
        su = 0
        ctr = 0
        for x in csv.reader(file):
            try:
                num = -float(x[1])
                print(num)
                su += num
                ctr += 1
            except:
                continue
        print(su)
        averarge = su / ctr
        l1.append(counter)
        l2.append(averarge)

plot.plot(l1, l2)
plot.show()
