# -*- coding: utf-8 -*-
#
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from Functional import Component as cpn
from Functional import sql
from data import menu_data
import Main_page

startcoords1 = (60, 40)



class DeleteMenu(QWidget):

	def __init__(self, parent=None):
		super(DeleteMenu, self).__init__(parent)
		#setup widget
		self.centralWidget = QtWidgets.QWidget(self)
		self.DeletMenu = QtWidgets.QWidget(self.centralWidget)
		self.DeletMenu.setGeometry(cpn.geometrysize)
		cpn.Set_Background(self, "./Pictures/restaurant-menu-background.jpg")
		self.items = {}
		self.DetMenu()

	#page set up
	def DetMenu(self):

		Gfont = cpn.font['general']
		cpn.settext(self, 'StN', Gfont, (80, 300, 171, 31), "<font color=%s>%s</font>" %('#5F2F2D', "Stall Name"))
		cpn.settext(self, 'ItN', Gfont, (80, 360, 171, 31), "<font color=%s>%s</font>" %('#5F2F2D', "Item Name"))
		cpn.setTXbox(self, 'txt_S', (220, 300, 251, 41), "Enter here")
		cpn.setTXbox(self, 'txt_I', (220, 360, 251, 41), "Enter here")

		#lock stall Name
		cpn.txtbox['txt_S'].setDisabled(True)
		self.checkBox = QtWidgets.QCheckBox(self)
		self.checkBox.setGeometry(QtCore.QRect(530, 310, 85, 21))
		self.checkBox.setChecked(True)
		self.checkBox.toggled.connect(cpn.txtbox['txt_S'].setDisabled)

		self.checkBox_balel = QtWidgets.QLabel(self)
		self.checkBox_balel.setGeometry(QtCore.QRect(550, 310, 85, 21))
		self.checkBox_balel.setFont(QFont("Arial", 13, QFont.Bold))
		self.checkBox_balel.setText("<font color=%s>%s</font>" %('#5F2F2D', "LOCK"))

		self.pushButton = QtWidgets.QPushButton(self)
		self.pushButton.setGeometry(QtCore.QRect(530, 360, 121, 70))
		self.pushButton.setText("DELETE\n The Menu")
		self.pushButton.setFont(QFont("Arial", 15, QFont.Bold))

		cpn.settext(self, 'delhead', QFont("Arial", 40, 100, QFont.Bold), (110, 40, 500, 90), "<font color=%s>%s</font>" %('#5F2F2D', "DETELE THE MENU"))

		self.pushButton.clicked.connect(self.delfromDB)

	def delfromDB(self):
		lista = []
		#checking
		txt_0 = self.items['txt_0'].text() is None #not in sql.Input_stallData.getStall(self)
		txt_1 = self.items['txt_1'].text() is None
		#pass checkings
		if (txt_0 or txt_1):
			print("Please give correct stall Name, item Name ")
			#print (sql.Input_stallData.getStall(self))
			#print (lista)
		else :
			print("DELETE FROM Menu in progress")
			lista.append(self.items['txt_0'].text())
			lista.append(self.items['txt_1'].text())
			print(lista)
			newdish = sql.Input_menuData(lista[0], lista[1])
			newdish.del_dish_DB()


