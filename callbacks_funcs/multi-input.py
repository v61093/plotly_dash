# Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
# import numpy as np
import pandas as pd

df = pd.read_csv('data/mpg.csv')

# app
app = dash.Dash()

features = df.columns

# Layout
app.layout = html.Div([
  html.Div([
    dcc.Dropdown(id='Xaxis',
                 options=[{
                   'label': i,
                   'value': i
                 } for i in features],
                 value='displacement')
  ],
           style={
             'width': '48%',
             'display': 'inline'
           }),
  html.Div([
    dcc.Dropdown(id='Yaxis',
                 options=[{
                   'label': i,
                   'value': i
                 } for i in features],
                 value='mpg')
  ],
           style={
             'width': '48%',
             'display': 'inline'
           }),
  dcc.Graph(id='feature-graphic'),
],
                      style={'padding': 10})


# call backs
@app.callback(
  Output(component_id='feature-graphic', component_property='figure'), [
    Input(component_id='Xaxis', component_property='value'),
    Input(component_id='Yaxis', component_property='value')
  ])
def update_fig(x_axis_name, y_axis_name):

  # Return output figure as a dictionary
  return {
    'data': [
      go.Scatter(
        x=df[x_axis_name],
        y=df[y_axis_name],
        text=df['name'],
        mode='markers',
      )
    ],
    'layout':
    go.Layout(title='My Dual Input Plot ',
              xaxis=dict(title=x_axis_name, type='log'),
              yaxis=dict(title=y_axis_name),
              hovermode='closest')
  }


# Run server
if __name__ == '__main__':
  app.run_server(host='0.0.0.0', debug=True)
