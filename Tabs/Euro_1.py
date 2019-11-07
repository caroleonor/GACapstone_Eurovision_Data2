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

df=pd.read_excel('eurovision_song_contest.xlsx')
df2=df[(df['Edition']=='2019f')&(df['Jury or Televoting']=='J')]

options_list=list(df2['To country'].value_counts().sort_index().index)


'''
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='Eurovision 2019'
'''


Euro_1_layout=html.Div(children=[
    html.H3('2019 Jury Vote'),
    dcc.Dropdown(id='top10_dropdown',
                 options=[{'label': i, 'value': i} for i in options_list],
                 value='Please select a participating country'),
    html.Br(),
    dcc.Graph(id='display-map')
])

'''
@app.callback(Output('display-map','figure'),
              [Input('top10_dropdown','value')])

def pick_a_country(country_name):
    df_pick=df2[(df2['To country']==country_name)&(df2['Points']!=0)]

    fig = go.Figure(data=go.Choropleth(
        locations=df_pick['From country'], # Spatial coordinates
        z = df_pick['Points'], # Data to be color-coded
        locationmode = 'country names', # set of locations match entries in `locations`
        colorscale = 'ylgnbu',
        colorbar_title = 'Points of Giving',
))
    fig.update_layout(geo=dict(scope='world',
                           lataxis=dict(range=[30.0, 80.0]),
                           lonaxis=dict(range=[-20.0, 50.0])),
                autosize=False,width=1300,height=700)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
    '''
