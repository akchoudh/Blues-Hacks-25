from fredapi import Fred
import pandas as pd


#Our FRED API key
api_key = "6b6db579163639914284f1e5729cc668"
fred = Fred(api_key)  #Initializse Fred with our API key

class giveData:

    @staticmethod
    def exchange_rate(start_date, end_date):
        #Fetches the exchange rate using the 'DEXCAUS' series
        exchange_rate_data = fred.get_series('DEXCAUS', start_date, end_date)
        return exchange_rate_data




print(giveData.exchange_rate("2010/1/1", "2025/1/31"))
