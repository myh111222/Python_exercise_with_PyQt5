from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QWidget ,QMessageBox,QApplication,QStackedWidget ,QHeaderView,QVBoxLayout ,QFrame,QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal, QTimer,QDate, QTime
import os
from datetime import datetime
import pytz
import sys
class Pay_First_Page(QWidget):
    #initialize
    def __init__(self,parent=None):
        super(Pay_First_Page,self).__init__(parent)
        self.setup_Ui()
        self.BlueButton2.clicked.connect(self.load_data) #to load data from cart.txt
    
    def setup_Ui(self):
        self.setObjectName("Pay_First_Page")
        self.resize(800, 600)
        #set a stall background
        self.centralwidget = QtWidgets.QWidget(self)
        self.CrtPayBackpic = QtWidgets.QLabel(self.centralwidget)
        self.CrtPayBackpic.setPixmap(QtGui.QPixmap("./Pictures/northspine.jpg"))
        self.CrtPayBackpic.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.CrtPayBackpic.setScaledContents(True)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 90, 331, 321))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./Pictures/NTU.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(240, 30, 350, 51))

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(400, 90, 341, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.tableWidget.horizontalHeader().setFont(font)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['Items','Numbers','Price'])
        self.tableWidget.horizontalHeader().setFixedHeight(50)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.BlueButton = QtWidgets.QPushButton(self)
        self.BlueButton.setGeometry(QtCore.QRect(30, 430, 96, 96))
        self.BlueButton.setStyleSheet("#BlueButton {\n"
"    background-color: #303d5e;\n"
"    min-width: 96px;\n"
"    max-width: 96px;\n"
"    min-height: 96px;\n"
"    max-height: 96px;\n"
"    border-radius: 48px; \n"
"    color: #FFFFFF;\n"
"}\n"
"#BlueButton:hover {\n"
"    background-color: #516cb0;\n"
"}\n"
"#BlueButton:pressed {\n"
"    background-color: #04070f;\n"
"}")
        self.BlueButton.setObjectName("BlueButton")
        self.BlueButton2 = QtWidgets.QPushButton(self)
        self.BlueButton2.setGeometry(QtCore.QRect(240, 430, 96, 96))
        self.BlueButton2.setStyleSheet("#BlueButton2{\n"
"    background-color: #303d5e;\n"
"    min-width: 96px;\n"
"    max-width: 96px;\n"
"    min-height: 96px;\n"
"    max-height: 96px;\n"
"    border-radius: 48px; \n"
"    color: #FFFFFF;\n"
"}\n"
"#BlueButton2:hover {\n"
"    background-color: #516cb0;\n"
"}\n"
"#BlueButton2:pressed {\n"
"    background-color: #04070f;\n"
"}")
        self.BlueButton2.setObjectName("BlueButton2")
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Cart_and_Pay", "Form"))
        self.label_2.setText(_translate("Cart_and_Pay", "<html><p><span style=\" font-size:26pt; font-weight:700; font-style:italic; color:#fcbf3e;\">Pay Your Bill Here<br /> </span></p></html>"))
        self.BlueButton.setText(_translate("Cart_and_Pay", "Pay"))
        self.BlueButton2.setText(_translate("Cart_and_Pay", "Load Data"))
        self.BlueButton.hide()
    #functions to load data
    def load_data(self):
        data = self.read_data()
        if data != "Error":
            total_price = 0.0
            for row_data_set in data:
                single_data = row_data_set.split() #split data from the data set
                self.add_item(single_data[0],single_data[1],single_data[2])
                total_price = total_price + float(single_data[2])
            row = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(row+1)
            self.tableWidget.setItem(row,0,QTableWidgetItem("Total:"))
            self.tableWidget.setItem(row,2,QTableWidgetItem(str(total_price)[0:5]))
            self.BlueButton.show()
            self.BlueButton2.hide()
        else:
            self.msg = QMessageBox(self) #if no data found, exit the app
            #self.msg.setIcon(QMessageBox.Information)
            #self.msg.setText("asd")
            self.msg.setStyleSheet("QLabel{min-width:200 px; font-size: 24px;} QPushButton{ width:200px; font-size: 18px; }")
            self.msg.setWindowTitle('No database Found')
            self.msg.exec_()

        
    #function to add item to tablewidget
    def add_item(self,item,number,price):
        row = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row+1)
        self.tableWidget.setItem(row,0,QTableWidgetItem(item))
        self.tableWidget.setItem(row,1,QTableWidgetItem("x"+number))
        self.tableWidget.setItem(row,2,QTableWidgetItem(price))

    #to read data from cart.txt, if no cart.txt found, return error
    def read_data(self):
        try:
            f = open("./cart.txt", "r") 
            lines = f.read().splitlines()
            return lines
        except:
            print("No database found")
            return "Error"

