#!/usr/bin/env python

from PyQt5 import QtCore, QtGui, QtWidgets
from data import menu_data
import stalls
from Functional import Component as cpn
from Functional import sql


### varible delclare
style1 = {"size":15, 'bold':True, 'weight':100, 'colorbgd':'#FFC300', 'colorpress':'#AF267E', 'colorhover':'#04070f', 'w':'110', 'h':'90'}
style2 = {"size":15, 'bold':True, 'weight':100, 'colorbgd':'#FFC300', 'colorpress':'#AF267E', 'colorhover':'#04070f', 'w':'230', 'h':'160'}
headingfont = QtGui.QFont("Arial", 34, QtGui.QFont.Bold)
stallist = sql.getfromDB()
stall = menu_data.ViewMenuButtons['stallBut']


#==========================================================================================================
###
### This file contains 3 pages connected to one main, using stackwidget to change page
###
###
### This is the main page connect to all 3 pages
###
class View_Menu(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super(View_Menu, self).__init__(parent)
		self.resize(800, 600)
		self.setWindowOpacity(0.9)
		self.stackedwidget = QtWidgets.QStackedWidget(self)
		self.stackedwidget.setGeometry(cpn.geometrysize)
		self.add_first_page()
		self.stallChoice = ""


	'''
	def general_link_click(self,nums):
		print("general_link_click " + str(nums))
		global choice
		choice=nums
		return nums
		#print("general_link_click " + str(self.nums))		
	'''


	def add_first_page(self):
		self.first_page = View_Menu_1st_Page()
		self.stackedwidget.addWidget(self.first_page)
		self.stackedwidget.setCurrentIndex(0)
		self.load_stall_buttons()


#==========================================================================================================
	##
	## the loop method is NOT working, as the function only takes the last value
	##
	##
	# for stall in menu_data.ViewMenuButtons['stallBut']:
	# 	print (stall['index'])
	# 	cpn.newbuttonfunction(self,stall["butName"],stall['position'],stall["name"],lambda:View_Menu.add_second_page(self,self.general_link_click(stall['index'])),**style1)


		# cpn.buttonFullStyle(self,lambda:View_Menu.add_second_page(self,self.Get_click(stalbtn[0]['buttxt'][:3])),**stalbtn[0])
		# cpn.buttonFullStyle(self,lambda:View_Menu.add_second_page(self,stalbtn[1]['buttxt'][:3]),**stalbtn[1])
		# cpn.buttonFullStyle(self,lambda:View_Menu.add_second_page(self,stalbtn[2]['buttxt'][:3]),**stalbtn[2])
		# cpn.buttonFullStyle(self,lambda:View_Menu.add_second_page(self,stalbtn[3]['buttxt'][:3]),**stalbtn[3])

#=============================================================================================================

	### call button fuctions, with lambda function.
	### lambda function can not use loop method to call with different input
	### But i finally find the way.
	### not fully understand why it not work work previously
	###
	### button creation and click event handler for 1st page
	def load_stall_buttons(self):

		stalbtn = menu_data.ViewMenuButtons['stallBut']
		for stall in stalbtn:

			cpn.buttonFullStyle(self, self.Get_click(stall['buttxt'][:3]), **stall)



	def Get_click(self, click):

		print('++++++++++++')
		print(click)
		return lambda: View_Menu.add_second_page(self, click)


	def add_second_page(self, store):
		self.second_page = View_Menu_2nd_Page(store)
		self.stallChoice = store
		print(store)
		print ("#####################################")

		self.stackedwidget.addWidget(self.second_page)
		self.stackedwidget.setCurrentIndex(1)

		#hide 1st page button
		cpn.button["McButton"].hide()
		cpn.button["KFCButton"].hide()
		cpn.button["SubButton"].hide()
		cpn.button["MYButton"].hide()

		#button click event handler for 2nd page
		cpn.button['calendarSubmit'].clicked.connect(lambda: self.add_third_page(store, self.second_page.SearchMenu()))
		#print (stalls.button)


	def add_third_page(self, store, DatetimeList):
		self.third_page = View_Menu_Third_Page(store, DatetimeList)
		self.stackedwidget.addWidget(self.third_page)
		self.stackedwidget.setCurrentIndex(2)
		cpn.button['goback'].clicked.connect(self.go_back)


	def go_back(self):
		self.stackedwidget.setCurrentIndex(0)
		self.stackedwidget.removeWidget(self.second_page)
		self.stackedwidget.removeWidget(self.third_page)


		#show 1st page button
		cpn.button["McButton"].show()
		cpn.button["KFCButton"].show()
		cpn.button["SubButton"].show()
		cpn.button["MYButton"].show()




#==========================================================================================================

### The first page
class View_Menu_1st_Page(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super(View_Menu_1st_Page, self).__init__(parent)

		#load background
		cpn.Set_Background(self, './Pictures/northspine.jpg')
		
		#set heading
		self.Page_heading()


	#setup text labels and stall buttons
	def Page_heading(self):
		self.heading = QtWidgets.QLabel(self)
		self.heading.setGeometry(QtCore.QRect(140, 40, 500, 71))
		self.heading.setFont(headingfont)
		self.heading.setText("Select Store Menu")
		
	#old menu buttons are deleted





### The second page
class View_Menu_2nd_Page(QtWidgets.QWidget):
	
	def __init__(self, menuStall, parent=None):
		super(View_Menu_2nd_Page, self).__init__(parent)

		### loop and check for correct stall choosed
		### pass value into the functions
		for stall in stallist:
			if (menuStall in stall['stallName']):

				# load background
				cpn.Set_Background(self, stall['menuBackground'])

				# set other lables and heading
				self.logoTips(stall)

		# set submit buttons
		cpn.newbuttonfunction(self, "calendarSubmit", (530, 110, 81, 91), "calendar \nSubmit", None, **style1)

		#set canlendar
		self.SetupCalenderSet()


	#calender time set
	def SetupCalenderSet(self):
		cpn.setfont('Calender', 20, 75, True)
		self.stallCalenderTime = QtWidgets.QDateTimeEdit(self)
		self.stallCalenderTime.setGeometry(QtCore.QRect(120, 120, 351, 51))
		self.stallCalenderTime.setFont(cpn.font['Calender'])
		self.stallCalenderTime.setDateTime(QtCore.QDateTime.currentDateTime())
		self.stallCalenderTime.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
		self.stallCalenderTime.setKeyboardTracking(True)
		self.stallCalenderTime.setAlignment(QtCore.Qt.AlignCenter)
		self.stallCalenderTime.setStyleSheet(
										"#stallCalenderTime {\n"
										"	 border-radius: 10px;\n"
										"	 padding: 2px 4px;\n"
										"	 color: #6c6c6c;}\n"
										"#stallCalenderTime:focus {\n"
										"	 color: #010101;}\n")
		#calender only
		self.calendarWidget = QtWidgets.QCalendarWidget(self)
		self.calendarWidget.setGeometry(QtCore.QRect(120, 230, 400, 300))
		self.calendarWidget.setVerticalHeaderFormat(self.calendarWidget.NoVerticalHeader)
		fmtGreen = QtGui.QTextCharFormat()
		fmtGreen.setForeground(QtGui.QBrush(QtCore.Qt.green))
		self.calendarWidget.setWeekdayTextFormat(QtCore.Qt.Saturday, fmtGreen)
		fmtOrange = QtGui.QTextCharFormat()
		fmtOrange.setForeground(QtGui.QBrush(QtGui.QColor(252, 140, 28)))
		self.calendarWidget.setWeekdayTextFormat(QtCore.Qt.Sunday, fmtOrange)


	def logoTips(self, stall):
		## use setFont
		cpn.setfont('tip', 20, 85, True)

		## use setlable
		cpn.settext(self, 'Tip', cpn.font['tip'], (150, 60, 350, 61), 'Please Select Date & Time')

		## use setlable
		cpn.setlable(self, 'logo', (30, 150, 80, 70), stall['icon'], True)


	#pass Date and Time to get specific date/time menu
	def SearchMenu(self):
		SearchDatetime = self.stallCalenderTime.dateTime()
		SearchDatetime = SearchDatetime.toPyDateTime()
		SearchDate = SearchDatetime.weekday() + 1
		DateTime = [SearchDate, SearchDatetime.hour]
		return DateTime



#==========================================================================================================

### the 3rd page
class View_Menu_Third_Page(QtWidgets.QWidget):

	def __init__(self, menuStall, DatetimeList=0, parent=None):
		super(View_Menu_Third_Page, self).__init__(parent)
		self.mainwidget = QtWidgets.QWidget(self)
		self.count = 0
		self.items = {}

		## 
		### loop and check for correct stall choosed
		### pass value into the functions
		###
		self.find_stall(menuStall)

		# set goback button
		cpn.newbuttonfunction(self, "goback", (640, 440, 72, 72), "GO \nBack", None, **style1)



	def find_stall(self, menuStall):
		for stall in stallist:
			if (menuStall in stall['stallName']):

				### set background
				###
				cpn.Set_Background(self.mainwidget, stall['backGround'])

				for menu in stall['stallMenu']:
					###
					### this is form stalls page
					###
					### New function for loading menus
					### Resued the menu function in stalls page
					### It works perfectly fine.
					###
					stalls.stalls_window.StallIcoPriName(self, menu, False)



	'''
	### for debugging
	###
	def stalls_menu(self,menuStall):
		#print (menu_data.stall_list[menuStall]['stallMenu'][1]['logo'])
		for stall in stallist:
			
			if (menuStall in stall['stallName'] ):
				print (stall['stallName'])

	'''



#==========================================================================================================
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	#Form = QtWidgets.QWidget()
	ui = View_Menu()
	#ui.setupUi(Form)
	ui.show()

	sys.exit(app.exec_())