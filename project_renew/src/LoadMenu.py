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

startcoords1=(60, 40)



class LoadMenu(QWidget):

	def __init__(self,parent=None):
		super(LoadMenu,self).__init__(parent)
		#setup widget
		self.centralWidget = QtWidgets.QWidget(self)
		self.DeletMenu = QtWidgets.QWidget(self.centralWidget)
		self.DeletMenu.setGeometry(cpn.geometrysize)
		cpn.Set_Background(self,"./Pictures/restaurant-menu-background.jpg")

		self.items={}
		self.Load_Menu()
	

	#page set up
	def Load_Menu(self):	
		
		## lables and text boxes
		for i in range (1):
			self.items['txt_'+"Location"] = QtWidgets.QLineEdit(self)
			self.items['txt_'+"Location"].setText("Browse for the menu file")
			self.items['txt_'+"Location"].setGeometry(QtCore.QRect(220, 200+i*60, 251, 41))
			self.items['label_'+"Location"] = QtWidgets.QLabel(self)
			self.items['label_'+"Location"].setGeometry(QtCore.QRect(80, 200+i*60, 171, 31))
			self.items['label_'+"Location"].setFont(QFont("Arial",17,QFont.Bold))
			
		self.items['label_Location'].setText("<font color=%s>%s</font>" %('#5F2F2D', "Location"))
		#self.items['label_1'].setText("<font color=%s>%s</font>" %('#5F2F2D', "Location"))
		
		## lock stall Name
		## checkbox
		self.items['txt_Location'].setDisabled(True)
		self.checkBox = QtWidgets.QCheckBox(self)
		self.checkBox.setGeometry(QtCore.QRect(530, 210, 85, 21))
		self.checkBox.setChecked(True)
		self.checkBox.toggled.connect(self.items['txt_Location'].setDisabled)

		## lable for checkbox
		self.checkBox_balel = QtWidgets.QLabel(self)
		self.checkBox_balel.setGeometry(QtCore.QRect(550, 210, 85, 21))
		self.checkBox_balel.setFont(QFont("Arial",13,QFont.Bold))
		self.checkBox_balel.setText("<font color=%s>%s</font>" %('#5F2F2D', "LOCK"))

		## button for browse menu
		self.pushButton = QtWidgets.QPushButton(self)
		self.pushButton.setGeometry(QtCore.QRect(530, 260, 121, 70))
		self.pushButton.setText(" BROWSE \n The Menu")
		self.pushButton.setFont(QFont("Arial",15,QFont.Bold))

		## title
		self.labeltitle = QtWidgets.QLabel(self)
		self.labeltitle.setGeometry(QtCore.QRect(140, 20, 3000, 90))
		self.labeltitle.setFont(QFont("Arial",30,QFont.Bold))
		self.labeltitle.setText("<font color=%s>%s</font>" %('#5F2F2D', "Browse New Menu File"))
		self.pushButton.clicked.connect(self.browse_data1)

	def browse_data1(self):
		data_path=QtWidgets.QFileDialog.getOpenFileName(self,'Open File',"D:\Programming",'*.txt',)
		with open('data_path.pickle', 'wb') as handle:
			_pickle.dump(data_path,handle,protocol=_pickle.HIGHEST_PROTOCOL)

		

