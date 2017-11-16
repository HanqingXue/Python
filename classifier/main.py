# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from datautil import *
from algutil import * 
import os
import sys
import time
import threading

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_main(object):
    def setupUi(self, main):
        self.assetsDisk = os.path.join(os.getcwd(), "assets")
        self.resultDisk = os.path.join(os.getcwd(), "result")
        self.testimg = os.path.join(self.assetsDisk, 'testbg.png')
        self.trainimg = os.path.join(self.assetsDisk, 'trainbg.png')
        self.primg = os.path.join(self.assetsDisk, 'prbg.png')
        self.sampleimg = os.path.join(self.assetsDisk, 'samplebg.png')
        self.titleimg = os.path.join(self.assetsDisk, 'title.png')
        self.resPr = os.path.join(self.resultDisk, 'PR.png')
        self.resTrain = os.path.join(self.resultDisk, 'train.png')
        self.resTest = os.path.join(self.resultDisk, 'test.png')
        self.resSample = os.path.join(self.resultDisk, 'Samples.png')
        main.setObjectName(_fromUtf8("main"))
        main.resize(1200, 690)
        self.centralwidget = QtGui.QWidget(main)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8(self.titleimg)))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 3, -1, -1)
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)
        self.spinBox_2 = QtGui.QSpinBox(self.tab)
        self.spinBox_2.setRange(0, 60000)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.spinBox_2.setValue(10000)
        self.spinBox_2.setSingleStep(10000)
        self.gridLayout_3.addWidget(self.spinBox_2, 3, 1, 1, 1)
        self.label_17 = QtGui.QLabel(self.tab)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_3.addWidget(self.label_17, 4, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_3.addWidget(self.label_9, 3, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.tab)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.comboBox, 0, 1, 1, 1)
        self.textBrowser = QtGui.QTextBrowser(self.tab)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout_3.addWidget(self.textBrowser, 2, 1, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.tab)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox.setRange(0, 10000)
        self.spinBox.setValue(1000)
        self.spinBox.setSingleStep(1000)
        self.gridLayout_3.addWidget(self.spinBox, 4, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 2)
        self.gridLayout_3.setColumnStretch(1, 8)
        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(2, 1)
        self.gridLayout_3.setRowStretch(3, 1)
        self.gridLayout_3.setRowStretch(4, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.progressBar = QtGui.QProgressBar(self.tab)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 5, 1, 1)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setPixmap(QtGui.QPixmap(_fromUtf8(self.testimg)))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(self.primg)))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.tabWidget_2 = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_11 = QtGui.QLabel(self.tab_3)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_4.addWidget(self.label_11, 3, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.tab_3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_4.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.tab_3)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_4.addWidget(self.label_12, 4, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.tab_3)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_4.addWidget(self.label_14, 3, 1, 1, 1)
        self.label = QtGui.QLabel(self.tab_3)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 5, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.tab_3)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_4.addWidget(self.label_15, 4, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.tab_3)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_4.addWidget(self.label_16, 2, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.tab_3)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_4.addWidget(self.label_13, 5, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_4)
        self.tabWidget_2.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget_2, 1, 5, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8(self.trainimg)))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8(self.sampleimg)))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        main.setCentralWidget(self.centralwidget)

        self.retranslateUi(main)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main)
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.reset)

        self.comboBox.currentIndexChanged[str].connect(self.changeComobox)
        des = descriptData()
        self.des = des.getData()
        self.textBrowser.setHtml(_translate("main", self.des[0]['des'], None))

    def changeComobox(self):
        index =  self.comboBox.currentIndex()
        if index == 0:
            index = 0
        else:
            index += 1
        self.textBrowser.setHtml(_translate("main", self.des[index]['des'], None))

    def reset(self):
        self.pushButton.setText(_translate("main", "运行", None))
        self.label_10.setPixmap(QtGui.QPixmap(_fromUtf8(self.testimg)))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(self.primg)))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8(self.trainimg)))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8(self.sampleimg)))
        self.label_16.setText(_translate("main", str(0) + "S", None))
        self.label_14.setText(_translate("main", str(0) + "%", None))
        self.label_15.setText(_translate("main", str(0) + "%", None))
        self.label_13.setText(_translate("main", str(0) + "%", None))
        self.progr14essBar.setProperty("value", 0)

    def run(self):
        self.pushButton.setText(_translate("main", "运行中", None))
        start = time.time()
        dutil = DateUtil()
        trainSize = []
        trainData = dutil.getTrainMatrix(self.spinBox_2.value())
        testData = dutil.getTrainMatrix(self.spinBox.value())
        self.progressBar.setProperty("value", 25)
        plotDataSize(trainData, 'train')
        plotDataSize(testData, 'test')
        plotSamples(testData)
        
        self.progressBar.setProperty("value", 50)
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8(self.resTrain)))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8(self.resSample)))
        self.label_10.setPixmap(QtGui.QPixmap(_fromUtf8(self.resTest)))

        self.progressBar.setProperty("value", 75)
        index = self.comboBox.currentIndex()
        if index == 0:
            index = 0
        else:
            index = index + 1

        if index == 7:
            algorithmName = 'RandomForest'
        else:
            algorithmName = self.des[index]['name']
        runThread = threading.Thread(target=self.algorithm(algorithmName, trainData, testData))
        runThread.setDaemon(True)
        runThread.start()

    def algorithm(self, algorithm, trainData, testData):
        start = time.time()
        alg = algutil()
        ans = alg.classify(algorithm, trainData, testData)
        plotPR(ans)
        end = time.time()
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(self.resPr)))
        self.progressBar.setProperty("value", 100)
        self.label_16.setText(_translate("main", str(round(end - start, 2)) + "S", None))
        self.label_14.setText(_translate("main", str(round(ans['avg']['precision'], 2)) + "%", None))
        self.label_15.setText(_translate("main", str(round(ans['avg']['recall'], 2)) + "%", None))
        self.label_13.setText(_translate("main", str(round(ans['avg']['fscore'], 2)) + "%", None))

    def retranslateUi(self, main):
        main.setWindowTitle(_translate("main", "MainWindow", None))
        self.label_7.setText(_translate("main", "算法简介", None))
        self.label_17.setText(_translate("main", "测试样本数", None))
        self.label_9.setText(_translate("main", "训练样本数", None))
        self.comboBox.setItemText(0, _translate("main", "决策树算法", None))
        self.comboBox.setItemText(1, _translate("main", "支持向量机", None))
        self.comboBox.setItemText(2, _translate("main", "AdaBoost", None))
        self.comboBox.setItemText(3, _translate("main", "KNN分类", None))
        self.comboBox.setItemText(4, _translate("main", "朴素贝叶斯", None))
        self.comboBox.setItemText(5, _translate("main", "随机梯度下降法", None))
        self.comboBox.setItemText(6, _translate("main", "随机森林", None))
        self.textBrowser.setHtml(_translate("main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\">决策树算法是一种逼近离散函数值的方法。它是一种典型的</span><a href=\"http://baike.baidu.com/item/%E5%88%86%E7%B1%BB%E6%96%B9%E6%B3%95\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; text-decoration: underline; color:#136ec2; background-color:#ffffff;\">分类方法</span></a><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\">，首先对数据进行处理，利用归纳算法生成可读的规则和决策树，然后使用决策对新数据进行分析。本质上决策树是通过一系列规则对数据进行分类的过程。</span></p></body></html>", None))
        self.label_2.setText(_translate("main", "算法", None))
        self.pushButton.setText(_translate("main", "运行", None))
        self.pushButton_2.setText(_translate("main", "初始化", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("main", "选项", None))
        self.label_11.setText(_translate("main", "总体精度", None))
        self.label_8.setText(_translate("main", "运行时间", None))
        self.label_12.setText(_translate("main", "总体召回率", None))
        self.label_14.setText(_translate("main", "0%", None))
        self.label.setText(_translate("main", "总体F1-Socore", None))
        self.label_15.setText(_translate("main", "0%", None))
        self.label_16.setText(_translate("main", "0S", None))
        self.label_13.setText(_translate("main", "0%", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("main", "试验结果", None))

def main():
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_main()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
