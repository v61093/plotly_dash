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
  encoded=base64.b64encode(open(image_file,'rb').read())
  return 'data:image/png;base64,{}'.format(encoded.decode())  

df = pd.read_csv('data/wheels.csv')

# app
app = dash.Dash()

features = df.columns

# Layout
app.layout = html.Div([
    dcc.RadioItems(id='wheels',
                   options = [{'label': i,'value':i} for i in df['wheels'].unique()],
                   value = 1,
                   inline=True),
    html.Div(id='wheels-output'),
    html.Hr(),
    dcc.RadioItems(id='colors',
                   options = [{'label': i,'value':i} for i in df['color'].unique()],
                   value='red',
                   inline=True,
                  ),
    html.Div(id='colors-output'),
    html.Img(id='display-image', src = 'children', height=300)
  ])

  # callbacks for wheels
@app.callback(Output(component_id='colors-output', component_property='children' ),
              [Input('colors','value')])
def call_back_wheel(wheel_value):
  return f'You selected {wheel_value}'

# callback for colors
@app.callback(Output('wheels-output', 'children' ),
              [Input('wheels','value')])
def call_back_color(color_value):
  return f'You selected {color_value}'

# call backs for image
@app.callback(Output('display-image','src'),
              [Input('wheels','value'),
               Input('colors','value')])
def callback_image(wheel, color):
  path = 'data/Images/'
  return encode_image(path+df[(df['wheels']==wheel) &
  (df['color']==color)]['image'].values[0])

# Run server
if __name__ == '__main__':
  app.run_server(host='0.0.0.0', debug=True)