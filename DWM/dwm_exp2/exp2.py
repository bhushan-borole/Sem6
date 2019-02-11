import pandas as pd 
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing
from sklearn import metrics


le = preprocessing.LabelEncoder()
df = pd.read_csv('data.csv')

color_encoded = le.fit_transform(df[['Color']])
type_encoded = le.fit_transform(df[['type']])
origin_encoded = le.fit_transform(df[['origin']])
label = le.fit_transform(df[['Stolen']])

features = zip(color_encoded, type_encoded, origin_encoded)
features = np.array([x for x in features])

model = GaussianNB()
model.fit(features, label)

y_pred = [[0, 0, 0]]

predict = model.predict(y_pred)
print("Predicted: ", predict)

