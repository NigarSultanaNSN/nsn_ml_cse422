# -*- coding: utf-8 -*-
"""18101143_NigarSulatanaNuha_Assign05.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uhoEjD-4NytZYwFWgc2JmhvpxvVvQf3Q
"""

pip install mglearn

import numpy as np
import pandas as pd

#dataset reading
given_dataset = pd.read_csv('/content/breast cancer classification dataset.csv')

#handling missing values
 given_dataset = given_dataset.dropna(how = 'any', axis = 0)

#encoded categorical features
import sklearn
from sklearn.preprocessing import LabelEncoder
enc = LabelEncoder()
given_dataset['diagnosis'] = enc.fit_transform(given_dataset['diagnosis'])
print(given_dataset[['diagnosis']].head())

#scaling from 0 to 1 using proper scaling technique, min max scaler
import mglearn
mglearn.plots.plot_scaling()

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

cancer= load_breast_cancer()
X_train, X_test, Y_train, Y_test= train_test_split(cancer.data, cancer.target, random_state= 1)

from sklearn.preprocessing import MinMaxScaler
Scaler= MinMaxScaler()
Scaler.fit(X_train)
X_train_scaled= Scaler.transform(X_train)
X_train_scaled= Scaler.transform(X_test)

#Accuracy calculatiobn using logistic regression
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

model = LogisticRegression(max_iter=6000)
model.fit(X_train, Y_train)
my_prediction1 = model.predict(X_test)
accuracy_test1 = accuracy_score(Y_test, my_prediction1)
print(accuracy_test1)

#Accuracy calculatiobn using decision tree
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(criterion='entropy',random_state=1)
clf.fit(X_train,Y_train)
my_prediction2 = clf.predict(X_test)
accuracy_test2 = accuracy_score(my_prediction2,Y_test)
print(accuracy_test2)

#Comparison using the bar chart
plt.bar(['Logistic Regression', 'Decision Tree'],[accuracy_test1, accuracy_test2])
plt.title('Comparing Accuracy')
plt.show()