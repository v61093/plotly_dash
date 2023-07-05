# GDP PER CAPITA vs LIFE EXPECTANY (SCATTER PLOT + DROPDOWN)

# Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
# import numpy as np
import pandas as pd

df = pd.read_csv('data/gapminderDataFiveYear.csv')

# app
app = dash.Dash()

year_options = []
for year in df['year']:
  year_options.append({'label': str(year), 'value': year})

app.layout = html.Div([
  dcc.Graph(id='graph'),
  dcc.Dropdown(id='year-picker', options=year_options, value=df['year'].min())
])


# call backs
@app.callback(Output(component_id='graph', component_property='figure'),
              [Input(component_id='year-picker', component_property='value')])
def update_fig(selected_year):

  # Data for only selected year from the dropdown
  filtered_df = df[df['year'] == selected_year]

  traces = []
  for contient_name in filtered_df['continent'].unique():
    df_by_continent = filtered_df[filtered_df['continent'] == contient_name]
    traces.append(
      go.Scatter(x=df_by_continent['gdpPercap'],
                 y=df_by_continent['lifeExp'],
                 mode='markers',
                 opacity=0.7,
                 name=contient_name))
  # Return output figure as a dictionary
  return {
    'data':
    traces,
    'layout':
    go.Layout(title='My Scatter Plot',
              xaxis=dict(title='GDP per Capita', type='log'),
              yaxis=dict(title='Life Expectancy'))
  }


# Run server
if __name__ == '__main__':
  app.run_server(host='0.0.0.0', debug=True)