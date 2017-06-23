# -*- coding: utf-8 -*-     
import os
import json
import struct
import random
import numpy as np     
import matplotlib.pyplot as plt    

class DateUtil(object):
    """docstring for DateUtil"""
    def __init__(self):
        super(DateUtil, self).__init__()
        self.trainDict = {}
        self.testDict = {}
        self.disk = os.path.join(os.getcwd(), "data")

    def parseData(self, datafname, dataLabels):
        #Read train data and package them with JSON
        self.trainFilename = datafname
        self.trainBinfile = open(self.trainFilename , 'rb')
        self.trainBuf = self.trainBinfile.read()
        self.trainIndex = 0
        self.magic, self.numImages , self.numRows , self.numColumns\
            = struct.unpack_from('>IIII' , self.trainBuf , self.trainIndex) 
        self.trainIndex += struct.calcsize('>IIII') 
        
        self.labelFilename = dataLabels
        self.labelBinFile = open(self.labelFilename , 'rb')
        self.labelBuf = self.labelBinFile.read()
        self.labelIndex = 0
        magic1, numLabels1 \
            = struct.unpack_from('>II' , self.labelBuf , self.labelIndex)    
        self.labelIndex += struct.calcsize('>II') 
        

        dataDict = {}
        imgId = 0 
        
        for i in range(0 , int(self.numImages)):
            dataDict[imgId] = {}
            
            im = struct.unpack_from('>784B' , self.trainBuf, self.trainIndex)
            label = struct.unpack_from('1B' ,self.labelBuf, self.labelIndex)[0]
            
            self.trainIndex += struct.calcsize('>784B') 
            self.labelIndex += struct.calcsize('1B')

            dataDict[imgId]["data"] = im
            dataDict[imgId]["label"] = label
            imgId += 1

        return dataDict

    def getTrainData(self):
        dataPath = os.path.join(self.disk, "train-images.idx3-ubyte")
        labelPath = os.path.join(self.disk, "train-labels.idx1-ubyte")
        self.trainDict =  self.parseData(dataPath, labelPath)
        return self.trainDict

    def plotImage(self, imgId, imgType):
        dataDict = {}
        self.getTrainData()
        self.getTestData()
        dataDict = self.trainDict if imgType == "train" else self.testDict

        try:
            im = np.array(dataDict[imgId]["data"])  
            im = im.reshape(28,28)
            print dataDict[imgId]["label"]
            plt.imshow(im)
            plt.show()
        except KeyError:
            print "[KeyError] Check the id of image."

    def getTestData(self):
        dataPath = os.path.join(self.disk, 't10k-images.idx3-ubyte')
        labelPath = os.path.join(self.disk, 't10k-labels.idx1-ubyte')
        self.testDict = self.parseData(dataPath, labelPath)
        return self.testDict


    def getTrainMatrix(self, num):
        self.getTrainData()
        trainMatrix = []
        trainLabels = []
        ids = random.sample(range(0, 60000), num)
        for Id in ids:
            trainMatrix.append(self.trainDict[Id]['data'])
            trainLabels.append(self.trainDict[Id]['label'])
        self.trainDict['dataMartix'] = np.array(trainMatrix)
        self.trainDict['labelList'] = np.array(trainLabels)
        return self.trainDict
    
    def getTestMatrix(self, num):
        self.getTestData()
        testMatrix = []
        testLabels = []
        ids = random.sample(range(0, 100434), num)
        for Id in ids:
            testMatrix.append(self.testDict[Id]['data'])
            testLabels.append(self.testDict[Id]['label'])
        self.testDict['dataMartix'] = np.array(testMatrix)
        self.testDict['labelList'] = np.array(testLabels)
        return self.testDict

class descriptData(object):
    """docstring for descriptData"""
    def __init__(self):
        super(descriptData, self).__init__()
        self.descript = {}

    def getData(self):
        dataDisk = os.path.join(os.getcwd(), "data")
        fPath = os.path.join(dataDisk, 'data.txt')
        f = open(fPath)
        for item in f.readlines():
            item = item.replace('\n', '')
            item = item.split(',')
            self.descript[int(item[0])] = {}
            self.descript[int(item[0])]['name'] = item[2]
            self.descript[int(item[0])]['des'] = item[1]
        return self.descript



        