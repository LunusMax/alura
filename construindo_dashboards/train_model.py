from ucimlrepo import fetch_ucirepo

heart_disease = fetch_ucirepo(id=45)
data = heart_disease.data.features
data['disease'] = (heart_disease.data.targets > 0) * 1

X = data.drop(columns='disease')
y = data['disease']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=432, stratify=y)

import xgboost as xgb
model = xgb.XGBClassifier(objective='binary:logistic')
model.fit(X_train, y_train)
preds = model.predict(X_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(y_test, preds)

print(f'A acurácia do modelo é {acc:.2%}')

import joblib
joblib.dump(model, 'xgb_model.pkl')