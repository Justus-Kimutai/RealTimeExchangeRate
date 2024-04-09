# A program to get Stock exchange world wide

import urllib.request
import json

API_KEY = 'CE9195TD0IOQFTOR'


#Data provided for free by Alpha Vantage. 
# url sample = http://<www.alphavantage.co/query?parameter=value>

def getStockExchange(country1,country2):
    fullURL ='https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency='+country1+'&to_currency='+country2+'&apikey='+API_KEY
   
   #request to alphavantage
    connection = urllib.request.urlopen(fullURL)
    stockExchangeString = connection.read().decode()
    stockExchangeDict = json.loads(stockExchangeString)

    ExchangeRateDict = stockExchangeDict['Realtime Currency Exchange Rate']

    return stockExchangeDict






