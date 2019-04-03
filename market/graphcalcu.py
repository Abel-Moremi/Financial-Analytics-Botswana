import market.resource as res
import pandas as pd
import json


def barclays_df():
    return data_to_df(pd.read_json(res.BarclaysDailyResource().export().json, dtype={
        "date": str, "price": int}))


def bihl_df():
    return data_to_df(pd.read_json(res.BihlDailyResource().export().json, dtype={
        "date": str, "price": int}))


def choppies_df():
    return data_to_df(pd.read_json(res.ChoppiesDailyResource().export().json, dtype={
        "date": str, "price": int}))


def data_to_df(data_pd):
    return pd.DataFrame(data_pd, columns=['date', 'price'])


def stock_df():
    return {'barclays': barclays_df(),
            'bihl': bihl_df(),
            'choppies': choppies_df(),
            }


def single_graph_schema(graphname):
    schema = '[{"name": "date","type": "date","format": "%Y-%m-%d"},' \
             ' {"name": "'+graphname+'","type": "number"}]'
    return json.loads(schema)


def double_graph_schema(graphname01, graphname02):
    schema = '[' \
             '{ "name": "date","type": "date","format": "%Y-%m-%d"}, ' \
             '{"name": "'+graphname01+'","type": "number"}, ' \
             '{"name": "'+graphname02+'","type": "number"}' \
             ']'
    return json.loads(schema)


def triple_graph_schema(graphname01, graphname02, graphname03):
    schema = '[' \
             '{ "name": "date","type": "date","format": "%Y-%m-%d"}, ' \
             '{"name": "'+graphname01+'","type": "number"}, ' \
             '{"name": "'+graphname02+'","type": "number"},' \
             '{"name": "'+graphname03+'","type": "number"}' \
             ']'
    return json.loads(schema)


def df_to_json(df):
    return df.to_json(orient='values')


def single_graph(graphs, df):
    return [single_graph_schema(graphs[0]), df_to_json(df)]


def double_graph(df_01, df_02, graphs):
    new_df = df_01.merge(df_02, left_on='date', right_on='date', how='outer')
    new_df.set_index('date')

    return [double_graph_schema(graphs[0], graphs[1]), df_to_json(new_df)]


def triple_graph(df_01, df_02, df_03, graphs):
    double_df = df_02.merge(df_03, left_on='date', right_on='date', how='outer')
    double_df.set_index('date')
    triple_df = df_01.merge(double_df, left_on='date', right_on='date', how='outer')
    triple_df.set_index('date')

    return [triple_graph_schema(graphs[0], graphs[1], graphs[2]), df_to_json(triple_df)]


def graph(selected_graphs):

    if len(selected_graphs) == 2:
        return double_graph(stock_df()[selected_graphs[0]], stock_df()[selected_graphs[1]], selected_graphs)

    elif len(selected_graphs) == 3:
        return triple_graph(stock_df()[selected_graphs[0]], stock_df()[selected_graphs[1]],
                            stock_df()[selected_graphs[2]], selected_graphs)

    return single_graph(selected_graphs, stock_df()[selected_graphs[0]])

