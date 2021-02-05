import csv
from decimal import *
from re import sub
import time
import pandas
import numpy as np
import matplotlib.pyplot as plt
import datetime
def main():
    print("test")
    with open('Yahoo-Finance-Scrape.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
#   double bottom is formed over 7 weeks
#   10 cents above middle peak
#   requires an up trend
#   the second bottom has to undercut the first bottom
#   peak between first bottom and second bottom
#   30% correction from highest peak 

#   if stock is upward trend then bullish market
#   if first bottom is low
#   if rallies up to high point
#   if declines back down pass the first bottom low
#   if rallies back up to the same high point as the first high price
#   and heavy volume of trades indicated big investors
#   if start buying once second rally is 10 cents above first rally
#   and hold
#   if price increase hold, sell once starts to decline 
    # x = min(Decimal(sub(r'[^\d.]', '', s)) for s in data)
    # x = min(float(s) for s in data)
    lowDataSet = []
    i= len(data) -1
    n = 0
    tic = time.perf_counter()
    while i > 0:
        lowDataSet.append([])
        lowDataSet[n].append(data[i][0])
        lowDataSet[n].append(Decimal(sub(r'[^\d.]', '', data[i][2])))
        n +=1
        i -=1
    toc = time.perf_counter()
    print(f"Time it took to fill list with data {toc - tic:0.4f}")
    x = [sub[0] for sub in lowDataSet]
    y = [sub[1] for sub in lowDataSet]

    plt.plot(x,y)
    plt.xticks(rotation=90)
    plt.show()
    
    tic = time.perf_counter()
    lowDataSet.sort(key = lambda x: x[1])

    toc = time.perf_counter()
    print(f"Time it took to sort data {toc - tic:0.10f}")



    
    
if __name__ == '__main__': main()