from ucimlrepo import fetch_ucirepo
import plotly.express as px
from dash import Dash, dcc, html

heart_disease = fetch_ucirepo(id=45)
data = heart_disease.data.features
#print(data.head())

hist_fig = px.histogram(data, x='age', title='Histograma de Idades')
hist_div = html.Div([
        html.H2('Histograma de Idades'),
        dcc.Graph(figure=hist_fig)
        ])

data['disease'] = (heart_disease.data.targets > 0) * 1
boxplot_fig = px.box(data, x='disease', y='age', color='disease', title='Boxplot de idades')
boxplot_div = html.Div([
        html.H2('Boxplot de Idades'),
        dcc.Graph(figure=boxplot_fig)
        ]) 

app = Dash(__name__)
app.layout = html.Div([  
    html.H1('Análise de dados do UCI Repository Heart Disease'),
    hist_div,
    boxplot_div
])

# app.layout.children.append(boxplot_div) ## add dynamically

app.run_server(debug=True)