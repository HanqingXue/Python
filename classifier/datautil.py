# -*- coding: utf-8 -*-     
import struct    
import matplotlib.pyplot as plt    
import operator  
import numpy as np  
import json
from matplotlib import pyplot as plt
import os
  
class DateUtil(object):
    """docstring for DateUtil"""
    def __init__(self):
        super(DateUtil, self).__init__()
        self.trainDict = {}
        self.testDict = {}
        self.disk = os.getcwd()
        print os.path.join("data")
        #print self.disk.join('data')

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
        self.trainDict =  self.parseData("train-images.idx3-ubyte", "train-labels.idx1-ubyte")
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
        self.testDict = self.parseData('t10k-images.idx3-ubyte', 't10k-labels.idx1-ubyte')
        return self.testDict

if __name__ == "__main__":
    util = DateUtil()
    
