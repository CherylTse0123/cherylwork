#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# !/usr/bin/env python
# python3.7

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt
import tushare as ts
app = dash.Dash()
app.layout = html.Div([
    html.H1('股票图'),
    dcc.Dropdown(
        id = 'my-dropdown',
        options = [
            {'label': '爱柯迪', 'value': '600933'},
            {'label': '赣锋锂业', 'value': '002460'},
            {'label': '中国神华', 'value': '601088'},
            {'label': '广汽集团', 'value': '601238'},
            {'label': '春秋航空', 'value': '601021'},],
        value = '600933'),dcc.Graph(id='my-graph')])
@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
# df = web.DataReader(
#     selected_dropdown_value, data_source='yahoo',
#     start=dt(2018, 1, 1), end=dt.now()
# )
    df = ts.get_k_data(selected_dropdown_value, ktype='30')
    return {'data': [
    {
        'x': df.index,
        'y': df.close
    }
  ]
}
if __name__ == '__main__':
    app.run_server(host="0.0.0.0")