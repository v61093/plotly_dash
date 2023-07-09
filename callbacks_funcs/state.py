# Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output,State
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
@app.callback(Output('output-out','children'),
            [Input('submit-val','n_clicks')],
            [State('input-in','value')])
def update_output(nclicks,number):
    return f'You have entered {number} and clicked submit button {nclicks} times'
  

# Run server
if __name__ == '__main__':
  app.run_server(host='0.0.0.0', debug=True)