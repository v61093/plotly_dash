# Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
# import plotly.graph_objs as go
from dash.dependencies import Input, Output
# import numpy as np

# app
app = dash.Dash()

# Layout
app.layout = html.Div([
  dcc.Input(id='my-id', value='enter text here', type='text'),
  html.Div(id='my-div')
])


# call backs
@app.callback(Output(component_id='my-div', component_property='children'),
              [Input(component_id='my-id', component_property='value')])
def update_output_div(input_str):
  return f'You entered: {input_str}'


# Run server
if __name__ == '__main__':
  app.run_server(host='0.0.0.0', debug=True)

#***************************************************************
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

#***************************************************************

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

# ************************************************************

# RADIO-ITEMS

# Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
# import numpy as np
import pandas as pd
import base64


# function to get image
def encode_image(image_file):
  encoded = base64.b64encode(open(image_file, 'rb').read())
  return 'data:image/png;base64,{}'.format(encoded.decode())


df = pd.read_csv('data/wheels.csv')

# app
app = dash.Dash()

features = df.columns

# Layout
app.layout = html.Div([
  dcc.RadioItems(id='wheels',
                 options=[{
                   'label': i,
                   'value': i
                 } for i in df['wheels'].unique()],
                 value=1,
                 inline=True),
  html.Div(id='wheels-output'),
  html.Hr(),
  dcc.RadioItems(
    id='colors',
    options=[{
      'label': i,
      'value': i
    } for i in df['color'].unique()],
    value='red',
    inline=True,
  ),
  html.Div(id='colors-output'),
  html.Img(id='display-image', src='children', height=300)
])


# callbacks for wheels
@app.callback(
  Output(component_id='colors-output', component_property='children'),
  [Input('colors', 'value')])
def call_back_wheel(wheel_value):
  return f'You selected {wheel_value}'


# callback for colors
@app.callback(Output('wheels-output', 'children'), [Input('wheels', 'value')])
def call_back_color(color_value):
  return f'You selected {color_value}'


# call backs for image
@app.callback(Output('display-image', 'src'),
              [Input('wheels', 'value'),
               Input('colors', 'value')])
def callback_image(wheel, color):
  path = 'data/Images/'
  return encode_image(path + df[(df['wheels'] == wheel)
                                & (df['color'] == color)]['image'].values[0])


# Run server
if __name__ == '__main__':
  app.run_server(host='0.0.0.0', debug=True)

#****************************************************************
# SLIDERS

# Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
# import plotly.graph_objs as go
from dash.dependencies import Input, Output
# import numpy as np
import pandas as pd

# import base64


# function to get image
def encode_image(image_file):
  encoded = base64.b64encode(open(image_file, 'rb').read())
  return 'data:image/png;base64,{}'.format(encoded.decode())


df = pd.read_csv('data/wheels.csv')

# app
app = dash.Dash()

features = df.columns

# Layout
app.layout = html.Div([
  dcc.RangeSlider(min=-5, max=6, step=1, value=[-2, 1], id='my-range-slider'),
  html.Div(id='output'),
])


# call backs for image
@app.callback(Output('output', 'children'),
              [Input('my-range-slider', 'value')])
def update_output(value):
  return value[0] * value[1]


# Run server
if __name__ == '__main__':
  app.run_server(host='0.0.0.0', debug=True)

#**************************************************************

# STATE
# Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import pandas as pd

# app
app = dash.Dash()

# Layout
app.layout = html.Div([
  dcc.Input(id='input-in', value=1),
  html.Button(children='Submit', id='submit-val', n_clicks=0),
  html.H1(id='output-out')
])


# call backs for image
@app.callback(Output('output-out', 'children'),
              [Input('submit-val', 'n_clicks')], [State('input-in', 'value')])
def update_output(nclicks, number):
  return f'You have entered {number} and clicked submit button {nclicks} times'


# Run server
if __name__ == '__main__':
  app.run_server(host='0.0.0.0', debug=True)

# *************************************************************************

# hoverData

# Imports
import dash
from dash import dcc
from dash import html
# import plotly.graph_objs as go
from dash.dependencies import Input, Output
import json
import pandas as pd
import base64


