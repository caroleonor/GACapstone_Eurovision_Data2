import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path
import plotly as py
import numpy as np
from Tabs import Euro_1
from Tabs import Euro_2

df=pd.read_excel('eurovision_song_contest.xlsx')
df2=df[(df['Edition']=='2019f')&(df['Jury or Televoting']=='J')]


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='Eurovision Song Contest Data'
app.config['suppress_callback_exceptions'] = True


#### Page Layout
app.layout=html.Div([
    html.Br(),
    html.H2 ('Eurovision Song Contest Data'),
    html.Br(),
    html.Br(),
    dcc.Tabs(id='Euro_Tabs',value='Euro_1',children=[
        dcc.Tab(label='2019 DataFrame',value='Euro_1'),
        dcc.Tab(label='1956-2019 DataFrame',value='Euro_2'),
    ]),
    html.Div([
        html.Div(id='Tabs-content'),],className='twelve columns',style={'marginBottom':50,'marginTop':25}),
    html.Div([
        html.A('see the code',href='https://github.com/caroleonor/GACapstone_Eurovision_Data'),
        html.Br(),
        html.A('data source',href='https://en.wikipedia.org/wiki/Eurovision_Song_Contest_2019')]),

])

#### callback
@app.callback(Output('Tabs-content','children'),
              [Input('Euro_Tabs','value')])
def pick_page(tab):
    if tab=='Euro_1':
        return Euro_1.Euro_1_layout
    else:
        return Euro_2.Euro_2_layout

#### Tab 1 callback
@app.callback(dash.dependencies.Output('display-map','figure'),
              [dash.dependencies.Input('top10_dropdown','value')])
def pick_a_country(country_name):
    df_pick=df2[(df2['To country']==country_name)&(df2['Points']!=0)]
    fig = go.Figure(data=go.Choropleth(
        locations=df_pick['From country'],
        z = df_pick['Points'],
        locationmode = 'country names',
        colorscale = 'ylgnbu',
        colorbar_title = 'Points of Giving',
))
    fig.update_layout(geo=dict(scope='world',
                           lataxis=dict(range=[30.0, 80.0]),
                           lonaxis=dict(range=[-20.0, 50.0])),
                autosize=False,width=1300,height=700)
    return fig

#### Tab 2 callback
'''@app.callback(dash.dependencies.Output('page_1_content','children'),
              [dash.dependencies.Input('page-1-dropdown','value')])'''




if __name__ == '__main__':
    app.run_server(debug=True)
