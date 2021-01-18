# Credit goes to Matt Button for helping me understand how to scrape using xpath and manipulate data. Visit his website at https://www.mattbutton.com/
# Credit goes to Debra Ray for helping me understand and provide headers when I scrape. Visit her website at https://debraray.medium.com/


from datetime import datetime,timedelta
import time
import requests, pandas, lxml, numpy
from lxml import html
import time

def format_date(date_datetime):
    date_timetuple = date_datetime.timetuple()
    date_mktime = time.mktime(date_timetuple)
    date_int = int(date_mktime)
    date_str = str(date_int)
    return date_str
def subdomain(symbol, start, end, filter="history"):
    subdoma = "/quote/{0}/history?period1={1}&period2={2}&interval=1d&filter={3}&frequency=1d"
    subdomain = subdoma.format(symbol, start, end, filter)
    return subdomain
def header_function(subdomain):
    hdrs = {"authority": "finance.yahoo.com",
        "method": "GET",
        "path":subdomain,
        "scheme": "https",
        "accept": "text/html",
        "accept-encoding":"gzip, deflate, br",
        "accept-language":"en-US,en;q=0.9",
        "cache-control": "no-cache",
        "dnt": "1",
        "pragma": "no-cache",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0;Win64)"
        }
    return hdrs

def scrape_page(url, header):
    page = requests.get(url, headers=header)
    element_html = html.fromstring(page.content)
    parsed_rows = []
    '''
        get headers of the data from yahoo finance
    '''
    table_headers = element_html.xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/thead/tr")  
    assert len(table_headers) > 0
    
    for table_header in table_headers:
        parse_header = []
        ele = table_header.xpath('./th')
        
        for ts in ele:
           (tex,) = ts.xpath('.//span/text()[1]')
           parse_header.append(tex)
           
        parsed_rows.append(parse_header)
    
    '''
        get data from table from yahoo finance
    '''
    table_rows = element_html.xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/tbody//tr")
    assert len(table_rows) > 0  
    for table_row in table_rows:
        parsed_row = []
        el = table_row.xpath('./td')
        
        none_count = 0
        for rs in el:
            try:
                (text,) = rs.xpath('.//span/text()[1]')
                parsed_row.append(text)
            except ValueError:
                parsed_row.append(numpy.NaN)
                none_count += 1
        if(none_count < 4):
            parsed_rows.append(parsed_row)
            
    
    return pandas.DataFrame(parsed_rows)



def main():   
    print("Executing Scrape.....")
    mainTic = time.perf_counter()
    
    dt_start = datetime.today() - timedelta(days=365)    
    dt_end = datetime.today()
    start = format_date(dt_start)
    end = format_date(dt_end)

    symbol = 'BTC-USD'
    sub = subdomain(symbol, start, end)
    header = header_function(sub)
    base_url = "https://finance.yahoo.com"
    url = base_url + sub
    
    #set up maximum rows and columns to display on pands
    pandas.options.display.max_rows = 150
    pandas.options.display.max_columns = 8
    
    tic = time.perf_counter()
    #Executes scrap on yahoo finanace
    df = scrape_page(url, header)
    print("Finsihed scraping website")
    toc = time.perf_counter()
    print(f"Time it took to scrape yahoo finance website {toc - tic:0.4f}")
    
    #Saves scrape to csv file format   
    df.to_csv('Yahoo-Finance-Scrape.csv', encoding='utf-8', index=False)
    print("Finsihed saving scrape to csv file")

    #Read from csv file format 
    path_to_file = "./Yahoo-Finance-Scrape.csv"
    df = pandas.read_csv(path_to_file, index_col=False,encoding="utf-8")
    print("Finsihed reading csv file")
    
    #Modifications to file including remove unnamed columns, columns 1,2,3,5, and 6
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df.drop(["1","2","3","5","6"], axis=1)
    
    #Delete first row
    df = df.iloc[1:,]
    
    #Modify column headings
    df = df.rename(columns={"0":"Date"})
    df = df.rename(columns={"4":"Closing Price"})
    print("Finsihed modifications of csv file")
    
    #Save to final file
    df.to_csv("Yahoo-Finance-Scrape.csv", index=False, encoding='utf-8')
    print("Finsihed writing modified csv file")
    
    mainToc = time.perf_counter()
    print(f"Time it took to complete creating dataset {mainToc - mainTic:0.4f}")
    
    
    
    
    


if __name__ == '__main__': main()