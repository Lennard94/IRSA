# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(3119, 1663)
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.widget.setObjectName("widget")
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setGeometry(QtCore.QRect(-10, -40, 2691, 1671))
        self.scrollArea.setMaximumSize(QtCore.QSize(2691, 16777215))
        self.scrollArea.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 2689, 1641))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(2689, 0))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 40, 5000, 5000))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea_2.setMaximumSize(QtCore.QSize(5000, 5000))
        self.scrollArea_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scrollArea_2.setAutoFillBackground(False)
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 999999, 999999))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_3.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_3.setMinimumSize(QtCore.QSize(999999, 999999))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.Load_EXP = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.Load_EXP.setGeometry(QtCore.QRect(270, 150, 201, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Load_EXP.setFont(font)
        self.Load_EXP.setStyleSheet("Background: rgb(0, 85, 255)")
        self.Load_EXP.setObjectName("Load_EXP")
        self.lb = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_3)
        self.lb.setGeometry(QtCore.QRect(20, 250, 111, 44))
        self.lb.setMaximum(4000)
        self.lb.setSingleStep(1)
        self.lb.setProperty("value", 1000)
        self.lb.setObjectName("lb")
        self.hb = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_3)
        self.hb.setGeometry(QtCore.QRect(140, 250, 111, 44))
        self.hb.setMaximum(4000)
        self.hb.setProperty("value", 1600)
        self.hb.setObjectName("hb")
        self.normalize_1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.normalize_1.setGeometry(QtCore.QRect(20, 310, 231, 43))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.normalize_1.setFont(font)
        self.normalize_1.setStyleSheet("Background: rgb(0, 85, 255)")
        self.normalize_1.setObjectName("normalize_1")
        self.exp_ir_graph = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.exp_ir_graph.setGeometry(QtCore.QRect(270, 210, 611, 301))
        font = QtGui.QFont()
        font.setItalic(False)
        self.exp_ir_graph.setFont(font)
        self.exp_ir_graph.setStyleSheet("background: rgb(255, 255, 255)")
        self.exp_ir_graph.setObjectName("exp_ir_graph")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_3)
        self.textBrowser.setGeometry(QtCore.QRect(0, 100, 1521, 441))
        self.textBrowser.setStyleSheet("background: rgb(180,180,180)")
        self.textBrowser.setObjectName("textBrowser")
        self.Load_EXP_VCD = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.Load_EXP_VCD.setGeometry(QtCore.QRect(890, 150, 201, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Load_EXP_VCD.setFont(font)
        self.Load_EXP_VCD.setStyleSheet("Background: rgb(0, 85, 255)")
        self.Load_EXP_VCD.setObjectName("Load_EXP_VCD")
        self.automatic = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.automatic.setGeometry(QtCore.QRect(20, 410, 231, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.automatic.setFont(font)
        self.automatic.setStyleSheet("Background: rgb(0, 85, 255)")
        self.automatic.setObjectName("automatic")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 210, 251, 151))
        self.textBrowser_3.setStyleSheet("background:\n"
"rgb(255, 150, 44)")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_3)
        self.textBrowser_4.setGeometry(QtCore.QRect(10, 370, 251, 141))
        self.textBrowser_4.setStyleSheet("background:\n"
"rgb(255, 150, 44)")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.delete_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.delete_2.setGeometry(QtCore.QRect(20, 460, 231, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.delete_2.setFont(font)
        self.delete_2.setStyleSheet("Background: rgb(0, 85, 255)")
        self.delete_2.setObjectName("delete_2")
        self.theo_ir_graph = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.theo_ir_graph.setGeometry(QtCore.QRect(270, 660, 611, 311))
        self.theo_ir_graph.setStyleSheet("background: rgb(255, 255, 255)")
        self.theo_ir_graph.setObjectName("theo_ir_graph")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_3)
        self.textBrowser_5.setGeometry(QtCore.QRect(0, 550, 1521, 471))
        self.textBrowser_5.setStyleSheet("background: rgb(180,180,180)")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_3)
        self.textBrowser_6.setGeometry(QtCore.QRect(10, 660, 251, 311))
        self.textBrowser_6.setStyleSheet("background:\n"
"rgb(255, 150, 44)")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.load_theo_exp = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.load_theo_exp.setGeometry(QtCore.QRect(460, 600, 191, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.load_theo_exp.setFont(font)
        self.load_theo_exp.setStyleSheet("Background: rgb(0, 85, 255)")
        self.load_theo_exp.setObjectName("load_theo_exp")
        self.w = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_3)
        self.w.setGeometry(QtCore.QRect(20, 700, 221, 44))
        self.w.setMaximum(4000)
        self.w.setProperty("value", 6)
        self.w.setObjectName("w")
        self.normalize_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.normalize_2.setGeometry(QtCore.QRect(20, 910, 231, 43))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.normalize_2.setFont(font)
        self.normalize_2.setStyleSheet("Background: rgb(0, 85, 255)")
        self.normalize_2.setObjectName("normalize_2")
        self.load_theo_vcd = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.load_theo_vcd.setGeometry(QtCore.QRect(890, 600, 201, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.load_theo_vcd.setFont(font)
        self.load_theo_vcd.setStyleSheet("Background: rgb(0, 85, 255)")
        self.load_theo_vcd.setObjectName("load_theo_vcd")
        self.exp_vcd_graph = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.exp_vcd_graph.setGeometry(QtCore.QRect(890, 210, 611, 301))
        self.exp_vcd_graph.setStyleSheet("background: rgb(255, 255, 255)")
        self.exp_vcd_graph.setObjectName("exp_vcd_graph")
        self.theo_vcd_graph = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.theo_vcd_graph.setGeometry(QtCore.QRect(890, 660, 611, 311))
        self.theo_vcd_graph.setStyleSheet("background: rgb(255, 255, 255)")
        self.theo_vcd_graph.setObjectName("theo_vcd_graph")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_3)
        self.textBrowser_7.setGeometry(QtCore.QRect(0, 1040, 1521, 421))
        self.textBrowser_7.setStyleSheet("background: rgb(180,180,180)")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_3)
        self.textBrowser_8.setGeometry(QtCore.QRect(0, 1110, 251, 321))
        self.textBrowser_8.setStyleSheet("background:\n"
"rgb(255, 150, 44)")
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.assignment_graph = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.assignment_graph.setGeometry(QtCore.QRect(260, 1110, 611, 321))
        self.assignment_graph.setStyleSheet("background: rgb(255, 255, 255)")
        self.assignment_graph.setObjectName("assignment_graph")
        self.shifted_graph = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.shifted_graph.setGeometry(QtCore.QRect(880, 1110, 611, 321))
        self.shifted_graph.setStyleSheet("background: rgb(255, 255, 255)")
        self.shifted_graph.setObjectName("shifted_graph")
        self.mu = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.mu.setGeometry(QtCore.QRect(40, 1170, 191, 31))
        self.mu.setDecimals(5)
        self.mu.setSingleStep(0.001)
        self.mu.setProperty("value", 0.98)
        self.mu.setObjectName("mu")
        self.sigma_1 = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.sigma_1.setGeometry(QtCore.QRect(40, 1207, 191, 31))
        self.sigma_1.setDecimals(5)
        self.sigma_1.setSingleStep(0.001)
        self.sigma_1.setProperty("value", 0.1)
        self.sigma_1.setObjectName("sigma_1")
        self.sigma_2 = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.sigma_2.setGeometry(QtCore.QRect(40, 1241, 191, 31))
        self.sigma_2.setDecimals(5)
        self.sigma_2.setSingleStep(1e-05)
        self.sigma_2.setProperty("value", 0.002)
        self.sigma_2.setObjectName("sigma_2")
        self.cutoff = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.cutoff.setGeometry(QtCore.QRect(40, 1275, 191, 30))
        self.cutoff.setMaximum(9999.0)
        self.cutoff.setProperty("value", 999.99)
        self.cutoff.setObjectName("cutoff")
        self.align = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.align.setGeometry(QtCore.QRect(10, 1380, 231, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.align.setFont(font)
        self.align.setStyleSheet("Background: rgb(0, 85, 255)")
        self.align.setObjectName("align")
        self.Load_EXP_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.Load_EXP_3.setGeometry(QtCore.QRect(480, 150, 201, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Load_EXP_3.setFont(font)
        self.Load_EXP_3.setStyleSheet("Background: rgb(0, 85, 255)")
        self.Load_EXP_3.setObjectName("Load_EXP_3")
        self.Load_EXP_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.Load_EXP_4.setGeometry(QtCore.QRect(1100, 150, 211, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Load_EXP_4.setFont(font)
        self.Load_EXP_4.setStyleSheet("Background: rgb(0, 85, 255)")
        self.Load_EXP_4.setObjectName("Load_EXP_4")
        self.Load_EXP_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.Load_EXP_6.setGeometry(QtCore.QRect(660, 600, 201, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Load_EXP_6.setFont(font)
        self.Load_EXP_6.setStyleSheet("Background: rgb(0, 85, 255)")
        self.Load_EXP_6.setObjectName("Load_EXP_6")
        self.Load_EXP_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.Load_EXP_7.setGeometry(QtCore.QRect(260, 1060, 211, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Load_EXP_7.setFont(font)
        self.Load_EXP_7.setStyleSheet("Background: rgb(0, 85, 255)")
        self.Load_EXP_7.setObjectName("Load_EXP_7")
        self.Load_EXP_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.Load_EXP_8.setGeometry(QtCore.QRect(880, 1060, 211, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Load_EXP_8.setFont(font)
        self.Load_EXP_8.setStyleSheet("Background: rgb(0, 85, 255)")
        self.Load_EXP_8.setObjectName("Load_EXP_8")
        self.load_theo_exp_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.load_theo_exp_2.setGeometry(QtCore.QRect(270, 600, 181, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.load_theo_exp_2.setFont(font)
        self.load_theo_exp_2.setStyleSheet("Background: rgb(0, 85, 255)")
        self.load_theo_exp_2.setObjectName("load_theo_exp_2")
        self.Load_EXP_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.Load_EXP_5.setGeometry(QtCore.QRect(1100, 600, 211, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Load_EXP_5.setFont(font)
        self.Load_EXP_5.setStyleSheet("Background: rgb(0, 85, 255)")
        self.Load_EXP_5.setObjectName("Load_EXP_5")
        self.temperature = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_3)
        self.temperature.setGeometry(QtCore.QRect(20, 800, 231, 44))
        self.temperature.setMaximum(4000)
        self.temperature.setProperty("value", 300)
        self.temperature.setObjectName("temperature")
        self.results = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_3)
        self.results.setGeometry(QtCore.QRect(1540, 1120, 256, 192))
        self.results.setObjectName("results")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_3)
        self.textBrowser_9.setGeometry(QtCore.QRect(1530, 1040, 471, 421))
        self.textBrowser_9.setStyleSheet("background: rgb(180,180,180)")
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser_9.raise_()
        self.textBrowser_7.raise_()
        self.assignment_graph.raise_()
        self.textBrowser_5.raise_()
        self.textBrowser.raise_()
        self.textBrowser_4.raise_()
        self.textBrowser_3.raise_()
        self.Load_EXP.raise_()
        self.lb.raise_()
        self.hb.raise_()
        self.normalize_1.raise_()
        self.exp_ir_graph.raise_()
        self.Load_EXP_VCD.raise_()
        self.automatic.raise_()
        self.delete_2.raise_()
        self.theo_ir_graph.raise_()
        self.textBrowser_6.raise_()
        self.load_theo_exp.raise_()
        self.w.raise_()
        self.normalize_2.raise_()
        self.load_theo_vcd.raise_()
        self.exp_vcd_graph.raise_()
        self.theo_vcd_graph.raise_()
        self.textBrowser_8.raise_()
        self.shifted_graph.raise_()
        self.mu.raise_()
        self.sigma_1.raise_()
        self.sigma_2.raise_()
        self.cutoff.raise_()
        self.align.raise_()
        self.Load_EXP_3.raise_()
        self.Load_EXP_4.raise_()
        self.Load_EXP_6.raise_()
        self.Load_EXP_7.raise_()
        self.Load_EXP_8.raise_()
        self.load_theo_exp_2.raise_()
        self.Load_EXP_5.raise_()
        self.temperature.raise_()
        self.results.raise_()
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 3119, 34))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSave = QtWidgets.QMenu(self.menuFile)
        self.menuSave.setObjectName("menuSave")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_Spectra = QtWidgets.QAction(MainWindow)
        self.actionSave_Spectra.setObjectName("actionSave_Spectra")
        self.actionSave_Alignment = QtWidgets.QAction(MainWindow)
        self.actionSave_Alignment.setObjectName("actionSave_Alignment")
        self.actionSave_Measures = QtWidgets.QAction(MainWindow)
        self.actionSave_Measures.setObjectName("actionSave_Measures")
        self.action_log_files = QtWidgets.QAction(MainWindow)
        self.action_log_files.setObjectName("action_log_files")
        self.menuSave.addSeparator()
        self.menuSave.addSeparator()
        self.menuSave.addAction(self.actionSave_Spectra)
        self.menuSave.addAction(self.actionSave_Alignment)
        self.menuSave.addAction(self.actionSave_Measures)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuSave.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Load_EXP.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">Load experimental IR spectrum</span></p></body></html>"))
        self.Load_EXP.setText(_translate("MainWindow", "LOAD IR"))
        self.lb.setToolTip(_translate("MainWindow", "<html><head/><body><p>Lower wavenumber to show/match</p></body></html>"))
        self.hb.setToolTip(_translate("MainWindow", "<html><head/><body><p>Higher wavenumber to show/match</p></body></html>"))
        self.normalize_1.setText(_translate("MainWindow", "Normalize"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Experimental IR and VCD Spectra</span></p></body></html>"))
        self.Load_EXP_VCD.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">Load experimental VCD spectrum</span></p></body></html>"))
        self.Load_EXP_VCD.setText(_translate("MainWindow", "LOAD VCD"))
        self.automatic.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">Automatically select peaks</span></p></body></html>"))
        self.automatic.setText(_translate("MainWindow", "Automatic"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Wave number range</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Peak Selection</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p></body></html>"))
        self.delete_2.setText(_translate("MainWindow", "Delete All"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Theoretical IR and VCD Spectra</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Lorentz Bandwidth</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Temperature</span></p></body></html>"))
        self.load_theo_exp.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">Load theoretical IR spectrum (in pickle format)</span></p></body></html>"))
        self.load_theo_exp.setText(_translate("MainWindow", "LOAD IR"))
        self.w.setToolTip(_translate("MainWindow", "<html><head/><body><p>Lorentzband width assumed for the broadening</p></body></html>"))
        self.normalize_2.setText(_translate("MainWindow", "Normalize"))
        self.load_theo_vcd.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">Load theoretical VCD spectrum</span></p></body></html>"))
        self.load_theo_vcd.setText(_translate("MainWindow", "LOAD VCD"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Alignment</span></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Scoring function</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\">µ</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">σ</span><span style=\" font-size:10pt; vertical-align:sub;\">1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">σ</span><span style=\" font-size:10pt; vertical-align:sub;\">2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">c</span></p></body></html>"))
        self.mu.setToolTip(_translate("MainWindow", "<html><head/><body><p>Parameter for the alignment: mean of the shifting</p></body></html>"))
        self.sigma_1.setToolTip(_translate("MainWindow", "<html><head/><body><p>Parameter for the alignment: sigma of the intensities</p></body></html>"))
        self.sigma_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Parameter for the alignment: sigma of the frequencies</p></body></html>"))
        self.cutoff.setToolTip(_translate("MainWindow", "<html><head/><body><p>Parameter for the alignment: cutoff. Set to high value to turn the cutoff off.</p></body></html>"))
        self.align.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">Align the theoretical spectra to the experimental data</span></p></body></html>"))
        self.align.setText(_translate("MainWindow", "Align"))
        self.Load_EXP_3.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">save experimental spectrum in png format</span></p></body></html>"))
        self.Load_EXP_3.setText(_translate("MainWindow", "Save .png"))
        self.Load_EXP_4.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">Save experimental VCD spectrum in png format</span></p></body></html>"))
        self.Load_EXP_4.setText(_translate("MainWindow", "Save .png"))
        self.Load_EXP_6.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">Save theoretical IR spectrum in png format</span></p></body></html>"))
        self.Load_EXP_6.setText(_translate("MainWindow", "Save .png"))
        self.Load_EXP_7.setText(_translate("MainWindow", "Save .png"))
        self.Load_EXP_8.setText(_translate("MainWindow", "Save .png"))
        self.load_theo_exp_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">Load energy distribution file (in pickle format)</span></p></body></html>"))
        self.load_theo_exp_2.setText(_translate("MainWindow", "LOAD E"))
        self.Load_EXP_5.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">Save theoretical VCD spectrum in png format</span></p></body></html>"))
        self.Load_EXP_5.setText(_translate("MainWindow", "Save .png"))
        self.temperature.setToolTip(_translate("MainWindow", "<html><head/><body><p>Temperature assumed for the boltzmann weighting</p></body></html>"))
        self.textBrowser_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Numerical Results of the Alignment</span></p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSave.setTitle(_translate("MainWindow", "Save ..."))
        self.actionOpen.setText(_translate("MainWindow", "Open ..."))
        self.actionSave_Spectra.setText(_translate("MainWindow", "Save spectra"))
        self.actionSave_Alignment.setText(_translate("MainWindow", "Save alignment"))
        self.actionSave_Measures.setText(_translate("MainWindow", "Save measures"))
        self.action_log_files.setText(_translate("MainWindow", "*.log files "))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
