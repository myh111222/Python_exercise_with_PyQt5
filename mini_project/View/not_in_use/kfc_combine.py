# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KFC_breakfast.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QWidget ,QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from datetime import datetime
import pytz

ActivButton=True
class KFC_breakfast_window(QWidget):
    def __init__(self,ActivButton=True,parent=None):
        super(KFC_breakfast_window,self).__init__(parent)
        self.setup_Ui(ActivButton)
        self.string="" # prepare the string to write to file   





    #function to clear all the user unput and remove database
    def clear_all(self): 
        self.BreakfastSetA_num.setValue(0)
        self.BreakfastSetB_num.setValue(0)
        self.BreakfastC_num.setValue(0)
        self.BreakfastD_num.setValue(0)
        self.BreakfastE_num.setValue(0)
        self.BreakfastF_num.setValue(0)
        self.KFCPepsi_num.setValue(0)
        self.KFCTea_num.setValue(0)


        
    def add_to_cart(self):
        #group all items inside dictionary
        items_lists=[
            [self.BreakfastSetA_num,self.BreakfastSetA_pric,self.BreakfastSetA_name] ,
            [self.BreakfastSetB_num,self.BreakfastSetB_pric,self.BreakfastSetB_name] ,
            [self.BreakfastC_num,self.kfcbreakfastC_pric,self.BreakfastC_name] ,
            [self.BreakfastD_num,self.BreakfastD_pric_2,self.BreakfastD_name] ,
            [self.BreakfastE_num,self.BreakfastE_pric_2,self.BreakfastE_name] ,
            [self.BreakfastF_num,self.BreakfastF_pric_2,self.BreakfastF_name] ,
            [self.KFCPepsi_num,self.KFCPepsi_pric_2,self.KFCpepsi_name] ,
            [self.KFCTea_num,self.KFCTea_pric_2,self.KFCTea_name] ,

        ]
        #prepare to write the data to database
        with open("./cart.txt","w") as f:
            for item_list in items_lists:
                print(item_list[0].value()) #for debugging
                if item_list[0].value() != 0:
                    convTotext = QtGui.QTextDocument()
                    convTotext.setHtml(item_list[2].text())
                    item_name = str(convTotext.toPlainText()) 
                    convTotext.setHtml(item_list[1].text()) #convert rich text to plain text
                    text = convTotext.toPlainText()
                    item_price_text = str(text)[1:]
                    item_price = float(item_price_text)
                    total_price = item_price*int(item_list[0].value())
                    self.string = self.string + item_name.replace(" ","_") + " " + str(item_list[0].value()) + " " +  str('{0:.2f}'.format(total_price)) + "\n" #format string and add together
            f.write(self.string) #write string to data base
            self.string=""  #clear string        



        #functions contains all menu icons
    def kfc_icon_breakfast(self):
        self.BreakfastSetC_log = QtWidgets.QLabel(self.mainwidget)
        self.BreakfastSetC_log.setGeometry(QtCore.QRect(443, 30, 111, 101))
        self.BreakfastSetC_log.setText("")
        self.BreakfastSetC_log.setPixmap(QtGui.QPixmap("./Pictures/kfc/kfcSetD.png"))
        self.BreakfastSetC_log.setScaledContents(True)
        self.BreakfastSetC_log.setObjectName("BreakfastSetC_log")
        
        self.BreakfastD_4 = QtWidgets.QLabel(self.mainwidget)
        self.BreakfastD_4.setGeometry(QtCore.QRect(654, 40, 111, 101))
        self.BreakfastD_4.setText("")
        self.BreakfastD_4.setPixmap(QtGui.QPixmap("./Pictures/kfc/kfcSetC.png"))
        self.BreakfastD_4.setScaledContents(True)
        self.BreakfastD_4.setObjectName("BreakfastD_4")

        self.BreakfastSetB_log = QtWidgets.QLabel(self.mainwidget)
        self.BreakfastSetB_log.setGeometry(QtCore.QRect(231, 30, 131, 91))
        self.BreakfastSetB_log.setText("")
        self.BreakfastSetB_log.setPixmap(QtGui.QPixmap("./Pictures/kfc/kfcBreakfastE.png"))
        self.BreakfastSetB_log.setScaledContents(True)
        self.BreakfastSetB_log.setObjectName("BreakfastSetB_log")

        self.BreakfastF_3 = QtWidgets.QLabel(self.mainwidget)
        self.BreakfastF_3.setGeometry(QtCore.QRect(241, 232, 101, 101))
        self.BreakfastF_3.setText("")
        self.BreakfastF_3.setPixmap(QtGui.QPixmap("./Pictures/kfc/kfcBreakfast2.png"))
        self.BreakfastF_3.setScaledContents(True)
        self.BreakfastF_3.setObjectName("BreakfastF_3")

        self.KFCPepsi_5 = QtWidgets.QLabel(self.mainwidget)
        self.KFCPepsi_5.setGeometry(QtCore.QRect(433, 242, 121, 91))
        self.KFCPepsi_5.setText("")
        self.KFCPepsi_5.setPixmap(QtGui.QPixmap("./Pictures/kfc/kfcpepci.png"))
        self.KFCPepsi_5.setScaledContents(True)
        self.KFCPepsi_5.setObjectName("KFCPepsi_5")

        self.KFCTea_5 = QtWidgets.QLabel(self.mainwidget)
        self.KFCTea_5.setGeometry(QtCore.QRect(594, 202, 211, 141))
        self.KFCTea_5.setText("")
        self.KFCTea_5.setPixmap(QtGui.QPixmap("./Pictures/kfc/kfcTea.png"))
        self.KFCTea_5.setScaledContents(True)
        self.KFCTea_5.setObjectName("KFCTea_5")

        self.BreakfastE_6 = QtWidgets.QLabel(self.mainwidget)
        self.BreakfastE_6.setGeometry(QtCore.QRect(20, 212, 141, 131))
        self.BreakfastE_6.setText("")
        self.BreakfastE_6.setPixmap(QtGui.QPixmap("./Pictures/kfc/kfcBreakfast1.png"))
        self.BreakfastE_6.setScaledContents(True)
        self.BreakfastE_6.setObjectName("BreakfastE_6")

        self.BreakfastSetA_log = QtWidgets.QLabel(self.mainwidget)
        self.BreakfastSetA_log.setGeometry(QtCore.QRect(20, 30, 161, 101))
        self.BreakfastSetA_log.setText("")
        self.BreakfastSetA_log.setPixmap(QtGui.QPixmap("./Pictures/kfc/kfc3.png"))
        self.BreakfastSetA_log.setScaledContents(True)
        self.BreakfastSetA_log.setObjectName("BreakfastSetA_log")

    

    #functions contains all menu prices
    def kfc_pric_breakfast(self):
        self.kfcbreakfastC_pric = QtWidgets.QLabel(self.mainwidget)
        self.kfcbreakfastC_pric.setGeometry(QtCore.QRect(473, 140, 91, 31))
        self.kfcbreakfastC_pric.setTextFormat(QtCore.Qt.RichText)
        self.kfcbreakfastC_pric.setObjectName("kfcbreakfastC_pric")

        self.BreakfastSetB_pric = QtWidgets.QLabel(self.mainwidget)
        self.BreakfastSetB_pric.setGeometry(QtCore.QRect(271, 140, 91, 31))
        self.BreakfastSetB_pric.setTextFormat(QtCore.Qt.RichText)
        self.BreakfastSetB_pric.setObjectName("BreakfastSetB_pric")

        self.BreakfastSetA_pric = QtWidgets.QLabel(self.mainwidget)
        self.BreakfastSetA_pric.setGeometry(QtCore.QRect(70, 140, 91, 31))
        self.BreakfastSetA_pric.setTextFormat(QtCore.Qt.RichText)
        self.BreakfastSetA_pric.setObjectName("BreakfastSetA_pric")
        self.BreakfastD_pric_2 = QtWidgets.QLabel(self.mainwidget)
        self.BreakfastD_pric_2.setGeometry(QtCore.QRect(674, 140, 91, 31))
        self.BreakfastD_pric_2.setTextFormat(QtCore.Qt.RichText)
        self.BreakfastD_pric_2.setObjectName("BreakfastD_pric_2")

        self.BreakfastF_pric_2 = QtWidgets.QLabel(self.mainwidget)
        self.BreakfastF_pric_2.setGeometry(QtCore.QRect(271, 342, 91, 31))
        self.BreakfastF_pric_2.setTextFormat(QtCore.Qt.RichText)
        self.BreakfastF_pric_2.setObjectName("BreakfastF_pric_2")

        self.BreakfastE_pric_2 = QtWidgets.QLabel(self.mainwidget)
        self.BreakfastE_pric_2.setGeometry(QtCore.QRect(70, 342, 91, 31))
        self.BreakfastE_pric_2.setTextFormat(QtCore.Qt.RichText)
        self.BreakfastE_pric_2.setObjectName("BreakfastE_pric_2")

        self.KFCTea_pric_2 = QtWidgets.QLabel(self.mainwidget)
        self.KFCTea_pric_2.setGeometry(QtCore.QRect(674, 342, 91, 31))
        self.KFCTea_pric_2.setTextFormat(QtCore.Qt.RichText)
        self.KFCTea_pric_2.setObjectName("KFCTea_pric_2")
        self.KFCPepsi_pric_2 = QtWidgets.QLabel(self.mainwidget)
        self.KFCPepsi_pric_2.setGeometry(QtCore.QRect(473, 342, 91, 31))
        self.KFCPepsi_pric_2.setTextFormat(QtCore.Qt.RichText)
        self.KFCPepsi_pric_2.setObjectName("KFCPepsi_pric_2")

    def KFC_breakfast_button(self):

        self.BlueButton = QtWidgets.QPushButton(self.mainwidget)
        self.BlueButton.setGeometry(QtCore.QRect(360, 470, 96, 96))
        self.BlueButton.setStyleSheet("#BlueButton {\n"
"    background-color: #2196f3;\n"
"    /*minimum size*/\n"
"    min-width: 96px;\n"
"    max-width: 96px;\n"
"    min-height: 96px;\n"
"    max-height: 96px;\n"
"    border-radius: 48px; /*Round*/\n"
"}\n"
"#BlueButton:hover {\n"
"    background-color: #64b5f6;\n"
"}\n"
"#BlueButton:pressed {\n"
"    background-color: #bbdefb;\n"
"}")
        
        self.BlueButton.setObjectName("BlueButton")

        self.BlueButton3 = QtWidgets.QPushButton(self.mainwidget)
        self.BlueButton3.setGeometry(QtCore.QRect(620, 470, 96, 96))
        self.BlueButton3.setStyleSheet("#BlueButton3 {\n"
"    background-color: #2196f3;\n"
"    /*minimum size*/\n"
"    min-width: 96px;\n"
"    max-width: 96px;\n"
"    min-height: 96px;\n"
"    max-height: 96px;\n"
"    border-radius: 48px; /*Round*/\n"
"}\n"
"#BlueButton3:hover {\n"
"    background-color: #64b5f6;\n"
"}\n"
"#BlueButton3:pressed {\n"
"    background-color: #bbdefb;\n"
"}")
        self.BlueButton3.setObjectName("BlueButton3")

        self.BlueButton2 = QtWidgets.QPushButton(self.mainwidget)
        self.BlueButton2.setGeometry(QtCore.QRect(490, 470, 96, 96))
        self.BlueButton2.setStyleSheet("#BlueButton2 {\n"
"    background-color: #2196f3;\n"
"    /*minimum size*/\n"
"    min-width: 96px;\n"
"    max-width: 96px;\n"
"    min-height: 96px;\n"
"    max-height: 96px;\n"
"    border-radius: 48px; /*Round*/\n"
"}\n"
"#BlueButton2:hover {\n"
"    background-color: #64b5f6;\n"
"}\n"
"#BlueButton2:pressed {\n"
"    background-color: #bbdefb;\n"
"}")
        self.BlueButton2.setObjectName("BlueButton2")
        self.BlueButton2.clicked.connect(self.clear_all)   # clear_all
        self.BlueButton3.clicked.connect(self.add_to_cart) # add the user input and calculate price
        self.OperHourlabel = QtWidgets.QLabel(self.mainwidget)
        self.OperHourlabel.setEnabled(True)
        self.OperHourlabel.setGeometry(QtCore.QRect(50, 400, 311, 181))
        self.OperHourlabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.OperHourlabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.OperHourlabel.setTextFormat(QtCore.Qt.RichText)
        self.OperHourlabel.setObjectName("OperHourlabel")
        self.BlueButton.pressed.connect(self.OperHourlabel.show)# functions for OperHourlabel
        self.BlueButton.released.connect(self.OperHourlabel.hide)# functions for OperHourlabel
        self.OperHourlabel.hide()
        _translate = QtCore.QCoreApplication.translate
        self.BlueButton.setText(_translate("MainWindow", "Operation \n""Hour"))
        self.BlueButton3.setText(_translate("MainWindow", "Add To \n""Chart"))
        self.BlueButton2.setText(_translate("MainWindow", "Clear All"))
        self.OperHourlabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#cc0000;\">KFC</span><span style=\" font-size:12pt; font-weight:600;\"> is one of popular franchised outlets </span></p><p><span style=\" font-size:12pt; font-weight:600;\">suitable for all people !</span></p><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">The operation hour is:</span></p><p><span style=\" font-size:18pt; font-weight:600; font-style:italic; color:#ef2929;\">Monday to Sunday </span></p><p><span style=\" font-size:18pt; font-weight:600; font-style:italic; color:#ef2929;\">8:00am to 9:00pm</span></p><p><span style=\" font-size:20pt; font-weight:600; font-style:italic; color:#ef2929;\">Haha</span></p></body></html>"))

    #function for quanlity of food
    def kfc_Breakfast_num(self):
        self.BreakfastSetA_num = QtWidgets.QSpinBox(self.mainwidget)
        self.BreakfastSetA_num.setGeometry(QtCore.QRect(71, 172, 48, 26))
        self.BreakfastSetA_num.setObjectName("BreakfastSetA_num")
        self.BreakfastSetB_num = QtWidgets.QSpinBox(self.mainwidget)
        self.BreakfastSetB_num.setGeometry(QtCore.QRect(271, 170, 48, 26))
        self.BreakfastSetB_num.setObjectName("BreakfastSetB_num")
        self.BreakfastC_num = QtWidgets.QSpinBox(self.mainwidget)
        self.BreakfastC_num.setGeometry(QtCore.QRect(473, 170, 48, 26))
        self.BreakfastC_num.setObjectName("BreakfastC_num")
        self.BreakfastD_num = QtWidgets.QSpinBox(self.mainwidget)
        self.BreakfastD_num.setGeometry(QtCore.QRect(674, 170, 48, 26))
        self.BreakfastD_num.setObjectName("BreakfastD_num_2")
        self.BreakfastE_num = QtWidgets.QSpinBox(self.mainwidget)
        self.BreakfastE_num.setGeometry(QtCore.QRect(70, 372, 48, 26))
        self.BreakfastE_num.setObjectName("BreakfastE_num_2")
        self.BreakfastF_num = QtWidgets.QSpinBox(self.mainwidget)
        self.BreakfastF_num.setGeometry(QtCore.QRect(271, 372, 48, 26))
        self.BreakfastF_num.setObjectName("BreakfastF_num_2")
        self.KFCTea_num = QtWidgets.QSpinBox(self.mainwidget)
        self.KFCTea_num.setGeometry(QtCore.QRect(674, 372, 48, 26))
        self.KFCTea_num.setObjectName("KFCTea_num_2")
        self.KFCPepsi_num = QtWidgets.QSpinBox(self.mainwidget)
        self.KFCPepsi_num.setGeometry(QtCore.QRect(473, 372, 48, 26))
        self.KFCPepsi_num.setObjectName("KFCPepsi_num_2")



    def setup_Ui(self,ActivButton):
        self.setObjectName("MainWindow")
        self.resize(800, 600)

        #set a stall background
        self.mainwidget = QtWidgets.QWidget(self)
        self.kfcBackpic = QtWidgets.QLabel(self.mainwidget)
        self.kfcBackpic.setPixmap(QtGui.QPixmap("./Pictures/kfc/background3_1.jpg"))
        self.kfcBackpic.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.kfcBackpic.setText("")
        self.kfcBackpic.setScaledContents(True)
        self.kfcBackpic.setObjectName("kfcBackpic")

        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setMaximumSize(QtCore.QSize(800, 600))
        self.mainwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.mainwidget.setObjectName("mainwidget")

        self.kfc_pric_breakfast() # call price function
        self.kfc_icon_breakfast() # call this icon function
        # choose to activate buttons and display quanlity of food when "ActivButton==True"
        if ActivButton==True:
            print (ActivButton)
            self.KFC_breakfast_button() #  call button function
            self.kfc_Breakfast_num()    #  call function for quanlity of food





        self.KFCTea_name = QtWidgets.QLabel(self.mainwidget)
        self.KFCTea_name.setGeometry(QtCore.QRect(654, 322, 121, 31))
        self.KFCTea_name.setTextFormat(QtCore.Qt.RichText)
        self.KFCTea_name.setObjectName("KFCTea_name")

        self.BreakfastF_name = QtWidgets.QLabel(self.mainwidget)
        self.BreakfastF_name.setGeometry(QtCore.QRect(241, 322, 121, 31))
        self.BreakfastF_name.setTextFormat(QtCore.Qt.RichText)
        self.BreakfastF_name.setObjectName("BreakfastF_name")


        self.BreakfastC_name = QtWidgets.QLabel(self.mainwidget)
        self.BreakfastC_name.setGeometry(QtCore.QRect(443, 120, 121, 31))
        self.BreakfastC_name.setTextFormat(QtCore.Qt.RichText)
        self.BreakfastC_name.setObjectName("BreakfastC_name")


        self.BreakfastD_name = QtWidgets.QLabel(self.mainwidget)
        self.BreakfastD_name.setGeometry(QtCore.QRect(644, 120, 121, 31))
        self.BreakfastD_name.setTextFormat(QtCore.Qt.RichText)
        self.BreakfastD_name.setObjectName("BreakfastD_name")

        self.KFCpepsi_name = QtWidgets.QLabel(self.mainwidget)
        self.KFCpepsi_name.setGeometry(QtCore.QRect(463, 322, 121, 31))
        self.KFCpepsi_name.setTextFormat(QtCore.Qt.RichText)
        self.KFCpepsi_name.setObjectName("KFCpepsi_name")



        self.BreakfastSetA_name = QtWidgets.QLabel(self.mainwidget)
        self.BreakfastSetA_name.setGeometry(QtCore.QRect(40, 120, 121, 31))
        self.BreakfastSetA_name.setTextFormat(QtCore.Qt.RichText)
        self.BreakfastSetA_name.setObjectName("BreakfastSetA_name")


        self.BreakfastSetB_name = QtWidgets.QLabel(self.mainwidget)
        self.BreakfastSetB_name.setGeometry(QtCore.QRect(241, 120, 121, 31))
        self.BreakfastSetB_name.setTextFormat(QtCore.Qt.RichText)
        self.BreakfastSetB_name.setObjectName("BreakfastSetB_name")

        self.BreakfastE_name = QtWidgets.QLabel(self.mainwidget)
        self.BreakfastE_name.setGeometry(QtCore.QRect(40, 322, 121, 31))
        self.BreakfastE_name.setTextFormat(QtCore.Qt.RichText)
        self.BreakfastE_name.setObjectName("BreakfastE_name")


        self.dailyMenu_label = QtWidgets.QLabel(self.mainwidget)
        self.dailyMenu_label.setGeometry(QtCore.QRect(90, 0, 200, 41))
        self.dailyMenu_label.setTextFormat(QtCore.Qt.RichText)
        self.dailyMenu_label.setObjectName("dailyMenu_label")
        self.KFClogo = QtWidgets.QLabel(self.mainwidget)
        self.KFClogo.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.KFClogo.setText("")
        self.KFClogo.setPixmap(QtGui.QPixmap("./Pictures/kfc/kfc-logo.png"))
        self.KFClogo.setScaledContents(True)
        self.KFClogo.setObjectName("KFClogo")


        QtCore.QMetaObject.connectSlotsByName(self)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))


        #text for menu and etc
        def text_name_breakfast(self):

            self.BreakfastSetA_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Breakfast Set A</span></p></body></html>"))
            self.BreakfastSetB_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Breakfast Set B</span></p></body></html>"))
            self.BreakfastC_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Breakfast Set C</span></p></body></html>"))
            self.BreakfastD_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Breakfast D</span></p></body></html>"))
            self.BreakfastE_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Breakfast set E</span></p></body></html>"))
            self.BreakfastF_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Breakfast set F</span></p></body></html>"))
            self.KFCpepsi_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Cool Pepsi</span></p></body></html>"))
            self.KFCTea_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Cool Lemon Tea</span></p></body></html>"))

        text_name_breakfast(self)
        self.kfcbreakfastC_pric.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">$7.00</span></p></body></html>"))
        self.KFCTea_pric_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">$2.00</span></p></body></html>"))
        self.KFCPepsi_pric_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">$2.00</span></p></body></html>"))
        
        self.BreakfastE_pric_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">$8.00</span></p></body></html>"))
        self.BreakfastF_pric_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">$5.00</span></p></body></html>"))
        self.BreakfastD_pric_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">$4.00</span></p></body></html>"))
        self.BreakfastSetB_pric.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">$7.00</span></p></body></html>"))
        self.BreakfastSetA_pric.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">$5.00</span></p></body></html>"))
        self.dailyMenu_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic; color:#fcaf3e;\">Breakfast Menu</span></p></body></html>"))



