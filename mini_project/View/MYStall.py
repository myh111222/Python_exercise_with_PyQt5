from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QWidget ,QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from datetime import datetime
import pytz
import time

class MalayStall(QtWidgets.QWidget):
	
	def __init__(self,parent=None):
		super(MalayStall,self).__init__(parent)
		self.setupUi()

	def setupUi(self):
		self.string = ''

		self.setObjectName("MalayStall")
		self.resize(800, 600)
		self.setMinimumSize(QtCore.QSize(800, 600))
		self.setMaximumSize(QtCore.QSize(800, 600))
		self.mainwidget = QtWidgets.QWidget(self)
		self.mainwidget.setMinimumSize(QtCore.QSize(800, 600))
		self.mainwidget.setObjectName("mainwidget")

		self.setAutoFillBackground(True)
		p = self.palette()
		p.setColor(self.backgroundRole(), QtCore.Qt.black)
		self.setPalette(p)
		self.gridLayout = QtWidgets.QGridLayout(self)
		self.gridLayout.setObjectName('gridLayout')

		now = QtCore.QDateTime.currentDateTime().toPyDateTime()
		print(now)



		#page 1 Malay
		MYMenuTuple = self.MYMenu(now)

		self.MYBG = QtWidgets.QLabel(self)
		self.MYBG.setGeometry(QtCore.QRect(0, 0, 800, 600))
		self.MYBG.setObjectName("MYBG")
		self.MYBG.setPixmap(QtGui.QPixmap('./Pictures/kfc/malaybackground2_4.jpg'))
		self.MYBG.setScaledContents(True)
		self.MYBG.setAlignment(QtCore.Qt.AlignCenter)

		self.spinBox_MY_0 = QtWidgets.QSpinBox(self)
		self.spinBox_MY_0.setGeometry(QtCore.QRect(117, 195, 42, 22))
		self.spinBox_MY_0.setFrame(False)
		self.spinBox_MY_0.setObjectName("spinBox_MY_0")

		self.spinBox_MY_1 = QtWidgets.QSpinBox(self)
		self.spinBox_MY_1.setGeometry(QtCore.QRect(380, 195, 42, 22))
		self.spinBox_MY_1.setAutoFillBackground(False)
		self.spinBox_MY_1.setWrapping(False)
		self.spinBox_MY_1.setFrame(False)
		self.spinBox_MY_1.setObjectName("spinBox_MY_1")

		self.spinBox_MY_2 = QtWidgets.QSpinBox(self)
		self.spinBox_MY_2.setGeometry(QtCore.QRect(380, 425, 42, 22))
		self.spinBox_MY_2.setFrame(False)
		self.spinBox_MY_2.setObjectName("spinBox_MY_2")

		self.spinBox_MY_3 = QtWidgets.QSpinBox(self)
		self.spinBox_MY_3.setGeometry(QtCore.QRect(110, 425,42, 22))
		self.spinBox_MY_3.setObjectName("spinBox_MY_3")

		self.spinBox_MY_4 = QtWidgets.QSpinBox(self)
		self.spinBox_MY_4.setGeometry(QtCore.QRect(640, 195, 42, 22))
		self.spinBox_MY_4.setObjectName("spinBox_MY_4")


		self.item0_price = QtWidgets.QLabel(self)
		self.item0_price.setGeometry(QtCore.QRect(80, 170, 114, 20))
		self.item0_price.setObjectName("item0_price")
		self.item0_price.setAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.item0_price.setFont(font)

		self.item1_price = QtWidgets.QLabel(self)
		self.item1_price.setGeometry(QtCore.QRect(340, 400, 114, 20))
		self.item1_price.setObjectName("item1_price")
		self.item1_price.setAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.item1_price.setFont(font)

		self.item2_price = QtWidgets.QLabel(self)
		self.item2_price.setGeometry(QtCore.QRect(70, 400, 114, 20))
		self.item2_price.setObjectName("item2_price")
		self.item2_price.setAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.item2_price.setFont(font)

		self.item3_price = QtWidgets.QLabel(self)
		self.item3_price.setGeometry(QtCore.QRect(340, 170, 114, 20))
		self.item3_price.setObjectName("item3_price")
		self.item3_price.setAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.item3_price.setFont(font)

		self.item4_price = QtWidgets.QLabel(self)
		self.item4_price.setGeometry(QtCore.QRect(600, 170, 114, 20))
		self.item4_price.setObjectName("item4_price")
		self.item4_price.setAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.item4_price.setFont(font)

		#self.MYBG = QtWidgets.QLabel(self)
		#self.MYBG.setGeometry(QtCore.QRect(4, -1, 701, 591))
		#self.MYBG.setObjectName("MYBG")

		self.item0_Pic = QtWidgets.QLabel(self)
		self.item0_Pic.setGeometry(QtCore.QRect(70, 55, 120, 100))
		self.item0_Pic.setObjectName("item0_Pic")
		self.item0_Pic.setPixmap(QtGui.QPixmap(MYMenuTuple[0][2]))
		self.item0_Pic.setScaledContents(True)
		self.item0_Pic.setAlignment(QtCore.Qt.AlignCenter)

		self.item1_Pic = QtWidgets.QLabel(self)
		self.item1_Pic.setGeometry(QtCore.QRect(340, 270, 130, 110))
		self.item1_Pic.setObjectName("item1_Pic")
		self.item1_Pic.setPixmap(QtGui.QPixmap(MYMenuTuple[1][2]))
		self.item1_Pic.setScaledContents(True)
		self.item1_Pic.setAlignment(QtCore.Qt.AlignCenter)

		self.item2_Pic = QtWidgets.QLabel(self)
		self.item2_Pic.setGeometry(QtCore.QRect(60, 270, 150, 120))
		self.item2_Pic.setObjectName("item2_Pic")
		self.item2_Pic.setPixmap(QtGui.QPixmap(MYMenuTuple[2][2]))
		self.item2_Pic.setScaledContents(True)
		self.item2_Pic.setAlignment(QtCore.Qt.AlignCenter)

		self.item3_Pic = QtWidgets.QLabel(self)
		self.item3_Pic.setGeometry(QtCore.QRect(330, 20, 147, 120))
		self.item3_Pic.setObjectName("item3_Pic")
		self.item3_Pic.setPixmap(QtGui.QPixmap(MYMenuTuple[3][2]))
		self.item3_Pic.setScaledContents(True)
		self.item3_Pic.setAlignment(QtCore.Qt.AlignCenter)


		self.item4_Pic = QtWidgets.QLabel(self)
		self.item4_Pic.setGeometry(QtCore.QRect(600, 40, 147, 110))
		self.item4_Pic.setObjectName("item4_Pic")
		self.item4_Pic.setPixmap(QtGui.QPixmap(MYMenuTuple[4][2]))
		self.item4_Pic.setScaledContents(True)
		self.item4_Pic.setAlignment(QtCore.Qt.AlignCenter)


		self.Checkout_MY = QtWidgets.QPushButton(self)
		self.Checkout_MY.setGeometry(QtCore.QRect(620, 470, 81, 31))
		self.Checkout_MY.setObjectName("Checkout_MY")
		font = QtGui.QFont()
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.Checkout_MY.setFont(font)
		self.Checkout_MY.setStyleSheet("#Checkout_MY {\n"
"    background-color: #F01C2F;\n"
"    color: #FFFFFF;\n"
"    /*minimum size*/\n"
"    min-width: 90px;\n"
"    max-width: 90px;\n"
"    min-height: 90px;\n"
"    max-height: 90px;\n"
"    border-radius: 45px; /*Round*/\n"
"}\n"
"#Checkout_MY:hover {\n"
"    background-color: #AF267E;\n"
"}\n"
"#Checkout_MY:pressed {\n"
"    background-color: #04070f;\n"
"}")

		self.Reset_MY = QtWidgets.QPushButton(self)
		self.Reset_MY.setGeometry(QtCore.QRect(490, 470, 81, 31))
		self.Reset_MY.setObjectName("Reset_MY")
		font = QtGui.QFont()
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.Reset_MY.setFont(font)
		self.Reset_MY.setStyleSheet("#Reset_MY {\n"
"    background-color: #F01C2F;\n"
"    color: #FFFFFF;\n"
"    /*minimum size*/\n"
"    min-width: 90px;\n"
"    max-width: 90px;\n"
"    min-height: 90px;\n"
"    max-height: 90px;\n"
"    border-radius: 45px; /*Round*/\n"
"}\n"
"#Reset_MY:hover {\n"
"    background-color: #AF267E;\n"
"}\n"
"#Reset_MY:pressed {\n"
"    background-color: #04070f;\n"
"}")
		self.OperationTime = QtWidgets.QPushButton(self)
		self.OperationTime.setGeometry(QtCore.QRect(360, 470, 81, 31))
		font = QtGui.QFont()
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.OperationTime.setFont(font)
		self.OperationTime.setObjectName("OperationTime")
		self.OperationTime.setStyleSheet("#OperationTime {\n"
"    background-color: #F01C2F;\n"
"    color: #FFFFFF;\n"
"    /*minimum size*/\n"
"    min-width: 90px;\n"
"    max-width: 90px;\n"
"    min-height: 90px;\n"
"    max-height: 90px;\n"
"    border-radius: 45px; /*Round*/\n"
"}\n"
"#OperationTime:hover {\n"
"    background-color: #AF267E;\n"
"}\n"
"#OperationTime:pressed {\n"
"    background-color: #04070f;\n"
"}")
		

		self.item0_Name = QtWidgets.QLabel(self)
		self.item0_Name.setGeometry(QtCore.QRect(80, 150, 114, 20))
		self.item0_Name.setObjectName("item0_Name")
		self.item0_Name.setAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.item0_Name.setFont(font)

		self.item1_Name = QtWidgets.QLabel(self)
		self.item1_Name.setGeometry(QtCore.QRect(340, 380, 114, 20))
		self.item1_Name.setObjectName("item1_Name")
		self.item1_Name.setAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.item1_Name.setFont(font)

		self.item2_Name = QtWidgets.QLabel(self)
		self.item2_Name.setGeometry(QtCore.QRect(70, 380, 114, 20))
		self.item2_Name.setObjectName("item2_Name")
		self.item2_Name.setAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.item2_Name.setFont(font)

		self.item3_Name = QtWidgets.QLabel(self)
		self.item3_Name.setGeometry(QtCore.QRect(340, 150, 114, 20))
		self.item3_Name.setObjectName("item3_Name")
		self.item3_Name.setAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.item3_Name.setFont(font)

		self.item4_Name = QtWidgets.QLabel(self)
		self.item4_Name.setGeometry(QtCore.QRect(600, 150,114, 20))
		self.item4_Name.setObjectName("item4_Name")
		self.item4_Name.setAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.item4_Name.setFont(font)


		self.operating_hour_text = QtWidgets.QLabel(self)
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.operating_hour_text.setFont(font)
		self.operating_hour_text.setAlignment(QtCore.Qt.AlignCenter)
		self.operating_hour_text.setGeometry(QtCore.QRect(450, 320, 350, 70))
		self.operating_hour_text.setObjectName("operating_hour_text")
		

		#self.MYBG.raise_()
		self.MYBG.raise_()
		self.spinBox_MY_0.raise_()
		self.spinBox_MY_1.raise_()
		self.spinBox_MY_2.raise_()
		self.spinBox_MY_3.raise_()
		self.spinBox_MY_4.raise_()
		self.item0_price.raise_()
		self.item1_price.raise_()
		self.item2_price.raise_()
		self.item3_price.raise_()
		self.item4_price.raise_()
		self.item0_Pic.raise_()
		self.item1_Pic.raise_()
		self.item2_Pic.raise_()
		self.item3_Pic.raise_()
		self.item4_Pic.raise_()
		self.Checkout_MY.raise_()
		self.Reset_MY.raise_()
		self.item0_Name.raise_()
		self.item1_Name.raise_()
		self.item2_Name.raise_()
		self.item3_Name.raise_()
		self.item4_Name.raise_()
		self.OperationTime.raise_()
		self.operating_hour_text.raise_()


		self.Reset_MY.clicked.connect(self.MY_clear_all)
		self.Checkout_MY.clicked.connect(self.MY_add_to_cart)


		
		
		
		#self.MYBG.raise_()


		#self.stackedWidget.addWidget(self.page)

		self.OperationTime.clicked.connect(self.ShowTime)
		
		self.retranslateUi(MYMenuTuple)



		#self.calendarWidget.clicked['QDate'].connect(self.dateTimeEdit.setDate)
		
		
		QtCore.QMetaObject.connectSlotsByName(self)


	def ShowTime(self):
		operating_hour_dic = {
			(0,1,2,3,4) : "10am - 10pm", #weekdays
			(5,6) : "11am - 12pm", #weekends
		}
		now = datetime.now()
		now_weekday = now.weekday() #get current time
		for key in operating_hour_dic:
			if now_weekday in key:
				self.operating_hour = operating_hour_dic[key] #get the operating hour from dic

		print(self.operating_hour)
		_translate = QtCore.QCoreApplication.translate
		self.setWindowTitle(_translate("MalayStall", "Malay Stall"))
		self.operating_hour_text.setText(_translate("MalayStall", "Operating Hours:\n"+self.operating_hour))


	def retranslateUi(self,MYMenuTuple):
		_translate = QtCore.QCoreApplication.translate
		self.setWindowTitle(_translate("MalayStall", "Malay Stall"))

		self.MYBG.setText(_translate("MalayStall", ""))
		
		self.item0_price.setText(_translate("MalayStall", MYMenuTuple[0][1]))
		self.item1_price.setText(_translate("MalayStall", MYMenuTuple[1][1]))
		self.item2_price.setText(_translate("MalayStall", MYMenuTuple[2][1]))
		self.item3_price.setText(_translate("MalayStall", MYMenuTuple[3][1]))
		self.item4_price.setText(_translate("MalayStall", MYMenuTuple[4][1]))
		#self.MYBG.setText(_translate("MalayStall", "MY Stall"))
		self.item0_Pic.setText(_translate("MalayStall", ''))
		self.item1_Pic.setText(_translate("MalayStall", ''))
		self.item2_Pic.setText(_translate("MalayStall", ''))
		self.item3_Pic.setText(_translate("MalayStall", ''))
		self.item4_Pic.setText(_translate("MalayStall", ''))
		self.Checkout_MY.setText(_translate("MalayStall", "Add To\nCart"))
		self.Reset_MY.setText(_translate("MalayStall", "Clear\nAll"))
		self.item0_Name.setText(_translate("MalayStall", MYMenuTuple[0][0]))
		self.item1_Name.setText(_translate("MalayStall", MYMenuTuple[1][0]))
		self.item2_Name.setText(_translate("MalayStall", MYMenuTuple[2][0]))
		self.item3_Name.setText(_translate("MalayStall", MYMenuTuple[3][0]))
		self.item4_Name.setText(_translate("MalayStall", MYMenuTuple[4][0]))
		self.OperationTime.setText(_translate('Subway','Opening\nHours'))
		#self.OpTime.setText(_translate('Subway','12AM-12PM'))
		#self.OkButton.setText(_translate("Subway",'Ok'))
		

	
	def MYMenu(self,current_time):
		EvenDayMenuTuple = ('Laksa','S$5','./Pictures/MalayFood/EvenDays/Laksa.png'),('Nasi Lemak','S$6','./Pictures/MalayFood/EvenDays/NasiLemak.png'),('Nasi Briyani','S$6','./Pictures/MalayFood/EvenDays/NasiBriyani.png'),('Mee Soto','S$5.5','./Pictures/MalayFood/EvenDays/MeeSoto.png'),('Nasi Kerabu','S$5.5','./Pictures/MalayFood/EvenDays/NasiKerabu.png')
		OddDayMenuTuple = ('Nasi Kerabu','S$5.5','./Pictures/MalayFood/EvenDays/NasiKerabu.png'),('Mee Siam','S$5.5','./Pictures/MalayFood/OddDays/MeeSiam.png'),('Rojak','S$4','./Pictures/MalayFood/OddDays/Rojak.png'),('Mee Rebus','S$6.5','./Pictures/MalayFood/OddDays/MeeRebus.png'),('Nasi Lemak','S$6','./Pictures/MalayFood/EvenDays/NasiLemak.png')
		Date = current_time.weekday() + 1
		if Date % 2 == 0:
			print('Even days menu')
			MenuTuple = EvenDayMenuTuple
		else:
			print('Odd days menu')
			MenuTuple = OddDayMenuTuple
		return MenuTuple



	def MY_clear_all(self):
		self.spinBox_MY_0.setValue(0)
		self.spinBox_MY_1.setValue(0)
		self.spinBox_MY_2.setValue(0)
		self.spinBox_MY_3.setValue(0)
		self.spinBox_MY_4.setValue(0)
		self.string = ''
		try:
			os.remove('./cart.txt')
		except:
			pass
	
	def MY_add_to_cart(self):
		item_lists = [
			[self.spinBox_MY_0,self.item0_price,self.item0_Name],
			[self.spinBox_MY_1,self.item1_price,self.item1_Name],
			[self.spinBox_MY_2,self.item2_price,self.item2_Name],
			[self.spinBox_MY_3,self.item3_price,self.item3_Name],
			[self.spinBox_MY_4,self.item4_price,self.item4_Name]
		]
		#define am empty dictionary
		dict_data={}
		with open('./cart.txt','w') as f:
			list1=[]
			for item_list in item_lists:
				print(item_list[0].value()) #for debugging
				if item_list[0].value() != 0:
					print('here')
					item_name = str(item_list[2].text())

					item_price_text = str(item_list[1].text())[2:]
					print(item_price_text)
					item_price = float(item_price_text)
					total_price = item_price*int(item_list[0].value())
					list1.append(item_name.replace(" ","_"))
					list1.append(str(item_list[0].value()))
					list1.append(str('{0:.2f}'.format(total_price)))
					#from selected time create and save dictionary for the cart and save it into variable data
					dict_data[item_lists.index(item_list)]=list1
					list1=[]
					print (dict_data) #for debugging
					self.string = self.string + item_name.replace(' ','_') + ' ' + str(item_list[0].value()) + ' ' +  str('{0:.2f}'.format(total_price)) + '\n' #format string and add together
			f.write(self.string) #write string to data base
			self.string=''	#clear string

        #Read dictionary for the cart and save it into variable call "dict_data"
		show_carted_item=""
		for x,y in dict_data.items():
			print (y[0],y[1],y[2])
			show_carted_item=show_carted_item+y[1]+" set of "+y[0]+" <br />"

		print (show_carted_item)

		#=================================================================================
		#pop window for adding cart
		#=================================================================================

		def popup_message(self,textss):
			popmsg= QMessageBox(self.mainwidget)
			popmsg.setWindowTitle("Adding to Cart")
			_translate = QtCore.QCoreApplication.translate
			if textss=="":
				popmsg.setText((_translate("Form", "<html><p><span style=\" font-size:12pt; font-weight:500; color:#AA2C00;\">No items in Cart!! <br />Please choose your food !</span></p></html>")))
			else:
				popmsg.setText(_translate("Form", "<html><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">You Have added to Cart: <br />  <br /> </span><span style=\" font-size:12pt; font-weight:400; color:#8E8E8E;\">{cart} </span></p></html>").format(cart=textss))
			popmsg.setGeometry(QtCore.QRect(400,300 , 200, 200))
			x=popmsg.exec_()

		popup_message(self,show_carted_item)
		time.sleep(0.1)

#####################################################
Stylesheet = '''

QLabel {
	color: white;
}

'''
##########################################################

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	app.setStyleSheet(Stylesheet)
	#Form = QtWidgets.QWidget()
	ui = MalayStall()
	#ui.setupUi(Form)
	ui.show()

	sys.exit(app.exec_())