# function to get image
def encode_image(image_file):
  encoded = base64.b64encode(open(image_file, 'rb').read())
  return 'data:image/png;base64,{}'.format(encoded.decode())


df = pd.read_csv('data/wheels.csv')

# app
app = dash.Dash()

# Layout
app.layout = html.Div([
  html.Div(dcc.Graph(
    id='wheel-plot',
    figure={
      'data':
      [go.Scatter(x=df['color'], y=df['wheels'], dy=1, mode='markers')],
      'layout': go.Layout(title='Test', hovermode='closest')
    }),
           style={
             'width': '30%',
             'float': 'left'
           }),
  # html.Div(
  # html.Pre(id='hover-data', style={'padding': 35}),
  html.Div(html.Img(id='hover-data', src='children', height=300),
           style={'paddingTop': 35})
])


# call backs for image
@app.callback(Output('hover-data', 'src'), [Input('wheel-plot', 'hoverData')])
def callback_img(hoverData):
  # return json.dumps(hoverData, indent=2)
  wheel = hoverData['points'][0]['y']
  color = hoverData['points'][0]['x']
  path = '/data/Images/'
  return encode_image(path + df[(df['wheels'] == wheel)
                                & (df['color'] == color)]['image'].values[0])


# Run server
if __name__ == '__main__':
  app.run_server(host='0.0.0.0', debug=True)

#****************************************************************************

# selectionData

# Imports
import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import json
import pandas as pd
import numpy as np
# import base64

app = dash.Dash()

# Create Data
np.random.seed(10)
x1 = np.linspace(0.1, 5, 50)
x2 = np.linspace(5.1, 10, 50)
y = np.random.randint(0, 50, 50)

# create DF
df1 = pd.DataFrame({'x': x1, 'y': y})
df2 = pd.DataFrame({'x': x1, 'y': y})
df3 = pd.DataFrame({'x': x2, 'y': y})

df = pd.concat([df1, df2, df3])

app.layout = html.Div([
  html.Div([
    dcc.Graph(id='plot',
              figure={
                'data': [go.Scatter(x=df['x'], y=df['y'], mode='markers')],
                'layout': go.Layout(title='Scatter Plot', hovermode='closest')
              })
  ],
           style={
             'width': '50%',
             'display': 'inline-block'
           }),
  html.Div([html.H1(id='density', style={'padding': 25})],
           style={
             'width': '50%',
             'display': 'inline-block'
           })
])


@app.callback(Output('density', 'children'), [Input('plot', 'selectedData')])
def find_density(selectedData):
  # calculate the density
  pts = len(selectedData['points'])
  rng_or_lassopoint = list(selectedData.keys())
  rng_or_lassopoint.remove('points')

  max_x = max(selectedData[rng_or_lassopoint[0]]['x'])
  min_x = min(selectedData[rng_or_lassopoint[0]]['x'])
  max_y = max(selectedData[rng_or_lassopoint[0]]['y'])
  min_y = min(selectedData[rng_or_lassopoint[0]]['y'])
  area = (max_x - min_x) * (max_y - min_y)
  d = pts / area
  return f'Density : {d:.2f}'


# Run server
if __name__ == '__main__':
  app.run_server(host='0.0.0.0', debug=True)

# ********************************************************************************

# Interaction with visualizations

# Imports
import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import json
import pandas as pd
import numpy as np
# import base64

app = dash.Dash()

# Create Data
df = pd.read_csv('data/mpg.csv')

# adding jitter(Noise)
df['year'] = np.random.randint(-4, 5, len(df)) * 0.1 + df['model_year']

app.layout = html.Div([
  html.Div([
    dcc.Graph(id='mpg-scatter',
              figure={
                'data': [
                  go.Scatter(x=df['year'] + 1900,
                             y=df['mpg'],
                             text=df['name'],
                             hoverinfo=['text', 'y', 'x'],
                             mode='markers')
                ],
                'layout':
                go.Layout(title='MPG Data',
                          xaxis=dict(title='year'),
                          yaxis=dict(title='MPG'),
                          hovermode='closest')
              })
  ],
           style={
             'width': '40%',
             'display': 'inline-block'
           }),
  html.Div([
    dcc.Graph(id='mpg-line',
              figure={
                'data': [go.Scatter(x=[0, 1], y=[0, 1], mode='lines')],
                'layout': go.Layout(title='Accelaration', margin={'l': 0})
              })
  ],
           style={
             'width': '30%',
             'display': 'inline-block'
           }),
  # html.Div(html.Pre(id='mpg-line', style={'padding': 35})),
  html.Div([dcc.Markdown(id='mpg-stats')],
           style={
             'width': '20%',
             'height': '50%'
           })
])


