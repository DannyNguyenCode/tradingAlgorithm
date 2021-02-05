#!/usr/bin/env python3

import platform
import datetime
from datetime import date
from random import randrange, uniform
from decimal import *
from re import sub
import scrapeModule
import csv

'''
    class to hold stock data
    this includes price and dates
    this class will be put into a list which can be used to calculate moveing average  
'''
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
    
    
'''
    Simple Moving Average function
    Takes a list containing multiple classes of stock and the number of days we want to go back
    Calculation is as follows:
        Iterate through list of stocks and add all their prices together
        Take total price and divide by number of days
    Number of days is how far back we want to go to get the smooth factor (200 days or 10 days)
    
'''
def simpleMovingAverage(*args):
    (stock, number) = args
    n = 0
    totalPrice = 0
    while n < number:
        totalPrice += stock[n].getPrice()
        n+=1
    return round(totalPrice/number,2)

'''
    format datetime into easier format for to read
    takes a datetime object and translates it into the following format:
        Month day, year
'''
def getFormattedDate(date):
    return f"{getMonth(date.getDate().month)} {date.getDate().day} {date.getDate().year}"

'''
    takes datetime month (by default it is a number between 1 and 12) and returns a string
'''
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

'''
    used to generate date between now and amount of days to go back
    if we pass the number 200 to function, it will return the date that was 200 days from today
'''
def generateDate(x):
    n = datetime.datetime.now()
    target = datetime.datetime.now() - datetime.timedelta(days=x)
    return target

'''
    used to generate random price for testing before obtaining a data set
'''
def generatePrice():
    frand = uniform(0,2)
    return frand

'''
    used to generate random classes of stock and returns a list
'''
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
    
    scrapeModule.main('BB')
    with open('Yahoo-Finance-Scrape.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    
    n = 1
    stock =[]
    while n < len(data):
        stock.append(Stock(data[n][0], Decimal(sub(r'[^\d.]', '', data[n][3]))))
        n += 1
  
    
    simpleFive = simpleMovingAverage(stock, 5)
    simpleTen = simpleMovingAverage(stock,10)
    simpleTwenty = simpleMovingAverage(stock,20)
    simpleOneHundred = simpleMovingAverage(stock, 99)
    print()
    print("Loading data analysis for stock.....")
    print(f"Current price as of {stock[0].getDate()} ${stock[0].getPrice():.2f} with a $5+- give or take")
    print(f"Simple Moving Average for passed 5 days is {simpleFive:.2f}")
    print(f"Simple Moving Average for passed 10 days is {simpleTen:.2f}")
    print(f"Simple Moving Average for passed 20 days is {simpleTwenty:.2f}")
    print(f"Simple Moving Average for passed 100 days is {simpleOneHundred:.2f}")
    
    
    print()
    print("Loading analysis of data......")
    if simpleFive < simpleTen and simpleTen < simpleTwenty:
        print("This stock is on a downwards trend")
    elif simpleFive > simpleTwenty and simpleTen > simpleTwenty:
        print("This stock is on an upwards trend")
    elif simpleFive > simpleTen and simpleTen < simpleTwenty:
        print("This stock may be fluctuating because historical data indicates a downward trend")
    else:
        print("This stock may be fluctuating because historical data indicates a upward trend")
        
    print()
    print("End of program")
    
if __name__ == '__main__': main()
