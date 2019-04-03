from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from market.fusioncharts import FusionCharts
from market.fusioncharts import FusionTable
from market.fusioncharts import TimeSeries


# Testing things out
from market.resource import BarclaysDailyResource, BihlDailyResource
import pandas as pd
import json
import market.graphcalcu as calcu
from market.forms import DomesticSecurietiesForm


@login_required(login_url="/accounts/login")
def chart(request):

    '''data_pd_01 = pd.read_json(BarclaysDailyResource().export().json, dtype={
        "date": str,
        "price": str
    })
    data_pd_02 = pd.read_json(BihlDailyResource().export().json, dtype={
        "date": str,
        "price": str
    })

    df_01 = pd.DataFrame(data_pd_01, columns=['date', 'price'], )
    df_02 = pd.DataFrame(data_pd_02, columns=['date', 'price'], )
    new_df = df_01.merge(df_02, left_on='date', right_on='date', how='outer')
    new_df.set_index('date')

    export = new_df.to_json(orient='values')

    # print(export)

    #dataset_temp = BarclaysDailyResource().export().json
    dataset_temp = export
    data = dataset_temp

    schema_data = open('C:/Users/Zozo/Google Drive/Semester 8/CSI408'
                       '/Project Source Code/financialanalyticsbotswana'
                       '/assets/jsonschema/schema02.json', 'r')


    # path = staticfiles_storage.url('schema.json')
    # schema_data = open(path, 'r')


    schema = json.loads(schema_data.read())'''

    securities_selected = []

    if request.method == "POST":
        domestic_form = DomesticSecurietiesForm(data=request.POST)
        if domestic_form.is_valid():
            securities = {
                'd_barclays_checkbox': 'barclays',
                'd_bihl_checkbox': 'bihl',
                'd_choppies_checkbox': 'choppies',
                'd_cresta_checkbox': 'cresta',
                'd_engen_checkbox': 'engen',
                'd_fnbb_checkbox': 'fnbb',
                'd_furnmart_checkbox': 'furnmart',
                'd_g4s_checkbox': 'g4s',
                'd_letlole_checkbox': 'letlole',
                'd_letshego_checkbox':  'letshego',
                'd_minergy_checkbox': 'minergy',
                'd_nap_checkbox': 'nap',
                'd_olympia_checkbox': 'olympia',
                'd_primetime_checkbox': 'primetime',
                'd_rcdp_checkbox': 'rcdp',
                'd_sechaba_checkbox': 'sechaba',
                'd_seedco_checkbox': 'seedco',
                'd_sefalana_checkbox': 'sefalana',
                'd_stanchart_checkbox': 'stanchart',
                'd_turnstar_checkbox': 'turnstart'
            }

            for key in securities:
                if request.POST.get(key, False):
                    securities_selected.append(securities[key])

            print(securities_selected)
    else:
        domestic_form = DomesticSecurietiesForm()
        securities_selected.append('barclays')

    graph = calcu.graph(securities_selected)
    schema = graph[0]
    data = graph[1]

    fusionTable = FusionTable(schema, data)
    timeSeries = TimeSeries(fusionTable)

    timeSeries.AddAttribute('chart', '{}')
    timeSeries.AddAttribute('caption', '{"text": "Botswana Stock Exchange Analysis"}')
    timeSeries.AddAttribute('subcaption', '{"text": "Stock Price"}')
    timeSeries.AddAttribute('timeseries', '"Type"')
    timeSeries.AddAttribute('yaxis', '[ {"plot": "Price", "title": "Price Value", "format": {"prefix": "(t)"}}]')

    # Create an object for the chart using the FusionCharts class constructor
    fcChart = FusionCharts("timeseries", "ex1", "100%", "80%", "chart", "json", timeSeries)

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'graphs/market.html', {
        'output': fcChart.render(),
        'chartTitle': "Line chart with time axis",
        'domesticform': domestic_form,
        'selectedGraph': securities_selected
    })