###====================########=========================##############=========================
#==============================================================================================

###====================########=========================##############=========================
#==============================================================================================





class KFC_daily_window(QWidget):
    def __init__(self,ActivButton=True,parent=None):
        super(KFC_daily_window,self).__init__(parent)
        self.setup_Ui(ActivButton)
        self.string="" # prepare the string to write to file

    #function to clear all the user unput and remove database
    def clear_all(self): 
        self.KFCsetA_num.setValue(0)
        self.KFCSetB_num.setValue(0)
        self.KFCSetC_num.setValue(0)
        self.KFCSetD_num.setValue(0)
        self.KFCSetE_num.setValue(0)
        self.KFCSetF_num.setValue(0)
        self.KFCPepsi_num.setValue(0)
        self.KFCFries_num.setValue(0)
        
    def add_to_cart(self):
        #group all items inside dictionary
        items_lists=[
            [self.KFCsetA_num,self.KFCsetA_pric,self.KFCsetA_name] ,
            [self.KFCSetB_num,self.KFCSetB_pric,self.KFCSetB_name] ,
            [self.KFCSetC_num,self.KFCSetC_pric,self.KFCSetC_name] ,
            [self.KFCSetD_num,self.KFCSetD_pric,self.KFCSetD_name] ,
            [self.KFCSetE_num,self.KFCSetE_pric,self.KFCSetE_name] ,
            [self.KFCSetF_num,self.KFCSetF_pric,self.KFCSetF_name] ,
            [self.KFCPepsi_num,self.KFCPepsi_pric,self.KFCPepsi_name] ,
            [self.KFCFries_num,self.KFCFries_pric,self.KFCFries_name] ,
        ]
        #prepare to write the data to database
        with open("./cart.txt","w") as f:
            for item_list in items_lists:
                print(item_list[0].value()) #for debugging
                if item_list[0].value() != 0:
                    convTotext = QtGui.QTextDocument()
                    convTotext.setHtml(item_list[2].text())
                    item_name = str(convTotext.toPlainText()) #convert rich text to plain
                    convTotext.setHtml(item_list[1].text())
                    text = convTotext.toPlainText()
                    item_price_text = str(text)[1:]
                    item_price = float(item_price_text)
                    total_price = item_price*int(item_list[0].value())
                    self.string = self.string + item_name.replace(" ","_") + " " + str(item_list[0].value()) + " " +  str('{0:.2f}'.format(total_price)) + "\n" #format string and add together
            f.write(self.string) #write string to data base
            self.string=""  #clear string   


    

    def kfc_daily_button(self):
        print ("kfc_daily_button")

        self.ClearButton2 = QtWidgets.QPushButton(self.mainwidget)
        self.ClearButton2.setGeometry(QtCore.QRect(490, 470, 96, 96))
        self.ClearButton2.setStyleSheet("#ClearButton2 {\n"
"    background-color: #2196f3;\n"
"    /*minimum size*/\n"
"    min-width: 80px;\n"
"    max-width: 80px;\n"
"    min-height: 80px;\n"
"    max-height: 80px;\n"
"    border-radius: 48px; /*Round*/\n"
"}\n"
"#ClearButton2:hover {\n"
"    background-color: #64b5f6;\n"
"}\n"
"#ClearButton2:pressed {\n"
"    background-color: #bbdefb;\n"
"}")
        self.ClearButton2.setObjectName("ClearButton2")
        self.BlueButton = QtWidgets.QPushButton(self.mainwidget)
        self.BlueButton.setGeometry(QtCore.QRect(360, 470, 96, 96))
        self.BlueButton.setObjectName("BlueButton")
        self.BlueButton.setStyleSheet("#BlueButton {\n"
"    background-color: #2196f3;\n"
"    /*minimum size*/\n"
"    min-width: 80px;\n"
"    max-width: 80px;\n"
"    min-height: 80px;\n"
"    max-height: 80px;\n"
"    border-radius: 48px; /*Round*/\n"
"}\n"
"#BlueButton:hover {\n"
"    background-color: #64b5f6;\n"
"}\n"
"#BlueButton:pressed {\n"
"    background-color: #bbdefb;\n"
"}")
        
        self.AddToChartButton = QtWidgets.QPushButton(self.mainwidget)
        self.AddToChartButton.setGeometry(QtCore.QRect(620, 470, 96, 96))
        self.AddToChartButton.setStyleSheet("#AddToChartButton {\n"
"    background-color: #2196f3;\n"
"    /*minimum size*/\n"
"    min-width: 80px;\n"
"    max-width: 80px;\n"
"    min-height: 80px;\n"
"    max-height: 80px;\n"
"    border-radius: 48px; /*Round*/\n"
"}\n"
"#AddToChartButton:hover {\n"
"    background-color: #64b5f6;\n"
"}\n"
"#AddToChartButton:pressed {\n"
"    background-color: #bbdefb;\n"
"}")

        self.AddToChartButton.setObjectName("AddToChartButton")
        self.ClearButton2.clicked.connect(self.clear_all)   # clear_all   
        self.AddToChartButton.clicked.connect(self.add_to_cart) #add the user input and calculate price
        self.OperHourlabel = QtWidgets.QLabel(self.mainwidget)
        self.OperHourlabel.setEnabled(True)
        self.OperHourlabel.setGeometry(QtCore.QRect(50, 400, 311, 180))
        self.OperHourlabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.OperHourlabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.OperHourlabel.setTextFormat(QtCore.Qt.RichText)
        self.OperHourlabel.setObjectName("OperHourlabel")
        self.BlueButton.pressed.connect(self.OperHourlabel.show)# functions for show OperHourlabel
        self.BlueButton.released.connect(self.OperHourlabel.hide)# functions for hide OperHourlabel
        self.OperHourlabel.hide()
        _translate = QtCore.QCoreApplication.translate
        self.BlueButton.setText(_translate("MainWindow", "Operation \n""Hour"))
        self.ClearButton2.setText(_translate("MainWindow", "Clear All"))
        self.AddToChartButton.setText(_translate("MainWindow", "Add To \n""Chart"))
        self.OperHourlabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#cc0000;\">KFC</span><span style=\" font-size:12pt; font-weight:600;\"> is one of popular franchised outlets </span></p><p><span style=\" font-size:12pt; font-weight:600;\">suitable for all people !</span></p><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">The operation hour is:</span></p><p><span style=\" font-size:18pt; font-weight:600; font-style:italic; color:#ef2929;\">Monday to Sunday </span></p><p><span style=\" font-size:18pt; font-weight:600; font-style:italic; color:#ef2929;\">8:00am to 9:00pm</span></p><p><span style=\" font-size:20pt; font-weight:600; font-style:italic; color:#ef2929;\">Haha</span></p></body></html>"))




    def setup_Ui(self,ActivButton):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setMaximumSize(QtCore.QSize(800, 600))
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mainwidget = QtWidgets.QWidget(self)
        self.mainwidget.setObjectName("mainwidget")
        def kfc_daily_num(self):
            print ("kfc_daily_num")
            self.KFCsetA_num = QtWidgets.QSpinBox(self.mainwidget)
            self.KFCsetA_num.setGeometry(QtCore.QRect(67, 170, 48, 26))
            self.KFCsetA_num.setObjectName("KFCsetA_num")   
            self.KFCsetA_name = QtWidgets.QLabel(self.mainwidget)
            self.KFCSetB_num = QtWidgets.QSpinBox(self.mainwidget)
            self.KFCSetB_num.setGeometry(QtCore.QRect(268, 170, 48, 26))
            self.KFCSetB_num.setObjectName("KFCSetB_num")
            self.KFCSetC_num = QtWidgets.QSpinBox(self.mainwidget)
            self.KFCSetC_num.setGeometry(QtCore.QRect(470, 170, 48, 26))
            self.KFCSetC_num.setObjectName("KFCSetC_num")
            self.KFCSetD_num = QtWidgets.QSpinBox(self.mainwidget)
            self.KFCSetD_num.setGeometry(QtCore.QRect(671, 170, 48, 26))
            self.KFCSetD_num.setObjectName("KFCSetD_num")
            self.KFCSetE_num = QtWidgets.QSpinBox(self.mainwidget)
            self.KFCSetE_num.setGeometry(QtCore.QRect(67, 362, 48, 26))
            self.KFCSetE_num.setObjectName("KFCSetE_num")
            self.KFCSetF_num = QtWidgets.QSpinBox(self.mainwidget)
            self.KFCSetF_num.setGeometry(QtCore.QRect(268, 362, 48, 26))
            self.KFCSetF_num.setObjectName("KFCSetF_num")
            self.KFCPepsi_num = QtWidgets.QSpinBox(self.mainwidget)
            self.KFCPepsi_num.setGeometry(QtCore.QRect(671, 362, 48, 26))
            self.KFCPepsi_num.setObjectName("KFCPepsi_num")
            self.KFCFries_num = QtWidgets.QSpinBox(self.mainwidget)
            self.KFCFries_num.setGeometry(QtCore.QRect(470, 362, 48, 26))
            self.KFCFries_num.setObjectName("KFCFries_num")
            self.kfcBackpic = QtWidgets.QLabel(self.mainwidget)
            self.kfcBackpic.setGeometry(QtCore.QRect(5, 0, 800, 600))
            self.kfcBackpic.setText("")
            self.kfcBackpic.setPixmap(QtGui.QPixmap("./Pictures/kfc/background3_1.jpg"))
            self.kfcBackpic.setScaledContents(True)
            self.kfcBackpic.setObjectName("kfcBackpic")

        #self.kfc_pric_breakfast() # call price function
        #self.kfc_icon_breakfast() # call this icon function
        # choose to activate buttons and display quanlity of food when "ActivButton==True"
        #self.KFC_daily_button()
        self.kfc_daily_button() #  call button function
        kfc_daily_num(self)    #  call function for quanlity of food

        #if ActivButton==True:
        #    print ("ActivButton: ",ActivButton)
        #    #self.KFC_breakfast_button()

        
        self.KFCsetA_name.setGeometry(QtCore.QRect(57, 120, 121, 31))
        self.KFCsetA_name.setTextFormat(QtCore.Qt.RichText)
        self.KFCsetA_name.setObjectName("KFCsetA_name")

        self.KFCsetA_3 = QtWidgets.QLabel(self.mainwidget)
        self.KFCsetA_3.setGeometry(QtCore.QRect(27, 30, 141, 101))
        self.KFCsetA_3.setText("")
        self.KFCsetA_3.setPixmap(QtGui.QPixmap("./Pictures/kfc/kfc1.png"))
        self.KFCsetA_3.setScaledContents(True)
        self.KFCsetA_3.setObjectName("KFCsetA_3")

        self.KFCsetA_pric = QtWidgets.QLabel(self.mainwidget)
        self.KFCsetA_pric.setGeometry(QtCore.QRect(67, 140, 91, 31))
        self.KFCsetA_pric.setTextFormat(QtCore.Qt.RichText)
        self.KFCsetA_pric.setObjectName("KFCsetA_pric")

        self.KFCSetB_pric = QtWidgets.QLabel(self.mainwidget)
        self.KFCSetB_pric.setGeometry(QtCore.QRect(268, 140, 91, 31))
        self.KFCSetB_pric.setTextFormat(QtCore.Qt.RichText)
        self.KFCSetB_pric.setObjectName("KFCSetB_pric")


        self.KFCSetB_name = QtWidgets.QLabel(self.mainwidget)
        self.KFCSetB_name.setGeometry(QtCore.QRect(258, 120, 121, 31))
        self.KFCSetB_name.setTextFormat(QtCore.Qt.RichText)
        self.KFCSetB_name.setObjectName("KFCSetB_name")

        self.KFCSetB_3 = QtWidgets.QLabel(self.mainwidget)
        self.KFCSetB_3.setGeometry(QtCore.QRect(228, 30, 131, 91))
        self.KFCSetB_3.setText("")
        self.KFCSetB_3.setPixmap(QtGui.QPixmap("./Pictures/kfc/kfc2.png"))
        self.KFCSetB_3.setScaledContents(True)
        self.KFCSetB_3.setObjectName("KFCSetB_3")
        self.KFCSetC_pric = QtWidgets.QLabel(self.mainwidget)
        self.KFCSetC_pric.setGeometry(QtCore.QRect(470, 140, 91, 31))
        self.KFCSetC_pric.setTextFormat(QtCore.Qt.RichText)
        self.KFCSetC_pric.setObjectName("KFCSetC_pric")

        self.KFCSetC_name = QtWidgets.QLabel(self.mainwidget)
        self.KFCSetC_name.setGeometry(QtCore.QRect(460, 120, 121, 31))
        self.KFCSetC_name.setTextFormat(QtCore.Qt.RichText)
        self.KFCSetC_name.setObjectName("KFCSetC_name")
        self.KFCSetC_3 = QtWidgets.QLabel(self.mainwidget)
        self.KFCSetC_3.setGeometry(QtCore.QRect(420, 30, 151, 101))
        self.KFCSetC_3.setText("")
        self.KFCSetC_3.setPixmap(QtGui.QPixmap("./Pictures/kfc/kfc3.png"))
        self.KFCSetC_3.setScaledContents(True)
        self.KFCSetC_3.setObjectName("KFCSetC_3")

        self.KFCSetD_name = QtWidgets.QLabel(self.mainwidget)
        self.KFCSetD_name.setGeometry(QtCore.QRect(661, 120, 121, 31))
        self.KFCSetD_name.setTextFormat(QtCore.Qt.RichText)
        self.KFCSetD_name.setObjectName("KFCSetD_name")

        self.KFCSetD_3 = QtWidgets.QLabel(self.mainwidget)
        self.KFCSetD_3.setGeometry(QtCore.QRect(611, 10, 161, 151))
        self.KFCSetD_3.setText("")
        self.KFCSetD_3.setPixmap(QtGui.QPixmap("./Pictures/kfc/kfcSetG.png"))
        self.KFCSetD_3.setScaledContents(True)
        self.KFCSetD_3.setObjectName("KFCSetD_3")

        self.KFCSetE_pric = QtWidgets.QLabel(self.mainwidget)
        self.KFCSetE_pric.setGeometry(QtCore.QRect(67, 332, 91, 31))
        self.KFCSetE_pric.setTextFormat(QtCore.Qt.RichText)
        self.KFCSetE_pric.setObjectName("KFCSetE_pric")

        self.KFCSetE_name = QtWidgets.QLabel(self.mainwidget)
        self.KFCSetE_name.setGeometry(QtCore.QRect(57, 312, 121, 31))
        self.KFCSetE_name.setTextFormat(QtCore.Qt.RichText)
        self.KFCSetE_name.setObjectName("KFCSetE_name")

        self.KFCSetE_5 = QtWidgets.QLabel(self.mainwidget)
        self.KFCSetE_5.setGeometry(QtCore.QRect(17, 222, 141, 101))
        self.KFCSetE_5.setText("")
        self.KFCSetE_5.setPixmap(QtGui.QPixmap("./Pictures/kfc/kfcBreakfastE.png"))
        self.KFCSetE_5.setScaledContents(True)
        self.KFCSetE_5.setObjectName("KFCSetE_5")
        self.KFCSetD_pric = QtWidgets.QLabel(self.mainwidget)
        self.KFCSetD_pric.setGeometry(QtCore.QRect(671, 140, 91, 31))
        self.KFCSetD_pric.setTextFormat(QtCore.Qt.RichText)
        self.KFCSetD_pric.setObjectName("KFCSetD_pric")

        self.KFCSetF_name = QtWidgets.QLabel(self.mainwidget)
        self.KFCSetF_name.setGeometry(QtCore.QRect(260, 312, 121, 31))
        self.KFCSetF_name.setTextFormat(QtCore.Qt.RichText)
        self.KFCSetF_name.setObjectName("KFCSetF_name")

        self.KFCSetF_2 = QtWidgets.QLabel(self.mainwidget)
        self.KFCSetF_2.setGeometry(QtCore.QRect(248, 212, 101, 141))
        self.KFCSetF_2.setText("")
        self.KFCSetF_2.setPixmap(QtGui.QPixmap("./Pictures/kfc/kfcSetH.png"))
        self.KFCSetF_2.setScaledContents(True)
        self.KFCSetF_2.setObjectName("KFCSetF_2")
        self.KFCSetF_pric = QtWidgets.QLabel(self.mainwidget)
        self.KFCSetF_pric.setGeometry(QtCore.QRect(268, 332, 91, 31))
        self.KFCSetF_pric.setTextFormat(QtCore.Qt.RichText)
        self.KFCSetF_pric.setObjectName("KFCSetF_pric")

        self.KFCPepsi_2 = QtWidgets.QLabel(self.mainwidget)
        self.KFCPepsi_2.setGeometry(QtCore.QRect(631, 232, 131, 91))
        self.KFCPepsi_2.setText("")
        self.KFCPepsi_2.setPixmap(QtGui.QPixmap("./Pictures/kfc/kfcpepci.png"))
        self.KFCPepsi_2.setScaledContents(True)
        self.KFCPepsi_2.setObjectName("KFCPepsi_2")
        self.KFCPepsi_pric = QtWidgets.QLabel(self.mainwidget)
        self.KFCPepsi_pric.setGeometry(QtCore.QRect(671, 332, 91, 31))
        self.KFCPepsi_pric.setTextFormat(QtCore.Qt.RichText)
        self.KFCPepsi_pric.setObjectName("KFCPepsi_pric")
        self.KFCPepsi_name = QtWidgets.QLabel(self.mainwidget)
        self.KFCPepsi_name.setGeometry(QtCore.QRect(661, 312, 121, 31))
        self.KFCPepsi_name.setTextFormat(QtCore.Qt.RichText)
        self.KFCPepsi_name.setObjectName("KFCPepsi_name")

        self.KFCFries_name = QtWidgets.QLabel(self.mainwidget)
        self.KFCFries_name.setGeometry(QtCore.QRect(460, 312, 121, 31))
        self.KFCFries_name.setTextFormat(QtCore.Qt.RichText)
        self.KFCFries_name.setObjectName("KFCFries_name")

        self.KFCFries_pric = QtWidgets.QLabel(self.mainwidget)
        self.KFCFries_pric.setGeometry(QtCore.QRect(470, 332, 91, 31))
        self.KFCFries_pric.setTextFormat(QtCore.Qt.RichText)
        self.KFCFries_pric.setObjectName("KFCFries_pric")
        self.KFCFries_2 = QtWidgets.QLabel(self.mainwidget)
        self.KFCFries_2.setGeometry(QtCore.QRect(440, 212, 111, 111))
        self.KFCFries_2.setText("")
        self.KFCFries_2.setPixmap(QtGui.QPixmap("./Pictures/kfc/KFCFries.png"))
        self.KFCFries_2.setScaledContents(True)
        self.KFCFries_2.setObjectName("KFCFries_2")

