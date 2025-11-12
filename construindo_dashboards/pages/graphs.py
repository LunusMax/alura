from ucimlrepo import fetch_ucirepo
import plotly.express as px
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

heart_disease = fetch_ucirepo(id=45)
data = heart_disease.data.features

hist_fig = px.histogram(data, x='age', title='Ages Histogram')
hist_div = html.Div([
        dcc.Graph(figure=hist_fig)
        ])

data['disease'] = (heart_disease.data.targets > 0) * 1
boxplot_fig = px.box(data, x='disease', y='age', color='disease', title='Ages Boxplot')
boxplot_div = html.Div([
        dcc.Graph(figure=boxplot_fig)
        ]) 

layout = html.Div([  
    html.H1('Data Analysis of UCI Repository Heart Disease', className='text-center mb-5'),
    dbc.Container([
        dbc.Row([
            dbc.Col([hist_div], md=7),
            dbc.Col([boxplot_div], md=5)
        ])
    ])

])