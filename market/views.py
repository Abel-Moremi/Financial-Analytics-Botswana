from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from market.fusioncharts import FusionCharts
from market.fusioncharts import FusionTable
from market.fusioncharts import TimeSeries


# Testing things out
from market.resource import BarclaysDailyResource, BihlDailyResource
from django.contrib.staticfiles.storage import staticfiles_storage
import pandas as pd
import json
from jsonmerge import merge, Merger


@login_required(login_url="/accounts/login")
def chart(request):

    data_pd_01 = pd.read_json(BarclaysDailyResource().export().json, dtype={
        "date": str,
        "price": str
    })
    data_pd_02 = pd.read_json(BihlDailyResource().export().json, dtype={
        "date": str,
        "price": str
    })

    df_01 = pd.DataFrame(data_pd_01, columns=['date', 'price'], )
    df_01.set_index('date')
    df_02 = pd.DataFrame(data_pd_02, columns=['date', 'price'])
    df_02.set_index('date')
    new_df = df_01.merge(df_02, left_on='date', right_on='date', how='outer')

    # cols_to_keep = ['date', 'price_x', 'price_y']
    # new_df = new_df[cols_to_keep]
    new_df.set_index('date')

    export = new_df.to_json(orient='values')

    # print(export)

    #dataset_temp = BarclaysDailyResource().export().json
    dataset_temp = export
    data = dataset_temp

    schema_data = open('C:/Users/Zozo/Google Drive/Semester 8/CSI408'
                       '/Project Source Code/financialanalyticsbotswana'
                       '/assets/schema02.json', 'r')

    # path = staticfiles_storage.url('schema.json')
    # schema_data = open(path, 'r')


    schema = json.loads(schema_data.read())
    fusionTable = FusionTable(schema, data)
    timeSeries = TimeSeries(fusionTable)


    '''timeSeries.AddAttribute("caption", """{ 
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
                                        }]""")'''

    timeSeries.AddAttribute('chart', '{}')
    timeSeries.AddAttribute('caption', '{"text": "Botswana Stock Exchange Analysis"}')
    timeSeries.AddAttribute('subcaption', '{"text": "Stock Price"}')
    timeSeries.AddAttribute('timeseries', '"Type"')
    timeSeries.AddAttribute('yaxis', '[ {"plot": "Price", "title": "Price Value", "format": {"prefix": "(t)"}}]')

    # Create an object for the chart using the FusionCharts class constructor
    fcChart = FusionCharts("timeseries", "ex1", "100%", "80%", "chart", "json", timeSeries)

     # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'graphs/market.html', {
        'output': fcChart.render(), 'chartTitle': "Line chart with time axis"})
