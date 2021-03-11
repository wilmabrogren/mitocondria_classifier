from mitosamples import URLS
import numpy as np
import tensorflow as tf
from tensorflow import keras
import mitosamples


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

mitoData = pd.read_csv('mpntext.csv')
X = mitoData.drop(columns=['location'])
y = mitoData['location']

model = DecisionTreeClassifier()
model.fit(X, y)

tree.export_graphviz(model, out_file='mpntextkorr2.dot',
                    feature_names=['x', 'y'],
                    class_names=sorted(y.unique()), 
                     label='all',
                     rounded=True, 
                    filled=True)

#def link_code():

for i in URLS:
    #link=(baseURLURLS[]+ baseURLend)
 print(baseURL+i+baseURLend)
 urllib.request.urlopen(i)
