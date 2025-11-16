from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

app = Dash(__name__, 
           external_stylesheets=['assets/main.css', dbc.themes.FLATLY],
           suppress_callback_exceptions=True)