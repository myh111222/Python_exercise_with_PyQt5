# -*- coding: utf-8 -*-

import sqlite3
import json
from sqlite3 import Error
import os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import tempfile
import time
#import mysql.connector
#from mysql.connector import Error

conn=sqlite3.connect("test.db")
c=conn.cursor()


conn.execute(
	"""
			CREATE TABLE IF NOT EXISTS "imagesTest" 
						( 
							"id" INT NOT NULL , 
							"name" TEXT NOT NULL , 
							"photo" BLOB NOT NULL ,  
							"resume" TEXT NOT NULL , 
							PRIMARY KEY ("id")
							)
					""")

def writeTofile(data, filename):
	# Convert binary data to proper format and write it on Hard Disk
	with open(filename, 'wb') as file:
		file.write(data)
	print("Stored blob data into: ", filename, "\n")



def convertToBinaryData(filename):
	#Convert digital data to binary format
	with open(filename, 'rb') as file:
		blobData = file.read()
	return blobData

def insertBLOB(empId, name, photo, resumeFile):
	try:
		sqliteConnection = sqlite3.connect('test.db')
		cursor = sqliteConnection.cursor()
		print("Connected to SQLite")
		sqlite_insert_blob_query = """ INSERT INTO imagesTest
								  (id, name, photo, resume) VALUES (?, ?, ?, ?)"""

		empPhoto = convertToBinaryData(photo)
		print (type(empPhoto))
		resume = resumeFile
		# Convert data into tuple format
		data_tuple = (empId, name, empPhoto, resume)
		cursor.execute(sqlite_insert_blob_query, data_tuple)
		sqliteConnection.commit()
		print("Image and file inserted successfully as a BLOB into a table")
		cursor.close()

	except sqlite3.Error as error:
		print("Failed to insert blob data into sqlite table", error)
	finally:
		if (sqliteConnection):
			sqliteConnection.close()
			print("the sqlite connection is closed")

#insertBLOB(1, "Eric", "./Pictures/McDonald.png", "eric.txt")
#insertBLOB(2, "Scott", "./Pictures/KFC.png", "scott.txt")


c.execute("""select name from imagesTest""" )
haha=c.fetchall()
print (haha)


menuKeys=["id", "name", "photo", "resume"]

import Component as cpn

class AddMenu(QWidget):

	def __init__(self,parent=None):
		super(AddMenu,self).__init__(parent)
		#setup widget
		self.centralWidget = QtWidgets.QWidget(self)
		self.AddMenu = QtWidgets.QWidget(self.centralWidget)
		self.AddMenu.setGeometry(cpn.geometrysize)
		cpn.Set_Background(self.centralWidget ,"./Pictures/restaurant-menu-background.jpg")
		self.label =  QtWidgets.QLabel(self)
		self.items={}
		self.AddtoMenu()

	## function to setup buttons and text box

	def readBlobData(self,empId):
		datalist=[]
		try:
			sqliteConnection = sqlite3.connect('test.db')
			cursor = sqliteConnection.cursor()
			print("Connected to SQLite")

			cursor.execute("""SELECT * from imagesTest where id = ?""", (empId,))
			record = cursor.fetchall()
			for row in record:
				print("Id = ", row[0], "Name = ", row[2])
				for item in row:
					time.sleep(2)
					print (item)
					datalist.append(item)
					id = row[0]
					name  = row[1]
					photo = row[2]
					resumeFile = row[3]
					
					print("Storing employee image and resume on disk \n")
					photoPath = "./tmp/" + name + ".png"
					writeTofile(photo, photoPath)
					self.displayImageData(photo)
			cursor.close()

		except sqlite3.Error as error:
			print("Failed to read blob data from sqlite table", error)
		finally:
			if (sqliteConnection):
				sqliteConnection.close()
				print("sqlite connection is closed")

	def AddtoMenu(self):	
		count =0
		self.imagePath=''
		# setup text box and text lables
		for i in menuKeys:
			cpn.settext(self,i,cpn.Gefont,(140, 110 + count*60, 171, 31),"<font color=%s>%s</font>" %('#5F2F2D', i))
			cpn.setTXbox(self,i,(265, 110 + count*60, 251, 41),"Enter here")
			count =count+1

		#lock stall Name by check box
		cpn.txtbox['id'].setDisabled(False)

		#check box
		self.checkBox = QtWidgets.QCheckBox(self)
		self.checkBox.setGeometry(QtCore.QRect(530, 300, 85, 21))
		self.checkBox.setChecked(True)
		self.checkBox.toggled.connect(cpn.txtbox['id'].setDisabled)

		#new txt lable
		cpn.settext(self,'checkBox',cpn.Gefont,(535, 300, 85, 21),"<font color=%s>%s</font>" %('#5F2F2D', "LOCK"))
		
		#new button
		cpn.newbuttonfunction(self,'submit',(520, 340, 121, 70),"Submit\n To Menu",None,**cpn.style2)
		cpn.newbuttonfunction(self,'Browse',(400, 340, 121, 70),"Browse\nImage",self.getImage,**cpn.style2)

		self.labeltitle = QtWidgets.QLabel(self)
		self.labeltitle.setGeometry(QtCore.QRect(210, 20, 300, 90))
		self.labeltitle.setFont(QFont("Arial",30,QFont.Bold))
		self.labeltitle.setText("<font color=%s>%s</font>" %('#5F2F2D', "ADD TO MENU"))
		
		vbox = QVBoxLayout()
		vbox.addWidget(self.label)
		self.label.setGeometry(QtCore.QRect(30, 200, 150, 200))

		try:
			cpn.button['submit'].clicked.connect(self.addtoDB)
		except :
			print ("failed to add to DB")

	def getImage(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file',
											'./', "Image files (*)")
		self.imagePath = fname[0]
		print (self.imagePath)
		cpn.txtbox["photo"].setText(str(self.imagePath))
		pixmap = QPixmap(self.imagePath)
		self.displayImageChose(QPixmap(pixmap))
		#self.resize(pixmap.width(), pixmap.height())

	def displayImageChose(self,images):
		
		self.label.setPixmap(images)
		self.label.setScaledContents(True)

	def displayImageData(self,images):
		self.label.setPixmap(QPixmap.loadFromData(images,'png'))
		self.label.setScaledContents(True)


	#This function performs add to DB
	def addtoDB(self):
		lista=[]
		#checkings:
		txt_0=cpn.txtbox["id"].text().isdigit()
		txt_1=cpn.txtbox["name"].text() is None
		txt_2=cpn.txtbox["photo"].text() is None
		txt_3=cpn.txtbox["resume"].text() is None

		#pass checkings
		if (not txt_0 or txt_1 or txt_2 or txt_3):
			print ("Please give correct stall Name, item Name, price, orderNumber, and MenuType (lunch/breakfirst) ")
			print (" ")
			#print (sql.Input_stallData.getStall(self))
			#print (lista)
		else :
			print ("add menu in progress")
			for i in menuKeys:
				print (cpn.txtbox[i].text())
				lista.append(cpn.txtbox[i].text())

			insertBLOB(int(lista[0]),lista[1],lista[2],lista[3])
			self.readBlobData(int(lista[0]))
			

				#
			#print (lista)
			#newdish= sql.Input_menuData(lista[0],lista[1],lista[2],int(lista[3]),lista[4],int(lista[5]))
			#newdish.add_dish_DB()


#==========================================================================================================
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	#Form = QtWidgets.QWidget()
	ui = AddMenu()
	#ui.setupUi(Form)
	ui.show()

	sys.exit(app.exec_())