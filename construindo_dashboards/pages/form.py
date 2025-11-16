from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import joblib
import numpy as np
import pandas as pd
from app import app

model = joblib.load('xgb_model.pkl')
medians = joblib.load('medians.pkl')

form = dbc.Container([
    html.H1('Heart Disease Prediction', className='text-center mt-5'),
    html.P('Please fill in the following information to predict if you have heart disease:', className='text-center mb-5'),
        dbc.Row([
            dbc.Col([
                dbc.CardGroup([
                    dbc.Label('age'),
                    dbc.Input(id='age', type='number', placeholder='Enter your age')
                ], className='mb-3'),

                dbc.CardGroup([
                    dbc.Label('Biological sex'),
                    dbc.Select(
                        id='sex',
                        options=[
                            {'label': 'Male', 'value': 1},
                            {'label': 'Female', 'value': 0}
                        ]
                    )
                ], className='mb-3'),

                # tipo de dor no peito
                dbc.CardGroup([
                    dbc.Label('chest pain type'),
                    dbc.Select(
                        id='cp',
                        options=[
                            {'label': 'Typical angina', 'value': 0},
                            {'label': 'Atypical angina', 'value': 1},
                            {'label': 'Non-anginal pain', 'value': 2},
                            {'label': 'Asymptomatic', 'value': 3}
                        ]
                    )
                ], className='mb-3'),

                # trestbps
                dbc.CardGroup([
                    dbc.Label('resting blood pressure'),
                    dbc.Input(id='trestbps', type='number',
                              placeholder='Enter your resting blood pressure')
                ], className='mb-3'),

                # chol
                dbc.CardGroup([
                    dbc.Label('serum cholestoral in mg/dl'),
                    dbc.Input(id='chol', type='number',
                              placeholder='Enter your serum cholestoral in mg/dl')
                ], className='mb-3'),

                # fbs
                dbc.CardGroup([
                    dbc.Label('fasting blood sugar > 120 mg/dl'),
                    dbc.Select(
                        id='fbs',
                        options=[
                            {'label': 'True', 'value': 1},
                            {'label': 'False', 'value': 0}
                        ]
                    )
                ], className='mb-3'),

                # restecg
                dbc.CardGroup([
                    dbc.Label('resting electrocardiographic results'),
                    dbc.Select(
                        id='restecg',
                        options=[
                            {'label': 'Normal', 'value': 0},
                            {'label': 'Having ST-T wave abnormality', 'value': 1},
                            {'label': 'Showing probable or definite left ventricular hypertrophy', 'value': 2}
                        ]
                    )
                ], className='mb-3'),
            ]),

            dbc.Col([
                # thalach
                dbc.CardGroup([
                    dbc.Label('maximum heart rate achieved'),
                    dbc.Input(id='thalach', type='number',
                              placeholder='Enter your maximum heart rate achieved')
                ], className='mb-3'),

                # exang
                dbc.CardGroup([
                    dbc.Label('exercise induced angina'),
                    dbc.Select(
                        id='exang',
                        options=[
                            {'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0}
                        ]
                    )
                ], className='mb-3'),

                # oldpeak
                dbc.CardGroup([
                    dbc.Label('oldpeak'),
                    dbc.Input(id='oldpeak', type='number',
                              placeholder='Enter your oldpeak value')
                ], className='mb-3'),

                # slope
                dbc.CardGroup([
                    dbc.Label('slope'),
                    dbc.Select(
                        id='slope',
                        options=[
                            {'label': 'Upsloping', 'value': 0},
                            {'label': 'Flat', 'value': 1},
                            {'label': 'Downsloping', 'value': 2}
                        ]
                    )
                ], className='mb-3'),

                # ca
                dbc.CardGroup([
                    dbc.Label('number of major vessels (0-3) colored by fluoroscopy'),
                    dbc.Select(
                        id='ca',
                        options=[
                            {'label': '0', 'value': 0},
                            {'label': '1', 'value': 1},
                            {'label': '2', 'value': 2},
                            {'label': '3', 'value': 3}
                        ]
                    )
                ], className='mb-3'),

                # thal, myocardial scintigraphy
                dbc.CardGroup([
                    dbc.Label('thal'),
                    dbc.Select(
                        id='thal',
                        options=[
                            {'label': 'Normal', 'value': '3'},
                            {'label': 'Fixed defect', 'value': '6'},
                            {'label': 'Reversible defect', 'value': '7'}
                        ]
                    )
                ], className='mb-3'),

                # botao de previsao
                dbc.CardGroup([
                    dbc.Button('Predict', id='submit-button', n_clicks=0, color='success'),
                ]),
            ])
        ])
    ], fluid=True)

layout = html.Div([
    form,
    html.Div(id='prediction')
])


@app.callback(
    Output('prediction', 'children'),
    Input('submit-button', 'n_clicks'),
    State('age', 'value'),
    State('sex', 'value'),
    State('cp', 'value'),
    State('trestbps', 'value'),
    State('chol', 'value'),
    State('fbs', 'value'),
    State('restecg', 'value'),
    State('thalach', 'value'),
    State('exang', 'value'),
    State('oldpeak', 'value'),
    State('slope', 'value'),
    State('ca', 'value'),
    State('thal', 'value')

)

def predict_heart_disease(n_clicks, age, sex, cp, trestbps, chol, fbs, restecg,
                          thalach, exang, oldpeak, slope, ca, thal):
    if n_clicks == 0:
        return ''
    
    user = pd.DataFrame(
        data = [[age, sex, cp, trestbps, chol, fbs, restecg,
                 thalach, exang, oldpeak, slope, ca, thal]],
        columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
                   'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

    )

    # fill missing values with medians
    user = user.fillna(medians)

    # oldpeak is float
    user['oldpeak'] = user['oldpeak'].astype(float)

    # convert numbers from strings to integers
    for col in user.columns:
        if col != 'oldpeak':
            user[col] = pd.to_numeric(user[col])


    prediction = model.predict(user)[0]
    if prediction == 1:
        message = 'The model predicts that you have heart disease.'
        alert_color = 'danger'
    else:
        message = 'The model predicts that you do not have heart disease.'
        alert_color = 'light'
    
     
    alert = dbc.Alert(
        message,
        color=alert_color,
        className='d-flex justify-content-center mb-5'
    )
    return alert