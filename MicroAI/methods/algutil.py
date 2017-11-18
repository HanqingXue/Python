#coding=utf-8

import time
import random
import numpy as np
from sklearn import svm
from scipy import interp
import matplotlib as mpl 
from sklearn import tree
from sklearn.svm import SVC
from datautil import DateUtil
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import StratifiedKFold
from sklearn.metrics import f1_score, classification_report
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier

class algutil(object):
    """docstring for algutil"""
    def __init__(self):
        super(algutil, self).__init__()
        self.algorithm = {
            "DT": tree.DecisionTreeClassifier(),
            "SVM": SVC(kernel="linear", C=0.025),
            "AdaBoost": AdaBoostClassifier(), 
            "KNN": KNeighborsClassifier(n_neighbors=600),
            "NBM": GaussianNB(),
            "SGD": SGDClassifier(loss="hinge", penalty="l2"), 
            "RF": RandomForestClassifier()
        }
    
    def classify(self, classifierName, trainData, testData):
        classifier = self.algorithm[classifierName] 
        classifier.fit(trainData["dataMartix"], trainData["labelList"])
        predictions = classifier.predict(testData["dataMartix"])
        
        report = classification_report(testData["labelList"], predictions)
        stopWords = ['precision', 'recall', 'f1-score', 'support', 'total', '/']
        report = report.split()
        report = list(report)
        for word in stopWords:
            report.remove(word)
        
        resultDict = {}
        for index in range(0, len(report), 5):
            cls        = report[index]
            precision  = float (report[index + 1])
            recall     = float (report[index + 2])
            fscore     = float (report[index + 3])
            support    = int (report[index + 4])

            resultDict[cls] = {}
            resultDict[cls]['precision'] = precision
            resultDict[cls]['recall'] = recall
            resultDict[cls]['fscore'] = fscore
            resultDict[cls]['support'] = support

        return resultDict