#=======================#======================#======================#======================#================#
#labels
        
        self.dailyMenu_label = QtWidgets.QLabel(self.mainwidget)
        self.dailyMenu_label.setGeometry(QtCore.QRect(90, 0, 141, 41))
        self.dailyMenu_label.setTextFormat(QtCore.Qt.RichText)
        self.dailyMenu_label.setObjectName("dailyMenu_label")
        self.KFClogo = QtWidgets.QLabel(self.mainwidget)
        self.KFClogo.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.KFClogo.setText("")
        self.KFClogo.setPixmap(QtGui.QPixmap("./Pictures/kfc/kfc-logo.png"))
        self.KFClogo.setScaledContents(True)
        self.KFClogo.setObjectName("KFClogo")
        QtCore.QMetaObject.connectSlotsByName(self)

#=======================#======================#======================#======================#================#
#buttons

        QtCore.QMetaObject.connectSlotsByName(self)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        def texr_name_daily(self):
            self.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.KFCsetA_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">KFC Set A</span></p></body></html>"))
            self.KFCSetB_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">KFC Set B</span></p></body></html>"))
            self.KFCSetC_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">KFC Set C</span></p></body></html>"))
            self.KFCSetD_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">KFC Set D</span></p></body></html>"))
            self.KFCSetE_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">KFC Set E</span></p></body></html>"))
            self.KFCSetF_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">KFC set F</span></p></body></html>"))
            self.KFCFries_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Franch Fries</span></p></body></html>"))
            self.KFCPepsi_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Cool Pepsi</span></p></body></html>"))

        texr_name_daily(self)

        self.KFCsetA_pric.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">$5.00</span></p></body></html>"))
        self.KFCSetB_pric.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">$7.00</span></p></body></html>"))
        self.KFCSetC_pric.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">$7.00</span></p></body></html>"))
        self.KFCSetD_pric.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">$4.00</span></p></body></html>"))
        self.KFCSetE_pric.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">$7.50</span></p></body></html>"))
        self.KFCFries_pric.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">$3.00</span></p></body></html>"))
        self.KFCPepsi_pric.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">$2.00</span></p></body></html>"))
        self.KFCSetF_pric.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">$5.00</span></p></body></html>"))

        self.dailyMenu_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic; color:#fcaf3e;\">Daily Menu</span></p></body></html>"))


     

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = KFC_daily_window()
    window.show()
    sys.exit(app.exec_())


