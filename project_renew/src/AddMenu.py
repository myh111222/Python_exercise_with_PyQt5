# -*- coding: utf-8 -*-
#
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtWidgets
from Functional import Component as cpn
from Functional import sql
from data import menu_data

startcoords1 = (60, 40)

# declare variables

#conn = sqlite3.connect('./data/PayCart.db')
#c = conn.cursor()
#c.execute("""CREATE TABLE PayCart (itemName TEXT,quantity INTERGER,unitprice REAL)""")



# ==========================================================================================================


class AddMenu(QWidget):

	def __init__(self, parent=None):
		super(AddMenu, self).__init__(parent)
		#setup widget
		self.centralWidget = QtWidgets.QWidget(self)
		self.AddMenu = QtWidgets.QWidget(self.centralWidget)
		self.AddMenu.setGeometry(cpn.geometrysize)
		self.items = {}
		self.AddtoMenu()

	#function to setup buttons and text box
	def menus(self):
		# setup text box and text lables
		for index, i in enumerate(menu_data.menuKeys):
			verIncrease = 60
			cpn.settext(self, i, cpn.Gefont, (80, 130 + index * verIncrease, 171, 31), "<font color=%s>%s</font>" %('#5F2F2D', i))
			cpn.setTXbox(self, i, (220, 130 + index * verIncrease, 251, 41), "Enter here")



	def AddtoMenu(self):

		## page set up
		self.menus()

		## setup background
		cpn.Set_Background(self.centralWidget, "./Pictures/restaurant-menu-background.jpg")

		## lock stall Name by check box
		cpn.txtbox['Stall Name'].setDisabled(True)

		## check box
		self.checkBox = QtWidgets.QCheckBox(self)
		self.checkBox.setGeometry(QtCore.QRect(530, 310, 85, 21))
		self.checkBox.setChecked(True)
		self.checkBox.toggled.connect(cpn.txtbox['Stall Name'].setDisabled)

		## new txt lable
		cpn.settext(self, 'checkBox', cpn.Gefont, (550, 310, 85, 21), "<font color=%s>%s</font>" %('#5F2F2D', "LOCK"))

		## new buttons
		cpn.newbuttonfunction(self, 'submit', (610, 340, 121, 70), "Submit\nTo Menu", None, **cpn.style2)
		cpn.newbuttonfunction(self, 'Browse', (500, 340, 121, 70), "Browse\nImage", self.getImage, **cpn.style2)
		self.submit_function

		## new label title
		self.labeltitle = QtWidgets.QLabel(self)
		self.labeltitle.setGeometry(QtCore.QRect(210, 20, 300, 90))
		self.labeltitle.setFont(QFont("Arial", 30, QFont.Bold))
		self.labeltitle.setText("<font color=%s>%s</font>" %('#5F2F2D', "ADD TO MENU"))

		## set image lables for selected dish
		self.label = QtWidgets.QLabel(self)
		self.label.setGeometry(QtCore.QRect(500, 160, 140, 120))


	def submit_function(self):
		try:
			cpn.button['submit'].clicked.connect(self.addtoDB)
		except:
			print("failed to add to DB")


	#This function performs add to DB
	def addtoDB(self):
		lista = []
		#checkings:
		txt_0 = cpn.txtbox["Stall Name"].text() not in sql.Input_stallData.getStall(self)
		txt_1 = cpn.txtbox["Item Name"].text() is None
		txt_2 = cpn.txtbox["Logo"].text() is None
		txt_3 = cpn.txtbox["Price"].text().isdigit()
		txt_4 = cpn.txtbox["Meal Type"].text() not in ['lunch', 'breakfirst'] 
		txt_5 = cpn.txtbox["Order Num"].text().isdigit()
		#pass checkings
		if (txt_0 or txt_1 or txt_2 or not txt_3 or txt_4 or not txt_5):
			print("Please give correct stall Name, item Name, price, orderNumber, and MenuType (lunch/breakfirst) ")
			print(" ")
			#print (sql.Input_stallData.getStall(self))
			#print (lista)
		else :
			print ("add menu in progress")
			#count = 0
			for index in enumerate(menu_data.menuKeys) :
				
				lista.append(self.items['txt_'+str(index)].text())
			print(lista)
			newdish = sql.Input_menuData(lista[0], lista[1], lista[2], int(lista[3]), lista[4], int(lista[5]))
			newdish.add_dish_DB()


	def getImage(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file',
											'./', "Image files (*)")
		self.imagePath = fname[0]
		print (self.imagePath)
		cpn.txtbox["Logo"].setText(str(self.imagePath))
		pixmap = QPixmap(self.imagePath)
		self.displayImageChose(QPixmap(pixmap))
		#self.resize(pixmap.width(), pixmap.height())

	# To display the select lmenu logo 
	def displayImageChose(self,images):

		self.label.setPixmap(images)
		self.label.setScaledContents(True)


	#this use bold data, not working yet
	def displayImageData(self, images):
		self.label.setPixmap(QPixmap.loadFromData(images, 'png'))
		self.label.setScaledContents(True)

