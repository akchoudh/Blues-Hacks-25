from fredapi import Fred
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template
import io

#Our FRED API key
api_key = "*****"
fred = Fred(api_key)  #Initializse Fred with our API key

class giveData:

    @staticmethod
    def exchange_rate(start_date, end_date):
        exchange_rate_data = fred.get_series('DEXCAUS', start_date, end_date)
        return exchange_rate_data


    @staticmethod
    def unemployment_rate(start_date, end_date):
        unemployment_data = fred.get_series("LRUNTTTTCAM156S", start_date, end_date)
        return unemployment_data

    @staticmethod
    def cpi(start_date, end_date):
        #Consumer price index
        cpi_data = fred.get_series("CPALTT01CAM659N", start_date, end_date)
        return cpi_data


    @staticmethod
    def housing_cost(start_date, end_date):
        #Housing as a % of 2010 prices
        housing_cost_data = fred.get_series("QCAN628BIS", start_date, end_date)
        return housing_cost_data

    @staticmethod
    def interest_rate(start_date, end_date):
        interest_rate_data = fred.get_series("IRLTLT01CAM156N", start_date, end_date)
        return interest_rate_data

    @staticmethod
    def export_value(start_date, end_date):
        #%of sales that are exports
        export_value_data = fred.get_series("XTEXVA01CAQ188S", start_date, end_date)
        return export_value_data


class graphData:
    data = giveData()
    def graph(self, func, start_date, end_date):

        #Fetches the data from function *func*
        series_data = func(start_date, end_date)

        #Avoids an error
        if series_data.empty:
            print("Data is unavaliable for this time period.")
            return

        #Plots the series
        plt.figure(figsize=(10, 5))
        series_data.plot()
        plt.title(f"{func.__name__.replace('_', ' ').capitalize()} from {start_date} to {end_date}")
        plt.xlabel("Date")
        plt.ylabel(func.__name__.replace('_', ' ').capitalize())
        plt_path = "static/plot.png"
        plt.savefig(plt_path)
        plt.close()
        return plt_path

app = Flask(__name__)
graphObj = graphData()



#Associated with the url path "/", and handles the GET and POST (receive and send) methods.
@app.route("/", methods=["GET", "POST"])

def index():
    #Render user form
    return render_template("web.html")

#Here we only need to GET.
@app.route("/", methods=["GET"])
def plot_on_websie():
    #Whatever start/end date and function name we get from the website.
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    func_name = request.args.get("func_name")

    #Raise error in HTML.
    if None in (start_date, end_date, func_name):
        return "Error: arguments missing", 400

    #Maps function name to the function itself.
    map = {
        "exchange_rate": graph_obj.data.exchange_rate,
        "unemployment_rate": graph_obj.data.unemployment_rate,
        "cpi": graph_obj.data.cpi,
        "housing_cost": graph_obj.data.housing_cost,
        "interest_rate": graph_obj.data.interest_rate,
        "export_value": graph_obj.data.export_value
    }
    if func_name not in func_name:
        return "Error: arguments missing", 400

    func = map[func_name]
    path = graphObj.graph(func, start_date, end_date)

    if plt_path is None:
        return "Error: cannot generate graph", 500

    return send_file(plt_path, mimetype="image/png")




