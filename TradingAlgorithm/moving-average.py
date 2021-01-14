#!/usr/bin/env python3

import platform
import datetime
from datetime import date
from random import randrange, uniform
from decimal import *
class Stock:
    def __init__(self, date, price):
        self._date = date
        self._price = price
    def getDate(self):
        return self._date
    def getPrice(self):
        return self._price
    def setDate(self,newDate):
        self._date=newDate
    def setPrice(self,newPrice):
        self._price = newPrice
    
    



def simpleMovingAverage(*args):
    (stock, number) = args
    n = 0
    totalPrice = 0
    while n < number:
        totalPrice += stock[n].getPrice()
        n+=1
    return round(totalPrice/number,2)
def getFormattedDate(date):
    return f"{getMonth(date.getDate().month)} {date.getDate().day} {date.getDate().year}"

def getMonth(month):
    if month==1:
        return "January"
    elif month == 2:
        return "February"
    elif month == 3:
        return "March"
    elif month == 4:
        return "April"
    elif month == 5:
        return "May"
    elif month == 6:
        return "June"
    elif month == 7:
        return "July"
    elif month == 8:
        return "August"
    elif month == 9:
        return "September"
    elif month == 10:
        return "October"
    elif month == 11:
        return "November"
    elif month == 12:
        return "December"
    else:
        return "Number must be between 1 and 12"

def generateDate(x):
    n = datetime.datetime.now()
    target = datetime.datetime.now() - datetime.timedelta(days=x)
    return target
def generatePrice():
    frand = uniform(0,2)
    return frand


def generateData():
    stockData =[]
    i = 1
    while i <= 200:
        stock = Stock(generateDate(i), generatePrice())
        stockData.append(stock)
        i+=1
    price = uniform((stockData[1].getPrice()*1.1), (stockData[1].getPrice()-(stockData[1].getPrice()*.1)))
    stockData[0] = Stock(generateDate(0), price)
    
    return stockData

def main():

    data = generateData()
    
    simpleFifty = simpleMovingAverage(data, 50)
    simpleTwoHundred = simpleMovingAverage(data, 200)
    simpleTen = simpleMovingAverage(data,10)
    print(f"Current price as of {getMonth(data[0].getDate().month)} {data[0].getDate().day} {data[0].getDate().year} ${data[0].getPrice():.2f}")
    print(f"Simple Moving Average for passed 10 days is {simpleTen:.2f}")
    print(f"Simple Moving Average for passed 50 days is {simpleFifty:.2f}")
    print(f"Simple Moving Average for passed 200 days is {simpleTwoHundred:.2f}")
    
    print()
    if simpleTen < simpleFifty and simpleFifty < simpleTwoHundred:
        print("This stock is on a downwards trend")
    elif simpleTen > simpleFifty and simpleFifty > simpleTwoHundred:
        print("This stock is on an upwards trend")
    elif simpleTen > simpleFifty and simpleFifty < simpleTwoHundred:
        print("This stock may be fluctuating because historical data indicates a downward trend")
    else:
        print("This stock may be fluctuating because historical data indicates a upward trend")


    print("End of program")
    
if __name__ == '__main__': main()
