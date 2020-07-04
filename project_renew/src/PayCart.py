import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QStackedWidget, QHeaderView, QFrame, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from Functional import Component as cpn


_translate = QtCore.QCoreApplication.translate
buttons = {}
styleblue = {"size":15, 'bold':True, 'weight':65, 'colorbgd':'#A03d5e', 'colorpress':'#04070f', 'colorhover':'#516cb0', 'w':'96', 'h':'105'}
cpn.setfont('waiting', 14, 75, True)
Afont = QFont("Arial", 16, 75, QFont.Bold)
Bfont = QFont("Arial", 16, 75, QFont.Bold)
Hfont = QFont("Arial", 22, 90, QFont.Bold)



class Pay_First_Page(QWidget):
	#initialize
	def __init__(self, parent=None):
		super(Pay_First_Page, self).__init__(parent)
		self.setup_Ui()
		#self.loaddatabut.clicked.connect(self.load_data) #to load data from cart.txt

	def setup_Ui(self):
		self.setObjectName("Pay_First_Page")
		#self.CartTaleb()
		#set a stall background
		cpn.Set_Background(self, "./Pictures/northspine.jpg")

		self.label = QtWidgets.QLabel(self)
		self.label.setGeometry(QtCore.QRect(20, 90, 331, 321))
		self.label.setPixmap(QtGui.QPixmap("./Pictures/NTU.jpg"))
		self.label.setScaledContents(True)

		cpn.setfont('Cartpay', 16, 75, True)
		self.label_2 = QtWidgets.QLabel(self)
		self.label_2.setGeometry(QtCore.QRect(240, 30, 350, 51))
		self.label_2.setFont(cpn.font['Cartpay'])
		self.label_2.setAlignment(QtCore.Qt.AlignCenter)


		cpn.newbuttonfunction(self, "Paybut", (30, 430, 96, 96), "Pay", None, **styleblue)
		cpn.button['Paybut'].hide()
		cpn.newbuttonfunction(self, "loadbut", (240, 430, 96, 96), "Load \nData", self.load_data, **styleblue)

		self.label_2.setText(_translate("Cart_and_Pay", "<html><p><span style=\" font-size:26pt; font-weight:700; font-style:italic; color:#fcbf3e;\">Pay Your Bill Here<br /> </span></p></html>"))
		self.CartTaleb()

	def CartTaleb(self):
		cpn.setfont('table', 12, 75, True)
		self.tableWidget = QtWidgets.QTableWidget(self)
		self.tableWidget.setGeometry(QtCore.QRect(400, 90, 341, 421))
		self.tableWidget.setColumnCount(0)
		self.tableWidget.setRowCount(0)
		self.tableWidget.horizontalHeader().setFont(cpn.font['table'])
		self.tableWidget.setFrameShape(QFrame.NoFrame)
		self.tableWidget.setColumnCount(3)
		self.tableWidget.setHorizontalHeaderLabels(['Items', 'Numbers', 'Price'])
		self.tableWidget.horizontalHeader().setFixedHeight(50)
		self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

	#functions to load data
	def load_data(self):
		data = self.read_data()
		self.tableWidget.setRowCount(0)
		self.tableWidget.clear()
		if data != "Error":
			total_price = 0.0
			for row_data_set in data:
				single_data = row_data_set.split() #split data from the data set
				self.add_item(single_data[0], single_data[1], single_data[2])
				total_price = total_price + float(single_data[2])
			row = self.tableWidget.rowCount()
			self.tableWidget.setRowCount(row + 1)
			self.tableWidget.setItem(row, 0, QTableWidgetItem("Total:"))
			self.tableWidget.setItem(row, 2, QTableWidgetItem(str(total_price)[0:5]))
			cpn.button['Paybut'].show()
			#cpn.button['loadbut'].hide()
		else:
			self.msg = QMessageBox(self) #if no data found, exit the app
			#self.msg.setIcon(QMessageBox.Information)
			#self.msg.setText("asd")
			self.msg.setStyleSheet("QLabel{min-width:200 px; font-size: 24px;} QPushButton{ width:200px; font-size: 18px; }")
			self.msg.setWindowTitle('No database Found')
			self.msg.exec_()


	#function to add item to tablewidget
	def add_item(self, item, number, price):
		row = self.tableWidget.rowCount()
		self.tableWidget.setRowCount(row+1)
		self.tableWidget.setItem(row, 0, QTableWidgetItem(item))
		self.tableWidget.setItem(row, 1, QTableWidgetItem("x" + number))
		self.tableWidget.setItem(row, 2, QTableWidgetItem(price))

	#to read data from cart.txt, if no cart.txt found, return error
	def read_data(self):
		try:
			f = open("./data/cart.txt", "r")
			lines = f.read().splitlines()
			return lines
		except:
			print("No database found")
			return "Error"

