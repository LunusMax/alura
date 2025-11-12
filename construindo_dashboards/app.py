from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pages

app = Dash(__name__, external_stylesheets=['assets/main.css', dbc.themes.FLATLY])

navigation = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Graphics", href="/graphs")),
        dbc.NavItem(dbc.NavLink("Form", href="/form")),
    ],
    brand="Dashboard",
    brand_href="#",
    color="primary",
    dark=True,
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navigation, 
    html.Div(id='page-content')
])


@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)

def render_page(pathname):
    if pathname == '/graphs':
        return pages.graphs.layout
    elif pathname == '/form':
        from app_form import app as form_app
        return form_app.layout
    else:
        return html.P('Home')


app.run_server(debug=True)