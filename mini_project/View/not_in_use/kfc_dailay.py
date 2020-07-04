from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QWidget ,QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from datetime import datetime
import pytz




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


    

    def kfc_daily_buttons(self):
        print ("kfc_daily_button")

        self.ClearButton2 = QtWidgets.QPushButton(self.mainwidget)
        self.ClearButton2.setGeometry(QtCore.QRect(490, 470, 96, 96))
        self.ClearButton2.setStyleSheet("#ClearButton2 {\n"
"    background-color: #2196f3;\n"
"    /*minimum size*/\n"
"    min-width: 96px;\n"
"    max-width: 96px;\n"
"    min-height: 96px;\n"
"    max-height: 96px;\n"
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
        
        self.AddToChartButton = QtWidgets.QPushButton(self.mainwidget)
        self.AddToChartButton.setGeometry(QtCore.QRect(620, 470, 96, 96))
        self.AddToChartButton.setStyleSheet("#AddToChartButton {\n"
"    background-color: #2196f3;\n"
"    /*minimum size*/\n"
"    min-width: 96px;\n"
"    max-width: 96px;\n"
"    min-height: 96px;\n"
"    max-height: 96px;\n"
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

    def kfc_daily_num(self):
        print ("kfc_daily_num")
        self.KFCsetA_num = QtWidgets.QSpinBox(self.mainwidget)
        self.KFCsetA_num.setGeometry(QtCore.QRect(67, 170, 48, 26))
        self.KFCsetA_num.setObjectName("KFCsetA_num")   
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



    def setup_Ui(self,ActivButton):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setMaximumSize(QtCore.QSize(800, 600))
        self.mainwidget = QtWidgets.QWidget(self)
        self.mainwidget.setObjectName("mainwidget")

        #set a stall background picture
        self.kfcBackpic = QtWidgets.QLabel(self.mainwidget)
        self.kfcBackpic.setGeometry(QtCore.QRect(5, 0, 800, 600))
        self.kfcBackpic.setText("")
        self.kfcBackpic.setPixmap(QtGui.QPixmap("./Pictures/kfc/background3_1.jpg"))
        self.kfcBackpic.setScaledContents(True)
        self.kfcBackpic.setObjectName("kfcBackpic")


        #choose to activate buttons and display quanlity of food when "ActivButton==True"

        #ActivButton=False, test case
        if ActivButton==True:
            print ("ActivButton: ",ActivButton)
            self.kfc_daily_buttons() #  call buttons function
            self.kfc_daily_num()     #  call function for quanlity of food

        self.KFCsetA_name = QtWidgets.QLabel(self.mainwidget)
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


     
