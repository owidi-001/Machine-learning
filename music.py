#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 23:08:45 2021

@author: whoami
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier  #sklearn library
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score #check predictions accuracy
from joblib import dump,load
from sklearn import tree #for graphical exports
# import data
music_data=pd.read_csv('music.csv')

# print(music_data)

# data cleaning

# split data set
X=music_data.drop(columns=['genre'])
y=music_data['genre']

X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.2) #using 20% for testing and 80% for training
# print(x)
# print(y)

# creating a model
model=DecisionTreeClassifier()
model.fit(X_train,y_train)

predictions=model.predict(X_test)

# measuring the accuracy of a model

score=accuracy_score(y_test,predictions)
# print(score)

# print(predictions)

# model persisters ie keep a record of trained data
# dump(model,'music-recommender.joblib')

# load the joblib file by
model=load('music-recommender.joblib')

# export to graph
tree.export_graphviz(model,out_file='music-recomender.dot',feature_names=['age','gender'],class_names=sorted(y.unique()),label='all',rounded=True,filled=True)