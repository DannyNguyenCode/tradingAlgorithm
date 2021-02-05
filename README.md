# TradingAlgorithm
<br>
## Working Pattern/Indicators <br>
* Moving Average
<br>
## How to Run
* Download from github
* Open in Python3 IDE/text editor
* Select pattern or indicator to run (Moving Average is only one completed)
* Enter SYMBOL of stock you wish to scrape
    * example scrapeModule.main('BB')
* Run program

## A rundown of how the program works

* Select a pattern/indicator program to run
* Once ran, it passes the symbol to the scrape module
* The scrape module then accesses yahoo finanace's website and collects the data
* Once data is scraped, it is stored in a variable using panda's dataframe, then data is saved into a .csv file
* Outputs of where currently scrape module is executing
* Once it is down, logic is used to determine and output trends from data collected