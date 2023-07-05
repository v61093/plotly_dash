import dash
import pandas as pd
# import numpy as np
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html

# app
app = dash.Dash()

df = pd.read_csv('OldFaithful.csv')
# X --> Duration of current erruption in minutes
# Y --> Working time until next erruption

data = [
  go.Scatter(x=df['X'],
             y=df['Y'],
             mode='markers',
             marker={
               # 'size': 12,
               'color': 'rgb(50,60,170)',
               'symbol': 'pentagon'
             })
]

layout = go.Layout(title='Old Faithful Erruption Intervals vs Durations',
                   xaxis={'title': 'Duration of Erruption (minites)'},
                   yaxis=dict(title='Interval to next erruption (minutes)'))

app.layout = html.Div(children=[
  dcc.Graph(id='Scatter PLot', figure={
    'data': data,
    'layout': layout
  })
])

if __name__ == '__main__':
  app.run_server(host='0.0.0.0', debug=True)