from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QWidget ,QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import datetime
import pytz
import time

class SubwayStall(QtWidgets.QWidget):
	
	def __init__(self,parent=None):
		super(SubwayStall,self).__init__(parent)
		self.setupUi()

	def setupUi(self):
		self.string = ''

		self.setObjectName("Subway")
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



		#page 1 Subway
		SubwayMenuTuple = self.SubwayMenu(now)
		print ("ahahaha")
		#self.page = QtWidgets.QWidget()
		#self.page.setObjectName("page")
		self.spinBox1 = QtWidgets.QSpinBox(self)
		self.spinBox1.setGeometry(QtCore.QRect(117, 195, 42, 22))
		self.spinBox1.setObjectName("spinBox1")

		self.spinBox2 = QtWidgets.QSpinBox(self)
		self.spinBox2.setGeometry(QtCore.QRect(380, 195, 42, 22))
		self.spinBox2.setObjectName("spinBox2")


		self.spinBox3 = QtWidgets.QSpinBox(self)
		self.spinBox3.setGeometry(QtCore.QRect(110, 425,42, 22))
		self.spinBox3.setObjectName("spinBox3")



		self.spinBox4 = QtWidgets.QSpinBox(self)
		self.spinBox4.setGeometry(QtCore.QRect(380, 425, 42, 22))
		self.spinBox4.setObjectName("spinBox4")

		self.spinBox5 = QtWidgets.QSpinBox(self)
		self.spinBox5.setGeometry(QtCore.QRect(640, 195, 42, 22))
		self.spinBox5.setObjectName("spinBox5")

		self.Item0Name = QtWidgets.QLabel(self)
		self.Item0Name.setGeometry(QtCore.QRect(80, 150, 114, 20))
		self.Item0Name.setObjectName("Item0Name")
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.Item0Name.setFont(font)
		self.Item0Name.setAlignment(QtCore.Qt.AlignCenter)
		self.Item1Name = QtWidgets.QLabel(self)
		self.Item1Name.setGeometry(QtCore.QRect(340, 150, 114, 20))
		self.Item1Name.setObjectName("Item1Name")
		self.Item1Name.setAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.Item1Name.setFont(font)
		self.Item2Name = QtWidgets.QLabel(self)
		self.Item2Name.setGeometry(QtCore.QRect(70, 380, 114, 20))
		self.Item2Name.setObjectName("Item2Name")
		self.Item2Name.setAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.Item2Name.setFont(font)
		self.Item3Name = QtWidgets.QLabel(self)
		self.Item3Name.setGeometry(QtCore.QRect(340, 380, 114, 20))
		self.Item3Name.setObjectName("Item3Name")
		self.Item3Name.setAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.Item3Name.setFont(font)
		self.Item4Name = QtWidgets.QLabel(self)
		self.Item4Name.setGeometry(QtCore.QRect(600, 150,114, 20))
		self.Item4Name.setObjectName("Item4Name")
		self.Item4Name.setAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.Item4Name.setFont(font)
		self.label_4 = QtWidgets.QLabel(self)
		self.label_4.setGeometry(QtCore.QRect(-86, -1, 131, 141))
		self.label_4.setObjectName("label_4")



		self.Item0Price = QtWidgets.QLabel(self)
		self.Item0Price.setGeometry(QtCore.QRect(80, 170, 114, 20))
		self.Item0Price.setObjectName("Item0Price")
		self.Item0Price.setAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.Item0Price.setFont(font)

		self.Item1Price = QtWidgets.QLabel(self)
		self.Item1Price.setGeometry(QtCore.QRect(340, 170, 114, 20))
		self.Item1Price.setObjectName("Item1Price")
		self.Item1Price.setAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.Item1Price.setFont(font)

		self.Item2Price = QtWidgets.QLabel(self)
		self.Item2Price.setAlignment(QtCore.Qt.AlignCenter)
		self.Item2Price.setGeometry(QtCore.QRect(70, 400, 114, 20))
		self.Item2Price.setObjectName("Item2Price")
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.Item2Price.setFont(font)

		self.Item3Price = QtWidgets.QLabel(self)
		self.Item3Price.setGeometry(QtCore.QRect(340, 400, 114, 20))
		self.Item3Price.setObjectName("Item3Price")
		self.Item3Price.setAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.Item3Price.setFont(font)

		self.Item4Price = QtWidgets.QLabel(self)
		self.Item4Price.setGeometry(QtCore.QRect(600, 170, 114, 20))
		self.Item4Price.setObjectName("Item4Price")
		self.Item4Price.setAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.Item4Price.setFont(font)

		self.SubwayBG = QtWidgets.QLabel(self)
		self.SubwayBG.setGeometry(QtCore.QRect(0, 0, 800, 600))
		self.SubwayBG.setObjectName("SubwayBG")
		self.SubwayBG.setPixmap(QtGui.QPixmap('./Pictures/kfc/subwayBG_4.jpg'))
		self.SubwayBG.setScaledContents(True)
		self.SubwayBG.setAlignment(QtCore.Qt.AlignCenter)

		self.Item0Pic = QtWidgets.QLabel(self)
		self.Item0Pic.setGeometry(QtCore.QRect(80, 70, 117, 70))
		self.Item0Pic.setObjectName("Item0Pic")
		self.Item0Pic.setPixmap(QtGui.QPixmap(SubwayMenuTuple[0][2]))
		self.Item0Pic.setScaledContents(True)
		self.Item0Pic.setAlignment(QtCore.Qt.AlignCenter)

		self.Item1Pic = QtWidgets.QLabel(self)
		self.Item1Pic.setGeometry(QtCore.QRect(340, 70, 117, 70))
		self.Item1Pic.setObjectName("Item1Pic")
		self.Item1Pic.setPixmap(QtGui.QPixmap(SubwayMenuTuple[1][2]))
		self.Item1Pic.setScaledContents(True)
		self.Item1Pic.setAlignment(QtCore.Qt.AlignCenter)

		self.Item2Pic = QtWidgets.QLabel(self)
		self.Item2Pic.setGeometry(QtCore.QRect(70, 300, 117, 70))
		self.Item2Pic.setObjectName("Item2Pic")
		self.Item2Pic.setPixmap(QtGui.QPixmap(SubwayMenuTuple[2][2]))
		self.Item2Pic.setScaledContents(True)
		self.Item2Pic.setAlignment(QtCore.Qt.AlignCenter)

		self.Item3Pic = QtWidgets.QLabel(self)
		self.Item3Pic.setGeometry(QtCore.QRect(340, 300, 117, 70))
		self.Item3Pic.setPixmap(QtGui.QPixmap(SubwayMenuTuple[3][2]))
		self.Item3Pic.setScaledContents(True)
		self.Item3Pic.setObjectName("Item3Pic")
		self.Item3Pic.setAlignment(QtCore.Qt.AlignCenter)

		self.Item4Pic = QtWidgets.QLabel(self)
		self.Item4Pic.setGeometry(QtCore.QRect(600, 70, 117, 70))
		self.Item4Pic.setObjectName("Item4Pic")
		self.Item4Pic.setPixmap(QtGui.QPixmap(SubwayMenuTuple[4][2]))
		self.Item4Pic.setScaledContents(True)
		self.Item4Pic.setAlignment(QtCore.Qt.AlignCenter)

		

		self.Checkout_S = QtWidgets.QPushButton(self)
		self.Checkout_S.setGeometry(QtCore.QRect(620, 470, 81, 31))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Checkout_S.sizePolicy().hasHeightForWidth())
		self.Checkout_S.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.Checkout_S.setFont(font)
		self.Checkout_S.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.Checkout_S.setAutoFillBackground(True)
		self.Checkout_S.setAutoDefault(False)
		self.Checkout_S.setDefault(False)
		self.Checkout_S.setFlat(False)
		self.Checkout_S.setObjectName("Checkout_S")

		self.Checkout_S.setStyleSheet("#Checkout_S {\n"
"    background-color: #F01C2F;\n"
"    color: #FFFFFF;\n"
"    /*minimum size*/\n"
"    min-width: 90px;\n"
"    max-width: 90px;\n"
"    min-height: 90px;\n"
"    max-height: 90px;\n"
"    border-radius: 45px; /*Round*/\n"
"}\n"
"#Checkout_S:hover {\n"
"    background-color: #AF267E;\n"
"}\n"
"#Checkout_S:pressed {\n"
"    background-color: #04070f;\n"
"}")

		self.Reset_S = QtWidgets.QPushButton(self)
		self.Reset_S.setGeometry(QtCore.QRect(490, 470, 81, 31))
		self.Reset_S.setObjectName("Reset_S")
		font = QtGui.QFont()
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.Reset_S.setFont(font)
		self.Reset_S.setStyleSheet("#Reset_S {\n"
"    background-color: #F01C2F;\n"
"    color: #FFFFFF;\n"
"    /*minimum size*/\n"
"    min-width: 90px;\n"
"    max-width: 90px;\n"
"    min-height: 90px;\n"
"    max-height: 90px;\n"
"    border-radius: 45px; /*Round*/\n"
"}\n"
"#Reset_S:hover {\n"
"    background-color: #AF267E;\n"
"}\n"
"#Reset_S:pressed {\n"
"    background-color: #04070f;\n"
"}")


		self.OperationTime = QtWidgets.QPushButton(self)
		self.OperationTime.setGeometry(QtCore.QRect(360, 470, 81, 31))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.OperationTime.sizePolicy().hasHeightForWidth())
		self.OperationTime.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.OperationTime.setFont(font)
		self.OperationTime.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.OperationTime.setAutoFillBackground(True)
		self.OperationTime.setAutoDefault(False)
		self.OperationTime.setDefault(False)
		self.OperationTime.setFlat(False)
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

		
		
		
		self.SubwayBG.raise_()
		self.spinBox1.raise_()
		self.spinBox2.raise_()
		self.spinBox3.raise_()
		self.spinBox4.raise_()
		self.spinBox5.raise_()

		self.Item0Price.raise_()
		self.Item1Price.raise_()
		self.Item2Price.raise_()
		self.Item3Price.raise_()
		self.Item4Price.raise_()
		self.Item0Pic.raise_()
		self.Item1Pic.raise_()
		self.Item2Pic.raise_()
		self.Item3Pic.raise_()
		self.Item4Pic.raise_()
		self.Checkout_S.raise_()
		self.Reset_S.raise_()
		self.Item0Name.raise_()
		self.Item1Name.raise_()
		self.Item2Name.raise_()
		self.Item3Name.raise_()
		self.Item4Name.raise_()
		self.label_4.raise_()
		self.OperationTime.raise_()
		self.Checkout_S.clicked.connect(self.Subway_add_to_cart)
		self.Reset_S.clicked.connect(self.Subway_clear_all)
		self.OperationTime.clicked.connect(self.ShowTime)

		self.retranslateUi(SubwayMenuTuple)

		
		QtCore.QMetaObject.connectSlotsByName(self)


	#Store operation hour information in a dictionary. Show the operation hour according to current date
	def ShowTime(self):
		operating_hour_dic = {
			(0,1,2,3,4) : "8am - 12pm", #weekdays
			(5,6) : "11am - 12pm", #weekends
		}
		now = datetime.datetime.now() 
		now_weekday = now.weekday() #get current time
		for key in operating_hour_dic:
			if now_weekday in key:
				self.operating_hour = operating_hour_dic[key] #get the operating hour from dic

		print(self.operating_hour)
		_translate = QtCore.QCoreApplication.translate
		self.setWindowTitle(_translate("Subway", "Form"))
		self.operating_hour_text.setText(_translate("Subway", "Operating Hours:\n"+self.operating_hour))
	

	def retranslateUi(self,SubwayMenuTuple):
		_translate = QtCore.QCoreApplication.translate
		self.setWindowTitle(_translate("Subway", "Form"))
		
		self.Item0Price.setText(_translate("Subway", SubwayMenuTuple[0][1]))
		self.Item1Price.setText(_translate("Subway", SubwayMenuTuple[1][1]))
		self.Item2Price.setText(_translate("Subway", SubwayMenuTuple[2][1]))
		self.Item3Price.setText(_translate("Subway", SubwayMenuTuple[3][1]))
		self.Item4Price.setText(_translate("Subway", SubwayMenuTuple[4][1]))
		self.SubwayBG.setText(_translate("Subway", ""))
		self.Item0Pic.setText(_translate("Subway", ""))
		self.Item1Pic.setText(_translate("Subway", ""))
		self.Item2Pic.setText(_translate("Subway", ""))
		self.Item3Pic.setText(_translate("Subway", ""))
		self.Item4Pic.setText(_translate("Subway", ""))
		self.Checkout_S.setText(_translate("Subway", "Add To\nCart"))
		self.Reset_S.setText(_translate("Subway", "Clear\nAll"))
		self.OperationTime.setText(_translate('Subway','Opening\nHours'))


		self.operating_hour_text = QtWidgets.QLabel(self)
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.operating_hour_text.setFont(font)
		self.operating_hour_text.setAlignment(QtCore.Qt.AlignCenter)
		self.operating_hour_text.setGeometry(QtCore.QRect(450, 320, 350, 70))
		self.operating_hour_text.setObjectName("operating_hour_text")
		self.operating_hour_text.raise_()


		self.Item0Name.setText(_translate("Subway", SubwayMenuTuple[0][0]))
		self.Item1Name.setText(_translate("Subway", SubwayMenuTuple[1][0]))
		self.Item2Name.setText(_translate("Subway", SubwayMenuTuple[2][0]))
		self.Item3Name.setText(_translate("Subway", SubwayMenuTuple[3][0]))
		self.Item4Name.setText(_translate("Subway", SubwayMenuTuple[4][0]))
		self.label_4.setText(_translate("Subway", "TextLabel"))

	#Store menu into a tuple, return menu according to current data and time		
	def SubwayMenu(self,current_time):
		print ("hehe")
		BreakfastTuple = ('Egg & Cheese','S$6.8','./Pictures/Subway/EggCheese.png'),('Chicken Bacon','S$7.5','./Pictures/Subway/ChickenBacon.png'),('Chicken Ham','S$5.6','./Pictures/Subway/ChickenHam.png'),('Chicken Sausage','S$6.9','./Pictures/Subway/ChickenSausage.png'),('Subway Melt','S$5.6','./Pictures/Subway/SubwayMelt.png')
		LunchTuple = ('Chicken Tariyaki','S$7.9','./Pictures/Subway/ChickenTeriyaki.png'),('Roast Beef','S$10.5','./Pictures/Subway/RoastBeef.png'),('Egg Mayo','S$5.6','./Pictures/Subway/EggMayo.png'),('Veggie Delite','S$5.9','./Pictures/Subway/VeggieDelite.png'),('Turkey','S$5.6','./Pictures/Subway/Turkey.png')
		if current_time.hour < 11:
			MenuTuple = BreakfastTuple
		else:
			MenuTuple = LunchTuple
		return MenuTuple

	#Reset all the values in the spinbox
	def Subway_clear_all(self):
		self.spinBox1.setValue(0)
		self.spinBox2.setValue(0)
		self.spinBox3.setValue(0)


		self.spinBox4.setValue(0)
		self.spinBox5.setValue(0)
		self.string = ''
		try:
			os.remove('./cart.txt')
		except:
			pass
	
	def Subway_add_to_cart(self):
		item_lists = [
			[self.spinBox1,self.Item0Price,self.Item0Name],
			[self.spinBox2,self.Item1Price,self.Item1Name],
			[self.spinBox3,self.Item2Price,self.Item2Name],
			[self.spinBox4,self.Item3Price,self.Item3Name],
			[self.spinBox5,self.Item4Price,self.Item4Name]
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
	ui = SubwayStall()
	#ui.setupUi(Form)
	ui.show()

	sys.exit(app.exec_())