class See_Waiting_Time(QWidget):
    def __init__(self,parent=None):
        super(See_Waiting_Time,self).__init__(parent)
        self.setup_Ui()
        self.BlueButton.clicked.connect(lambda : self.calculate_waiting_time(self.textEdit.toPlainText()))
    def setup_Ui(self):
        self.setObjectName("Form")
        self.resize(800, 600)
        self.mainwidget = QtWidgets.QWidget(self)
        self.CartPay_BG = QtWidgets.QLabel(self)
        self.CartPay_BG.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.CartPay_BG.setPixmap(QtGui.QPixmap('./Pictures/northspine.jpg'))
        self.CartPay_BG.setScaledContents(True)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(50, 410, 141, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./Pictures/ntu_lion.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(240, 400, 551, 221))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./Pictures/paidui1.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(180, 40, 431, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(310, 150, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(190, 160, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(190, 230, 431, 71))
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(190, 190, 431, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_6.setFont(font)
        self.label_5.setObjectName("label_5")
        self.BlueButton = QtWidgets.QPushButton(self)
        self.BlueButton.setGeometry(QtCore.QRect(530, 130, 72, 72))
        self.BlueButton.setStyleSheet("#BlueButton {\n"
"    background-color: #303d5e;\n"
"    min-width: 72px;\n"
"    max-width: 72px;\n"
"    min-height: 72px;\n"
"    max-height: 72px;\n"
"    border-radius: 36px; \n"
"    color: #FFFFFF;\n"
"}\n"
"#BlueButton:hover {\n"
"    background-color: #516cb0;\n"
"}\n"
"#BlueButton:pressed {\n"
"    background-color: #04070f;\n"
"}")
        self.BlueButton.setObjectName("BlueButton")
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Enter the number of people in front of you"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.label_4.setText(_translate("Form", "Number:"))
        self.BlueButton.setText(_translate("Form", "Click"))

    def popup_message(self,textss):
        msg= QMessageBox(self.mainwidget)
        msg.setWindowTitle("Warning !!")
        _translate = QtCore.QCoreApplication.translate
        if textss==1:
            msg.setText(_translate("Form", "<html><p><span style=\" font-size:18pt; font-weight:700; color:#FA2C00;\">Only Numbers Allowed!!  <br />Please enter a valid integer number !</span></p></html>"))
        elif textss==2:
            msg.setText(_translate("Form", "<html><p><span style=\" font-size:18pt; font-weight:700; color:#FA2C00;\">Exceed the Range!! Too big!! <br />Please enter a valid integer number !</span></p></html>"))
        else:
            msg.setText(_translate("Form", "<html><p><span style=\" font-size:18pt; font-weight:700; color:#FA2C00;\">Exceed the Range!! No Negative Value!! <br />Please enter a valid integer number !</span></p></html>"))

        msg.setGeometry(QtCore.QRect(400,300 , 200, 400))
        x=msg.exec_()

    def calculate_waiting_time(self,input_text):
        _translate = QtCore.QCoreApplication.translate

        try:
            num_of_people = int(input_text)
            if num_of_people > 100:
                self.label_5.setText("Please enter a valid integer number")
                self.popup_message(textss=2)
            elif num_of_people < 0:
                self.label_5.setText("Please enter a valid integer number")
                self.popup_message(textss=0)
            else:
                self.label_6.setText("Your estimated waitting time is "+str(num_of_people*2)+" mins\n")
                self.label_5.setText(_translate("Form", "<html><p><span style=\" font-size:16pt; font-weight:600; color:#FA2C00;\">Thank You for Using! <br />Have A Nice Day!</span></p></html>"))

        except:
            self.label_5.setText("Only Numbers Allowed! \nPlease enter a valid integer number")
            self.popup_message(textss=1)

#Controller Class to control all the page interations
class Cart_Pay(QWidget):

    #Initialiaze the first page for class View_Menu_First_Page()
    def __init__(self,parent=None):
        super(Cart_Pay,self).__init__(parent)
        self.resize(800,600)
        self.stackedwidget = QStackedWidget(self)
        self.stackedwidget.setGeometry(QtCore.QRect(0,0 , 800, 600))
        self.stackedwidget.setObjectName("stackwidget")

        self.add_first_page()

    #function to show first page
    def add_first_page(self):
        self.first_page = Pay_First_Page()
        self.stackedwidget.addWidget(self.first_page)
        self.stackedwidget.setCurrentIndex(0)
        print(self.first_page.tableWidget.rowCount())
        self.first_page.BlueButton.clicked.connect(self.add_second_page) #only can use lambda: to make use of return value form functions

    #function to show second page
    def add_second_page(self):
        self.second_page = See_Waiting_Time()
        self.stackedwidget.addWidget(self.second_page)
        self.stackedwidget.setCurrentIndex(1)


if __name__ == '__main__':

    
    app =QtWidgets.QApplication(sys.argv)
    w = Cart_Pay()
    w.show()
    sys.exit(app.exec_())