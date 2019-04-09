from django.shortcuts import render
from articles.models import Article
from django.contrib.auth.decorators import login_required
from market.fusioncharts import FusionCharts
from market.fusioncharts import FusionTable
from market.fusioncharts import TimeSeries
from market.forms import DomesticSecurietiesForm, IndexSecurietiesForm
import market.graphcalcu as calcu
import market.models as stockmodel


@login_required(login_url="/accounts/login")
def chart(request):

    def dailydose(stock):
        return [
                stock[0].price,
                stock[1].price - stock[0].price,
                stock[0].volume,
                stock[0].low,
                stock[0].high
               ]


    articles = Article.objects.all().order_by('-date')
    dailydose = {
        'Barclays': dailydose(stockmodel.BarclaysDaily.objects.order_by('date')[:2]),
        'Bihl': dailydose(stockmodel.BihlDaily.objects.order_by('date')[:2]),
        'Choppies': dailydose(stockmodel.ChoppiesDaily.objects.order_by('date')[:2])
    }

    securities_selected = []
    securities_index_selected = []

    if request.method == "POST":
        domestic_form = DomesticSecurietiesForm(data=request.POST)
        index_form = IndexSecurietiesForm(data=request.POST)

        if index_form.is_valid():
            index_securities = {
                'i_barclays_checkbox': 'barclays',
                'i_bihl_checkbox': 'bihl',
                'i_choppies_checkbox': 'choppies',
                'i_cresta_checkbox': 'cresta',
                'i_engen_checkbox': 'engen',
                'i_fnbb_checkbox': 'fnbb',
                'i_furnmart_checkbox': 'furnmart',
                'i_g4s_checkbox': 'g4s',
                'i_letlole_checkbox': 'letlole',
                'i_letshego_checkbox': 'letshego',
                'i_minergy_checkbox': 'minergy',
                'i_nap_checkbox': 'nap',
                'i_olympia_checkbox': 'olympia',
                'i_primetime_checkbox': 'primetime',
                'i_rcdp_checkbox': 'rcdp',
                'i_sechaba_checkbox': 'sechaba',
                'i_seedco_checkbox': 'seedco',
                'i_sefalana_checkbox': 'sefalana',
                'i_stanchart_checkbox': 'stanchart',
                'i_turnstar_checkbox': 'turnstart'
            }

            for key in index_securities:
                if request.POST.get(key, False):
                    securities_index_selected.append(index_securities[key])

            print(securities_index_selected)

        if domestic_form.is_valid():
            domestic_securities = {
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

            for key in domestic_securities:
                if request.POST.get(key, False):
                    securities_selected.append(domestic_securities[key])

            print(securities_selected)

    else:
        domestic_form = DomesticSecurietiesForm()
        index_form = IndexSecurietiesForm()

        securities_selected.append('barclays')

    # Session it out
    if 'graphs' not in request.session:
        graphs = {
            'securities': securities_selected,
            'index': securities_index_selected
        }
        request.session['graphs'] = graphs
    else:

        if len(securities_selected) == 0:
            print("feel me")
            securities_selected = request.session['graphs']['securities']

        if len(securities_index_selected) == 0:
            securities_index_selected = request.session['graphs']['index']

        graphs = {
            'securities': securities_selected,
            'index': securities_index_selected
        }

        request.session['graphs'] = graphs

    print('Selected' + str(securities_selected))
    print('Index' + str(securities_index_selected))

    graph = calcu.graph(securities_selected, securities_index_selected)
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
    fcChart = FusionCharts("timeseries", "ex1", "100%", "50%", "chart", "json", timeSeries)

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'graphs/market.html', {
        'output': fcChart.render(),
        'chartTitle': "Line chart with time axis",
        'domesticform': domestic_form,
        'indexform': index_form,
        'selectedGraph': securities_selected,
        'Articles': articles,
        'daily': dailydose
    })
