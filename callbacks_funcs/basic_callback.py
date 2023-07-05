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
