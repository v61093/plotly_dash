# Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

# app
app = dash.Dash()

# creating random data points
np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

# Layout
app.layout = html.Div([
  'This is the Outer Most Div Block',
  dcc.Graph(id='scatterplot',
            figure={
              'data': [
                go.Scatter(x=random_x,
                           y=random_y,
                           mode='markers',
                           marker={
                             'size': 12,
                             'color': 'rgb(200,51,34)',
                             'symbol': 'pentagon'
                           })
              ],
              'layout':
              go.Layout(title='My Scatter Plot',
                        xaxis=dict(title='some x title'))
            }),
  html.Div(
    [
      'This is the first inner div block ',
      dcc.Graph(
        id='scatterplot',
        figure={
          'data': [
            go.Scatter(
              x=random_x,
              y=random_y,
              mode='markers',
              marker={
                # 'size': 12,
                'color': 'rgb(78,151,34)',
                'symbol': 'pentagon'
              })
          ],
          'layout':
          go.Layout(title='My inner Scatter Plot',
                    xaxis=dict(title='some x title'))
        })
    ],
    style={
      'color': 'blue',
      'border': '2px blue solid'
    }),
  dcc.Graph(id='scatterplot_3',
            figure={
              'data': [
                go.Scatter(x=random_x,
                           y=random_y,
                           mode='markers',
                           marker={
                             'size': 12,
                             'color': 'rgb(78,151,34)',
                             'symbol': 'pentagon'
                           })
              ],
              'layout':
              go.Layout(title='My Second Scatter Plot',
                        xaxis=dict(title='some x title'))
            })
])

# Run server
if __name__ == '__main__':
  app.run_server(host='0.0.0.0', debug=True)
