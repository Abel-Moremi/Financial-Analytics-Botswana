from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from market.fusioncharts import FusionCharts
from market.fusioncharts import FusionTable
from market.fusioncharts import TimeSeries


# Testing things out
from market.resource import BarclaysDailyResource
from django.contrib.staticfiles.storage import staticfiles_storage
import json

@login_required(login_url="/accounts/login")
def chart(request):

    dataset_temp = BarclaysDailyResource().export().json
    data = str(dataset_temp)
    print(data)

    schema_data = open('C:/Users/Zozo/Google Drive/Semester 8/CSI408'
                       '/Project Source Code/financialanalyticsbotswana'
                       '/assets/schema.json', 'r')

    # path = staticfiles_storage.url('schema.json')
    # schema_data = open(path, 'r')

    schema = json.loads(schema_data.read())
    print(schema)


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
                                            prefix: '(t)'
                                            },
                                            title: 'Price Value'
                                        }]""")

    # Create an object for the chart using the FusionCharts class constructor
    fcChart = FusionCharts("timeseries", "ex1", "100%", "100%", "chart", "json", timeSeries)

     # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'graphs/market.html', {
        'output': fcChart.render(), 'chartTitle': "Line chart with time axis"})
