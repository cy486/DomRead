#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

train = pd.read_csv('E:/Preliminary-finals.csv')
test = pd.read_csv('E:/Preliminary-finals.csv')
y = (train["label"] - 1).astype(int)

column = "review"
test_id = test["ID"].copy()

text_clf = Pipeline([('tfidf', TfidfVectorizer(ngram_range=(1, 2), min_df=3,
                                               max_df=0.9, use_idf=1, smooth_idf=1,
                                               sublinear_tf=1)),

                     ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                           alpha=1e-3, random_state=42,
                                           max_iter=5, tol=None))])

text_clf = text_clf.fit(train[column], y)
preds = text_clf.predict(test[column])

base = open('try.csv', 'w')

i = 0
base.write("id,label" + "\n")
for item in preds:
    base.write(str(i) + "," + str(item + 1) + "\n")
    i = i + 1
base.close()