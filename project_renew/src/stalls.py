# -*- coding: utf-8 -*-
#
# WARNING! All changes made in this file will be lost!
import sqlite3
import sys
import time
import re
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import QtCore, QtWidgets
from Functional import sql
from Functional import Component as cpn
from data import menu_data
CONN_PAYCART = sql.conn_PayCart()
sys.path.append('..')



#set stylesheet for buttons in stall menu
style1 = {"size":15, 'bold':True, 'weight':100, 'colorbgd':'#FFC300', 'colorpress':'#AF267E', 'colorhover':'#04070f', 'w':'110', 'h':'90'}
totalitems = cpn.totalitems
startcoords = (60, 40)
itemInARow = 4
Xincreasement = 190
Yincreasement = 180
c = CONN_PAYCART.cursor()

#==========================================================================================================

class stalls_window(QWidget):

	def __init__(self, stalll, parent=None):
		super(stalls_window, self).__init__(parent)
		#setup widget
		self.setMinimumSize(cpn.WidgetSize)
		self.setMaximumSize(cpn.WidgetSize)
		self.mainwidget = QtWidgets.QWidget(self)
		self.mainwidget.setMinimumSize(cpn.WidgetSize)
		self.mainwidget.setObjectName(stalll['PageName'])
		self.items = {}
		self.count = 0

		#load functions
		#new background function
		cpn.Set_Background(self.mainwidget, stalll['backGround'])
		self.stalls_menu(stalll)

		#create 3 buttons, read button attribute from menu_data
		cpn.buttonFullStyle(self.mainwidget, None, **menu_data.buttons['OHButton'])
		cpn.buttonFullStyle(self.mainwidget, None, **menu_data.buttons['ClearButton'])
		cpn.buttonFullStyle(self.mainwidget, None, **menu_data.buttons['AddToCart'])
		cpn.button['ClearButton'].clicked.connect(self.clear_all)
		cpn.button['AddToCart'].clicked.connect(self.AddToChar)

		self.showOH()



	#this function contains Icon, price, name, could be reused in other file
	def StallIcoPriName(self, dish, OdNum=True):

		ItemIndex = self.count
		# calculation for how many arrangement of menu in a row
		self.Xstartcoords = startcoords[0] + (ItemIndex %  itemInARow) * Xincreasement
		self.Ystartcoords = startcoords[1] + (ItemIndex // itemInARow) * Yincreasement

		# icons
		# check for value type of logo if BOLD or string
		self.stalls_icon = QtWidgets.QLabel(self.mainwidget)
		self.stalls_icon.setPixmap(QPixmap(dish['logo']))
		self.stalls_icon.setScaledContents(True)
		self.stalls_icon.setGeometry(self.Xstartcoords, self.Ystartcoords, 111, 101)

		# this is not working yet
#		elif (type(dish['logo']) == bytes):
#			self.stalls_icon = QtWidgets.QLabel(self.mainwidget)
#			self.stalls_icon.setPixmap(QPixmap.loadFromData(dish['logo'], 'png'))
#			self.stalls_icon.setScaledContents(True)
#			self.stalls_icon.setGeometry(self.Xstartcoords, self.Ystartcoords, 111, 101)

		#price
		self.stalls_pric = QtWidgets.QLabel(self.mainwidget)
		self.stalls_pric.setGeometry(self.Xstartcoords + 30, self.Ystartcoords + 100, 91, 31)
		self.stalls_pric.setText("$"+str(dish['price']))

		#stallName
		self.stalls_name = QtWidgets.QLabel(self.mainwidget)
		self.stalls_name.setGeometry(self.Xstartcoords + 30, self.Ystartcoords + 85, 91, 31)
		self.stalls_name.setText(dish['itemName'])

		#numbers bar
		#previously use globals() to retrive string data from dictionary to set as variable name
		if (OdNum == True):
			self.items[dish['itemName']] = QtWidgets.QSpinBox(self.mainwidget)
			self.items[dish['itemName']].setValue(0)
			self.items[dish['itemName']].setGeometry(self.Xstartcoords + 30, self.Ystartcoords+125, 45, 23)
		#increasement of the itemindex
		self.count = self.count + 1


	#it is to load Icon, price, name, numberbar
	def stalls_menu(self, stalll):

		for dish in stalll['stallMenu']:
			#call
			self.StallIcoPriName(dish)
		self.count = 0
		totalitems.update(self.items)




	#clear function
	def clear_all(self):
		for i in self.items:
			print(i)
			self.items[i].setValue(0)
		c.execute("DELETE FROM PayCart")
		print('clear alllll')
		


	#showOH function
	def showOH(self):
		cpn.setlable(self.mainwidget, 'showOH', (40, 380, 210, 200), './Pictures/operationhour.jpeg', True)
		cpn.lable['showOH'].hide()
		cpn.button['OHButton'].pressed.connect(cpn.lable['showOH'].show)
		cpn.button['OHButton'].released.connect(cpn.lable['showOH'].hide)
		#QtWidgets.QLabel.setVisible


	def popup_message(self, textss):
		popmsg= QMessageBox(self.mainwidget)
		popmsg.setWindowTitle("Adding to Cart")
		popmsg.setFont(cpn.font['general'])
		if textss == "":
			popmsg.setText("No items in Cart!! \nPlease choose your food !")
		else:
			popmsg.setText(("You Have added to Cart: \n{}").format(self.print_cart(textss)))
		popmsg.setGeometry(QtCore.QRect(400, 300 , 200, 200))
		popmsg.exec_()


	def print_cart(self, cart):
		output = ""
		for item in cart:
			strr = str(item[0]) + "   " + str(item[1]) + "   " + str(item[2]) +' \n'
			output += strr
		print (output)
		return  output
		


	#AddToChar function
	def AddToChar(self):
		with open('./data/cart.txt', 'w') as fread:
			print("self.items========================")
			print(self.items)
			for stall in menu_data.stall_list:
				for dish in stall['stallMenu']:
					#TheDish=menu_data.stall_list[stall]['stallMenu'][dish]
					#print (dish['itemName'])
					if (totalitems[dish['itemName']].value() != 0):
					#print (dish['itemName'])
						fread.write(dish['itemName'] + "  " + str(dish['price']) + "  " + str(totalitems[dish['itemName']].value()) +"\n")
						#using sql, add cart to database
						sql.add_item(sql.PayCart(dish['itemName'], totalitems[dish['itemName']].value(), dish['price']))

			c.execute("SELECT * FROM PayCart WHERE quantity != 0")
			print("SQL Data ")
			cartlist=[]
			cartlist.extend(c.fetchall())
			print(cartlist)
			CONN_PAYCART.commit()
		self.popup_message(cartlist)
		print("AddToChar")
		time.sleep(0.2)

