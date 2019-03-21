from django.shortcuts import render

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from market.fusioncharts import FusionCharts
from market.fusioncharts import FusionTable
from market.fusioncharts import TimeSeries
import requests

# Testing things out
from market.resource import BarclaysDailyResource
from django.contrib.staticfiles.storage import staticfiles_storage
import json


def chart(request):

    dataset_temp = BarclaysDailyResource().export().json
    data = str(dataset_temp)
    print(data)

    schema_data = open('C:/Users/Zozo/Google Drive/Semester 8/CSI408'
                       '/Project Source Code/financialanalyticsbotswana'
                       '/assets/schema.json', 'r')
    schema = json.loads(schema_data.read())
    print(schema)


    #data = requests.get('https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/line-chart-with-time-axis-data.json').text
    #schema = requests.get('https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/line-chart-with-time-axis-schema.json').text

    fusionTable = FusionTable(schema, data)
    timeSeries = TimeSeries(fusionTable)

    timeSeries.AddAttribute("caption", """{ 
                                        text: 'Stock Price Analysis'
                                        }""")

    timeSeries.AddAttribute("subcaption", """{ 
                                    text: 'Barclays'
                                    }""")

    timeSeries.AddAttribute("yAxis", """[{
                                            plot: {
                                            value: 'price',
                                            type: 'line'
                                            },
                                            format: {
                                            prefix: 'P'
                                            },
                                            title: 'Price Value'
                                        }]""")

    # Create an object for the chart using the FusionCharts class constructor
    fcChart = FusionCharts("timeseries", "ex1", 700, 450, "chart", "json", timeSeries)

     # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'graphs/market.html', {
        'output': fcChart.render(), 'chartTitle': "Line chart with time axis"})
