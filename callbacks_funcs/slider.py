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
    dcc.RangeSlider(min=-5, max=6, step=1, value=[-2,1], id='my-range-slider'),
    html.Div(id='output'),
  ])


# call backs for image
@app.callback(Output('output','children'),
            [Input('my-range-slider','value')])
def update_output(value):
    return value[0]*value[1]

# Run server
if __name__ == '__main__':
  app.run_server(host='0.0.0.0', debug=True)