class See_Waiting_Time(QWidget):
	def __init__(self, parent=None):
		super(See_Waiting_Time, self).__init__(parent)
		self.setup_Ui()
		cpn.button['Blueclik'].clicked.connect(lambda: self.calculate_waiting_time(cpn.txtbox['Qnumb'].text()))
		#self.BlueButton.clicked.connect(lambda : self.calculate_waiting_time(self.textEdit.toPlainText()))

	def setup_Ui(self):
		self.setObjectName("Form")
		self.mainwidget = QtWidgets.QWidget(self)
		self.CartPay_BG = QtWidgets.QLabel(self)
		self.CartPay_BG.setGeometry(cpn.geometrysize)
		self.CartPay_BG.setPixmap(QtGui.QPixmap('./Pictures/northspine.jpg'))
		self.CartPay_BG.setScaledContents(True)

		#create lables
		cpn.setlable(self, 'ntulion', (50, 410, 141, 171), "./Pictures/ntu_lion.png", True)
		cpn.setlable(self, 'queue', (240, 400, 551, 221), "./Pictures/paidui1.png", True)

		#creat txt lables
		cpn.settext(self, 'QHead', Hfont, (100, 40, 631, 81), cpn.setcolor("Enter the number of people in front of you", '#FF1144'))
		cpn.settext(self, 'num', Afont, (180, 150, 121, 20), cpn.setcolor("Number: ", '#630030'))

		#create text box
		cpn.setTXbox(self, 'Qnumb', (310, 150, 195, 31), ' ')



		#create lables
		self.label_5 = QtWidgets.QLabel(self)
		self.label_5.setGeometry(QtCore.QRect(190, 270, 431, 71))
		self.label_6 = QtWidgets.QLabel(self)
		self.label_6.setGeometry(QtCore.QRect(190, 230, 431, 71))
		self.label_5.setFont(Bfont)
		self.label_6.setFont(Bfont)

		#create a click button
		cpn.newbuttonfunction(self,"Blueclik", (530, 130, 72, 72), "Click", None, **styleblue)

		self.setWindowTitle(_translate("Form", "Form"))

		'''
		self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" >\n"
										"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
										"p, li { white-space: pre-wrap; }\n"
										"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
										"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
		'''

	def popup_message(self, textss):
		msg = QMessageBox(self.mainwidget)
		msg.setFont(Hfont)
		msg.setWindowTitle("Warning !!")
		if textss == 1:
			msg.setText(cpn.setcolor("Only Numbers Allowed!!   <br />Please enter a valid integer number !", '#582255'))
		elif textss == 2:
			msg.setText(cpn.setcolor(" Exceed the Range!! Too big!!  <br />Please enter a valid integer number !", '#B85255'))
		else:
			msg.setText(cpn.setcolor("Exceed the Range!! No Negative Value!!  <br />Please enter a valid integer number !", '#881193'))

		msg.setGeometry(QtCore.QRect(400, 300, 200, 400))
		x = msg.exec_()

	def calculate_waiting_time(self, input_text):

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
				self.label_5.setText(cpn.setcolor("Thank You for Using! <br />Have A Nice Day!",'#FA2C00'))
		except:
			self.label_5.setText(cpn.setcolor("Only Numbers Allowed!  <br /> Please enter a valid integer number", '#DD5555'))
			self.popup_message(textss=1)

#Controller Class to control all the page interations
class Cart_Pay(QWidget):

	#Initialiaze the first page for class View_Menu_First_Page()
	def __init__(self, parent=None):
		super(Cart_Pay, self).__init__(parent)
		self.stackedwidget = QStackedWidget(self)
		self.stackedwidget.setGeometry(cpn.geometrysize)
		self.stackedwidget.setObjectName("stackwidget")
		self.add_first_page()

	#function to show first page
	def add_first_page(self):
		self.first_page = Pay_First_Page()
		self.stackedwidget.addWidget(self.first_page)
		self.stackedwidget.setCurrentIndex(0)
		print(self.first_page.tableWidget.rowCount())
		cpn.button['Paybut'].clicked.connect(self.add_second_page) #only can use lambda: to make use of return value form functions

	#function to show second page
	def add_second_page(self):
		self.second_page = See_Waiting_Time()
		self.stackedwidget.addWidget(self.second_page)
		self.stackedwidget.setCurrentIndex(1)


if __name__ == '__main__':

	
	app = QtWidgets.QApplication(sys.argv)
	w = Cart_Pay()
	w.show()
	sys.exit(app.exec_())