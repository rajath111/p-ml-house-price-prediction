import numpy as np
import pandas as pd
import pickle

df = pd.read_csv('data/housing.csv',sep=',')

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X = df.iloc[:, 0:3]
y = df.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y)
pd.concat([X_test, y_test], axis=1).to_csv('data/test_data.csv', index=None)
model = LinearRegression()
model.fit(X_train, y_train)
with open('model/modelfile', 'wb') as f:
    pickle.dump(model, f)