@app.callback(Output('mpg-line', 'figure'),
              [Input('mpg-scatter', 'hoverData')])
def call_back_graph(hoverData):
  # return json.dumps(hoverData, indent=2)
  v_index = hoverData['points'][0]['pointIndex']
  figure = {
    'data': [
      go.Scatter(x=[0, 1],
                 y=[0, 60 / df.iloc[v_index]['acceleration']],
                 mode='lines',
                 line={'width': 3 * df.iloc[v_index]['cylinders']})
    ],
    'layout':
    go.Layout(title=df.iloc[v_index]['name'],
              xaxis={'visible': False},
              yaxis={
                'visible': False,
                'range': [0, 60 / df['acceleration'].min()]
              },
              margin={'l': 0},
              height=300)
  }
  return figure


@app.callback(Output('mpg-stats', 'children'),
              [Input('mpg-scatter', 'hoverData')])
def callback_stats(hoverData):
  v_index = hoverData['points'][0]['pointIndex']
  stats = f'''
    {df.iloc[v_index]['cylinders']} cylinders
    {df.iloc[v_index]['displacement']}cc displacement
    
    0 to 60mph in {df.iloc[v_index]['acceleration']} seconds
  '''
  return stats


# Run server
if __name__ == '__main__':
  app.run_server(host='0.0.0.0', debug=True)

# *****************************************************************************

# Thsi project below is to show real time stock proce data for the stocks choosen, Unfortunately the code is not in sync and has some issues.
# We can use this code to understand how to connect to multiple functionalities with respective call backs.

# Imports
import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
# import json
import pandas as pd
# import numpy as np
import pandas_datareader as web
from datetime import datetime

nsdq = pd.read_csv('data/NASDAQcompanylist.csv')
nsdq.set_index('Symbol', inplace=True)
options = []
for tic in nsdq.index:
  my_dict = {}
  my_dict['label'] = str(nsdq.loc[tic]['Name']) + ' ' + tic
  my_dict['value'] = tic
  options.append(my_dict)
# app
app = dash.Dash()

app.layout = html.Div([
  html.Div([
    html.H1(children='Stock Ticker DashBoard'),
    dcc.Dropdown(
      id='my-stock-picker', options=options, value=['TSLA'], multi=True)
  ],
           style={
             'display': 'inline-block',
             'width': '30%'
           }),
  html.Div([
    html.H3('Enter a Stock Symbol'),
    dcc.DatePickerRange(id='my-date-picker-range',
                        min_date_allowed=datetime(1995, 8, 5),
                        max_date_allowed=datetime.today(),
                        start_date=datetime(2010, 1, 1),
                        end_date=datetime.today())
  ],
           style={'display': 'inline-block'}),
  html.Div([html.Button(id='submit-button', n_clicks=0, children='submit')],
           style={'display': 'inline-block'}),
  dcc.Graph(id='my-graph')
])


@app.callback(Output('my-graph', 'figure'), [
  State('my-stock-picker', 'value'),
  State('my-date-picker-range', 'start_date'),
  State('my-date-picker-range', 'end_date')
], [Input('submit-button', 'n_clicks')])
def update_graph(n_clicks, stock_ticker, start_date, end_date):
  start = datetime.strptime(start_date[:10], '%Y-%m-%d')
  end = datetime.strptime(end_date[:10], '%Y-%m-%d')

  traces = []
  for tic in stock_ticker:
    df = web.DataReader(tic, 'yahoo', start=start, end=end)
    traces.append({'x': df.index, 'y': df['Close'], 'name': tic})

  fig = {'data': traces, 'layout': go.Layout(title=stock_ticker)}
  return fig


# Run server
if __name__ == '__main__':
  app.run_server(host='0.0.0.0', debug=True)
