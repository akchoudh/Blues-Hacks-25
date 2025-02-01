from fredapi import Fred
import pandas as pd
import matplotlib.pyplot as plt

#Our FRED API key
api_key = "********"
fred = Fred(api_key)  #Initializse Fred with our API key

class giveData:

    @staticmethod
    def exchange_rate(start_date, end_date):
        #Fetches the exchange rate using the 'DEXCAUS' series
        exchange_rate_data = fred.get_series('DEXCAUS', start_date, end_date)
        return exchange_rate_data


    @staticmethod
    def unemployment_rate(start_date, end_date):
        #Fetches Canada's unemployment rate
        unemployment_data = fred.get_series("LRUNTTTTCAM156S", start_date, end_date)
        return unemployment_data

    @staticmethod
    def cpi(start_date, end_date):
        #Fetches consumer price index
        cpi_data = fred.get_series("CPALTT01CAM659N", start_date, end_date)
        return cpi_data


    @staticmethod
    def housing_cost(start_date, end_date):
        #Fetches housing as a percent of 2010 prices
        housing_cost_data = fred.get_series("QCAN628BIS", start_date, end_date)
        return housing_cost_data

    @staticmethod
    def interest_rate(start_date, end_date):
        # Fetches BOC interest rate
        interest_rate_data = fred.get_series("IRLTLT01CAM156N", start_date, end_date)
        return interest_rate_data

    @staticmethod
    def export_value(start_date, end_date):
        #Fetches %of sales that are exports
        export_value_data = fred.get_series("XTEXVA01CAQ188S", start_date, end_date)
        return export_value_data


class graphData:
    data = giveData()

    def graph(self, func, start_date, end_date):

        #Fetches the data from function *func*
        series_data = func(start_date, end_date)

        #Avoids an error
        if series_data.empty:
            print("No data available for the specified time period.")
            return

        # Plotting the series
        plt.figure(figsize=(10, 5))
        series_data.plot()
        plt.title(f"{func.__name__.replace('_', ' ').capitalize()} from {start_date} to {end_date}")
        plt.xlabel("Date")
        plt.ylabel(func.__name__.replace('_', ' ').capitalize())
        plt.grid(True)
        plt.show()
graph = graphData()
graph.graph(graph.data.exchange_rate, "2022-01-01", "2023-01-01")
