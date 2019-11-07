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

# Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='Non English Entries'


# Read in the data
df_f=pd.read_csv('Non_English.csv')
df_f['Ratio']=df_f['Non English']/df_f['Total']
df_f['Ratio_e']=df_f['English']/df_f['Total']
df_f['Ratio_m']=df_f['Mix']/df_f['Total']

# Set up the app
trace_ne=go.Scatter(x=df_f['Year'],
                 y=df_f['Ratio'],
                 mode='lines',
                 marker={'color':'#DC7633'},
                 name='Non_English')
trace_e=go.Scatter(x=df_f['Year'],
                 y=df_f['Ratio_e'],
                 mode='lines',
                 marker={'color':'#8E44AD'},
                 name='English')
trace_m=go.Scatter(x=df_f['Year'],
                 y=df_f['Ratio_m'],
                 mode='lines',
                 marker={'color':'#F1C40F'},
                 name='Two or more languages')


# Assign traces to Data
data=[trace_ne,trace_e,trace_m]
layout=go.Layout()
fig=go.Figure(data=data,layout=layout)

# Set up the layout
Euro_2_layout=html.Div(children=[
                        html.H3('The Ratio of Non English Entries'),
                        dcc.Graph(id='figure-1',
                                  figure=fig)])




if __name__ == '__main__':
    app.run_server()
