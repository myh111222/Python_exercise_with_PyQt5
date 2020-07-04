from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QWidget ,QMessageBox,QApplication,QStackedWidget ,QVBoxLayout,QHBoxLayout,QListWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal, QTimer,QDate, QTime
import os
from datetime import datetime
import pytz
import kfcCombine
import viewMenu_Mac





class View_Menu_First_Page(QtWidgets.QWidget):
	def __init__(self,parent=None):
		super(View_Menu_First_Page,self).__init__(parent)
		self.setupUi()


	def setupUi(self):
		self.setObjectName("ViewMenu")
		self.resize(800, 600)

		self.First_PageBG = QtWidgets.QLabel(self)
		self.First_PageBG.setGeometry(QtCore.QRect(0, 0, 800, 600))
		self.First_PageBG.setObjectName("SubwayBG")
		self.First_PageBG.setPixmap(QtGui.QPixmap('./Pictures/northspine.jpg'))
		self.First_PageBG.setScaledContents(True)
		self.First_PageBG.setAlignment(QtCore.Qt.AlignCenter)

		self.setAutoFillBackground(True)
		p = self.palette()
		p.setColor(self.backgroundRole(), QtCore.Qt.black)
		self.setPalette(p)
		

		self.setWindowOpacity(0.9)
		self.label = QtWidgets.QLabel(self)
		self.label.setGeometry(QtCore.QRect(90, 40, 500, 71))
		font = QtGui.QFont()
		font.setPointSize(24)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")

		self.McButton = QtWidgets.QPushButton(self)
		self.McButton.setGeometry(QtCore.QRect(150, 120, 151, 111))
		self.McButton.setObjectName("McButton")
		self.McButton.clicked.connect(self.Mc_link_click)
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(18)
		font.setBold(True)
		font.setWeight(75)
		self.McButton.setFont(font)
		self.McButton.setStyleSheet("#McButton{\n"
									"	 background-color: #FFC300;\n"
									"	 min-width: 200px;\n"
									"	 max-width: 200px;\n"
									"	 min-height: 170px;\n"
									"	 max-height: 170px;\n"
									"	 border-radius: 50px; \n"
									"	 color: #ED1C22;\n"
									"}\n"
									"#McButton:hover {\n"
									"	 background-color: #ED1C22;\n"
									"	 color: #FFC300;\n"
									"}\n"
									"#McButton:pressed {\n"
									"	 background-color: #FC7A08;\n"
									"	 color: #000000;\n"
									"}")

		self.SubButton = QtWidgets.QPushButton(self)
		self.SubButton.setGeometry(QtCore.QRect(450, 120, 151, 111))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.SubButton.setFont(font)
		self.SubButton.setObjectName("SubButton")
		self.SubButton.clicked.connect(self.Subway_link_click)
		self.SubButton.setStyleSheet(
									"#SubButton{\n"
									"	 background-color: #009743;\n"
									"	 min-width: 200px;\n"
									"	 max-width: 200px;\n"
									"	 min-height: 170px;\n"
									"	 max-height: 170px;\n"
									"	 border-radius: 50px; \n"
									"	 color: #ffcb0a;\n"
									"}\n"
									"#SubButton:hover {\n"
									"	 background-color: #ffcb0a;\n"
									"	 color:	 #009743;\n"
									"}\n"
									"#SubButton:pressed {\n"
									"	 background-color: #94F272;\n"
									"	 color: #000000;\n"
									"}"
									)
											

		self.MYButton = QtWidgets.QPushButton(self)
		self.MYButton.setGeometry(QtCore.QRect(150, 300, 151, 111))
		self.MYButton.setObjectName("MYButton")
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.MYButton.setFont(font)
		self.MYButton.clicked.connect(self.MY_link_click)
		self.MYButton.setStyleSheet("#MYButton{\n"
									"	 background-color: #F720F3;\n"
									"	 min-width: 200px;\n"
									"	 max-width: 200px;\n"
									"	 min-height: 170px;\n"
									"	 max-height: 170px;\n"
									"	 border-radius: 50px; \n"
									"	 color: #009000;\n"#009000
									"}\n"
									"#MYButton:hover {\n"
									"	 background-color: #009000;\n"
									"	 color: #F720F3;\n"
									"}\n"
									"#MYButton:pressed {\n"
									"	 background-color: #89F720;\n"
									"	 color: #000000;\n"
									"}")
		
		self.KFCButton = QtWidgets.QPushButton(self)
		self.KFCButton.setGeometry(QtCore.QRect(450, 300, 151, 111))
		self.KFCButton.setObjectName("KFCButton")
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.KFCButton.setFont(font)
		self.KFCButton.clicked.connect(self.KFC_link_click)
		self.KFCButton.setStyleSheet("#KFCButton{\n"
									"	 background-color: #A3080B;\n"
									"	 min-width: 200px;\n"
									"	 max-width: 200px;\n"
									"	 min-height: 170px;\n"
									"	 max-height: 170px;\n"
									"	 border-radius: 50px; \n"
									"	 color: #FFFFFF;\n"
									"}\n"
									"#KFCButton:hover {\n"
									"	 background-color: #000000;\n"
									"	 color: #A3080B;\n"
									"}\n"
									"#KFCButton:pressed {\n"
									"	 background-color: #FFFFFF;\n"
									"	 color: #000000;\n"
									"}")
		
		self.retranslateUi()
		QtCore.QMetaObject.connectSlotsByName(self)

	def retranslateUi(self):
		_translate = QtCore.QCoreApplication.translate
		self.setWindowTitle(_translate("View_Menu_First_Page", "View_Menu_First_Page"))
		self.label.setText(_translate("View_Menu_First_Page", "Select Store Menu"))
		self.SubButton.setText(_translate("View_Menu_First_Page", "Subway"))
		self.McButton.setText(_translate('View_Menu_First_Page',"McDonald's"))
		self.MYButton.setText(_translate('View_Menu_First_Page',"Malay\nStall"))
		self.KFCButton.setText(_translate('View_Menu_First_Page',"KFC"))
	
	def Subway_link_click(self):
		print('Subway')
		return "Subway"
	def Mc_link_click(self):
		print("McDonald's")
		return "Mcdonalds"
	def MY_link_click(self):
		print("Malay Stall")
		return "Malay"
	def KFC_link_click(self):
		print("KFC")
		return "KFC"



class View_Menu_Second_Page(QtWidgets.QWidget):
	
	def __init__(self,text,parent=None):
		super(View_Menu_Second_Page,self).__init__(parent)
		self.setupUi(text)

	def setupUi(self,text):
		self.setObjectName("View_Menu_Second_Page")
		self.resize(800, 600)

		self.setWindowOpacity(0.9)

		self.setAutoFillBackground(True)
		p = self.palette()
		p.setColor(self.backgroundRole(), QtCore.Qt.black)
		self.setPalette(p)


		self.label_3 = QtWidgets.QLabel(self)
		self.label_3.setGeometry(QtCore.QRect(0, 0, 800,600))
		self.label_3.setText("")
		self.label_3.setPixmap(QtGui.QPixmap("./Pictures/"+text+".jpg"))
		self.label_3.setScaledContents(True)
		self.label_3.setObjectName("label_3")

		self.dateTimeEdit = QtWidgets.QDateTimeEdit(self)
		self.dateTimeEdit.setGeometry(QtCore.QRect(120, 120, 351, 51))
		font = QtGui.QFont()
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.dateTimeEdit.setFont(font)
		self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
		self.dateTimeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
		self.dateTimeEdit.setKeyboardTracking(True)
		self.dateTimeEdit.setAlignment(QtCore.Qt.AlignCenter)
		self.dateTimeEdit.setObjectName("dateTimeEdit")
		self.dateTimeEdit.setStyleSheet("#dateTimeEdit {\n"
"	 border-radius: 10px;\n"
"	 padding: 2px 4px;\n"
"	 color: #6c6c6c;\n"

"}\n"
"#dateTimeEdit:focus {\n"
"	 color: #010101;\n"
"}")


		self.calendarWidget = QtWidgets.QCalendarWidget(self)
		self.calendarWidget.setGeometry(QtCore.QRect(120, 230, 400, 300))
		self.calendarWidget.setObjectName("calendarWidget")

		self.calendarWidget.setVerticalHeaderFormat(self.calendarWidget.NoVerticalHeader)

		fmtGreen = QtGui.QTextCharFormat()
		fmtGreen.setForeground(QtGui.QBrush(QtCore.Qt.green))
		self.calendarWidget.setWeekdayTextFormat(QtCore.Qt.Saturday, fmtGreen)

		fmtOrange = QtGui.QTextCharFormat()
		fmtOrange.setForeground(QtGui.QBrush(QtGui.QColor(252, 140, 28)))
		self.calendarWidget.setWeekdayTextFormat(QtCore.Qt.Sunday, fmtOrange)

		self.BlueButton = QtWidgets.QPushButton(self)
		self.BlueButton.setGeometry(QtCore.QRect(530, 110, 81, 91))
		self.BlueButton.setObjectName("BlueButton")
		self.BlueButton.clicked.connect(self.SearchMenu)
		self.BlueButton.setStyleSheet("#BlueButton {\n"
"	 background-color: #303d5e;\n"
"	 /*minimum size*/\n"
"	 min-width: 96px;\n"
"	 max-width: 96px;\n"
"	 min-height: 96px;\n"
"	 max-height: 96px;\n"
"	 border-radius: 48px; /*Round*/\n"
"	 color: #FFFFFF;\n"
"}\n"
"#BlueButton:hover {\n"
"	 background-color: #516cb0;\n"
"}\n"
"#BlueButton:pressed {\n"
"	 background-color: #04070f;\n"
"}")



		self.Tip = QtWidgets.QLabel(self)
		self.Tip.setGeometry(QtCore.QRect(150, 70, 250, 51))
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.Tip.setFont(font)
		self.Tip.setAlignment(QtCore.Qt.AlignCenter)
		self.Tip.setObjectName("Tip")
		
	
		self.Logo = QtWidgets.QLabel(self)
		self.Logo.setGeometry(QtCore.QRect(200, 30, 180, 61))
		self.Logo.setObjectName(text)
		#llogo = self.ChangeLogo()
		#print(llogo[text])
		#self.Logo.setPixmap(QtGui.QPixmap(llogo[text]))
		#self.Logo.setScaledContents(True)
		#self.Logo.setAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.Logo.setFont(font)


		self.retranslateUi(text)
		self.calendarWidget.clicked['QDate'].connect(self.dateTimeEdit.setDate)
		QtCore.QMetaObject.connectSlotsByName(self)
	
	
	def ChangeLogo(self):
		Logo = {'Mcdonalds':'./Pictures/ViewLogo/McDonald.jpg','Subway':'./Pictures/ViewLogo/Subway.png','Malay':'./Pictures/ViewLogo/Malay.png','KFC':'./Pictures/ViewLogo/KFC.png'}
		return Logo






	#pass Date and Time to get specific date/time menu
	def SearchMenu(self):
		SearchDatetime = self.dateTimeEdit.dateTime()
		SearchDatetime = SearchDatetime.toPyDateTime()
		SearchDate = SearchDatetime.weekday() + 1 
		DateTime = [SearchDate,SearchDatetime.hour]
		return DateTime

	def retranslateUi(self,text):
		_translate = QtCore.QCoreApplication.translate
		self.setWindowTitle(_translate("View_Menu_Second_Page", "Select Date"))
		self.BlueButton.setText(_translate("View_Menu_Second_Page", "Submit"))
		self.Logo.setText(_translate("View_Menu_Second_Page", text))
		#set logo text to 
		self.Tip.setText(_translate("Select Date", "Please Select Date & Time"))



StyleSheet = '''
#qt_calendar_navigationbar {
	background-color: rgb(0, 188, 212);
	min-height: 100px;
}
#qt_calendar_prevmonth, #qt_calendar_nextmonth {
	border: none; 
	margin-top: 64px;
	color: white;
	min-width: 36px;
	max-width: 36px;
	min-height: 36px;
	max-height: 36px;
	border-radius: 18px; 
	font-weight: bold; 
	qproperty-icon: none; 
	background-color: transparent;
}
#qt_calendar_prevmonth {
	qproperty-text: "<"; 
}
#qt_calendar_nextmonth {
	qproperty-text: ">";
}
#qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {
	background-color: rgba(225, 225, 225, 100);
}
#qt_calendar_prevmonth:pressed, #qt_calendar_nextmonth:pressed {
	background-color: rgba(235, 235, 235, 100);
}

#qt_calendar_yearbutton, #qt_calendar_monthbutton {
	color: white;
	margin: 18px;
	min-width: 60px;
	border-radius: 30px;
}
#qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover {
	background-color: rgba(225, 225, 225, 100);
}
#qt_calendar_yearbutton:pressed, #qt_calendar_monthbutton:pressed {
	background-color: rgba(235, 235, 235, 100);
}

#qt_calendar_yearedit {
	min-width: 50px;
	color: white;
	background: transparent;
}
#qt_calendar_yearedit::up-button { 
	width: 20px;
	subcontrol-position: right;
}
#qt_calendar_yearedit::down-button { 
	width: 20px;
	subcontrol-position: left;
}
CalendarWidget QToolButton QMenu {
	 background-color: white;
}
CalendarWidget QToolButton QMenu::item {
	padding: 10px;
}
CalendarWidget QToolButton QMenu::item:selected:enabled {
	background-color: rgb(230, 230, 230);
}
CalendarWidget QToolButton::menu-indicator {
	subcontrol-position: right center;
}

#qt_calendar_calendarview {
	outline: 0px;
	selection-background-color: rgb(0, 188, 212);
}


'''

class View_Menu_Third_Page(QtWidgets.QWidget):
	
	def __init__(self,store,DateTimeList,parent=None):
		super(View_Menu_Third_Page,self).__init__(parent)
		#DateTime = [SearchDate,SearchDatetime.hour]
		self.setMinimumSize(QtCore.QSize(800, 600))
		self.setMaximumSize(QtCore.QSize(800, 600))
		
		self.listWidget = QListWidget(self)
		self.stackedWidget = QStackedWidget(self)
		self.mainwidget = QtWidgets.QWidget(self)


		if 'Subway' in store:
			self.setupUi_Subway(DateTimeList[1])
		elif 'Malay' in store:
			self.setupUi_MY(DateTimeList[0])
			
		elif 'Mcdonalds'in store:
			if DateTimeList[1] >= 11:
				viewMenu_Mac.ViewMenus_MacC.setup_Ui_Pm_Mcdonalds(self)
			else:
				viewMenu_Mac.ViewMenus_MacC.setup_Ui_Am_Mcdonalds(self)
		elif 'KFC' in store:
			layout = QHBoxLayout(self, spacing=0)
			layout.addWidget(self.stackedWidget)		
			if DateTimeList[1] < 12:
				kfcCombine.KFC_breakfast_window.kfc_pric_breakfast(self)
				
				self.stackedWidget.addWidget(kfcCombine.KFC_breakfast_window(ActivButton=False))
			else:
				self.stackedWidget.addWidget(kfcCombine.KFC_daily_window(ActivButton=False))

		_translate = QtCore.QCoreApplication.translate

		self.BlueButton_2 = QtWidgets.QPushButton(self)
		self.BlueButton_2.setGeometry(QtCore.QRect(700, 500, 72, 72))
		self.BlueButton_2.setText("Back")
		self.BlueButton_2.setStyleSheet("QPushButton {\n"
"	 border: none; \n"
"	 background-color: #303d5e;\n"
"	 /*minimum size*/\n"
"	 min-width: 72px;\n"
"	 max-width: 72px;\n"
"	 min-height: 72px;\n"
"	 max-height: 72px;\n"
"	 border-radius: 36px; /*Round*/\n"
"	 color: #FFFFFF;\n"
"	 \n"
"}\n"
"QPushButton:hover {\n"
"	  background-color: #516cb0;\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"	  background-color: #04070f;\n"
"}\n"
)

	def setupUi_MY(self,DateTimeDate):
		self.setObjectName('MalayStall')
		self.resize(800,600)
		self.setMinimumSize(QtCore.QSize(800, 600))
		self.setMaximumSize(QtCore.QSize(800, 600))
		self.mainwidget = QtWidgets.QWidget(self)
		self.mainwidget.setMinimumSize(QtCore.QSize(800, 600))
		self.mainwidget.setObjectName("mainwidget")
		self.MYBG = QtWidgets.QLabel(self)
		self.MYBG.setGeometry(QtCore.QRect(0, 0, 800, 600))
		self.MYBG.setObjectName("MYBG")
		self.MYBG.setPixmap(QtGui.QPixmap('./Pictures/kfc/malaybackground2_4.jpg'))
		self.MYBG.setScaledContents(True)
		self.MYBG.setAlignment(QtCore.Qt.AlignCenter)
		self.setWindowOpacity(0.9)

		self.setAutoFillBackground(True)
		p = self.palette()
		p.setColor(self.backgroundRole(), QtCore.Qt.black)
		self.setPalette(p)
		self.gridLayout = QtWidgets.QGridLayout(self)
		self.gridLayout.setObjectName('gridLayout')


		MYMenuTuple = self.MYMenu(DateTimeDate)


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

		#self.MYBG.raise_()
		self.item0_price.raise_()
		self.item1_price.raise_()
		self.item2_price.raise_()
		self.item3_price.raise_()
		self.item0_Pic.raise_()
		self.item1_Pic.raise_()
		self.item2_Pic.raise_()
		self.item3_Pic.raise_()
		self.item0_Name.raise_()
		self.item1_Name.raise_()
		self.item2_Name.raise_()
		self.item3_Name.raise_()

		
		self.retranslateUi_MY(MYMenuTuple)


	def setupUi_Subway(self,DatetimeTime):
		self.setObjectName("Subway")
		self.resize(800, 600)
		self.setMinimumSize(QtCore.QSize(800, 600))
		self.setMaximumSize(QtCore.QSize(800, 600))
		self.SubwayBG = QtWidgets.QLabel(self)
		self.SubwayBG.setGeometry(QtCore.QRect(0, 0, 800, 600))
		self.SubwayBG.setObjectName("SubwayBG")
		self.SubwayBG.setPixmap(QtGui.QPixmap('./Pictures/kfc/subwayBG_4.jpg'))
		self.SubwayBG.setScaledContents(True)
		self.SubwayBG.setAlignment(QtCore.Qt.AlignCenter)
		self.mainwidget = QtWidgets.QWidget(self)
		self.mainwidget.setMinimumSize(QtCore.QSize(800, 600))
		self.mainwidget.setObjectName("mainwidget")
		self.setWindowOpacity(0.9)



		self.setAutoFillBackground(True)
		p = self.palette()
		p.setColor(self.backgroundRole(), QtCore.Qt.black)
		self.setPalette(p)
		self.gridLayout = QtWidgets.QGridLayout(self.mainwidget)
		self.gridLayout.setObjectName('gridLayout')

		#page 1 Subway
		SubwayMenuTuple = self.SubwayMenu(DatetimeTime)
   
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

		self.SubwayBG = QtWidgets.QLabel(self.mainwidget)
		self.SubwayBG.setGeometry(QtCore.QRect(20, 0, 708, 588))
		self.SubwayBG.setObjectName("SubwayBG")
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
		self.Item2PicsetupUi_MY.setScaledContents(True)
		self.Item2Pic.setAlignment(QtCore.Qt.AlignCenter)

		self.Item3Pic = QtWidgets.QLabel(self)
		self.Item3Pic.setGeometry(QtCore.QRect(340, 300, 117, 70))
		self.Item3Pic.setPixmap(QtGui.QPixmap(SubwayMenuTuple[3][2]))
		self.Item3Pic.setScaledContents(True)
		self.Item3Pic.setObjectName("Item3Pic")
		self.Item3Pic.setAlignment(QtCore.Qt.AlignCenter)


		
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
		#self.label_4 = QtWidgets.QLabel(self.mainwidget)
		#self.label_4.setGeometry(QtCore.QRect(-86, -1, 131, 141))
		#self.label_4.setObjectName("label_4")
		
		self.SubwayBG.raise_()


		self.Item0Price.raise_()
		self.Item1Price.raise_()
		self.Item2Price.raise_()
		self.Item3Price.raise_()
		self.Item0Pic.raise_()
		self.Item1Pic.raise_()
		self.Item2Pic.raise_()
		self.Item3Pic.raise_()

		self.Item0Name.raise_()
		self.Item1Name.raise_()
		self.Item2Name.raise_()
		self.Item3Name.raise_()

		

		self.retranslateUi_Sub(SubwayMenuTuple)
		
		QtCore.QMetaObject.connectSlotsByName(self)
	
	
	
	def retranslateUi_Sub(self,SubwayMenuTuple):
		_translate = QtCore.QCoreApplication.translate
		self.setWindowTitle(_translate("Subway", "Subway"))

		self.Item0Price.setText(_translate("Subway", SubwayMenuTuple[0][1]))
		self.Item1Price.setText(_translate("Subway", SubwayMenuTuple[1][1]))
		self.Item2Price.setText(_translate("Subway", SubwayMenuTuple[2][1]))
		self.Item3Price.setText(_translate("Subway", SubwayMenuTuple[3][1]))
		self.SubwayBG.setText(_translate("Subway", "Subway"))

		self.Item0Pic.setText(_translate("Subway", "Item0Pic"))
		self.Item1Pic.setText(_translate("Subway", "Item1Pic"))
		self.Item2Pic.setText(_translate("Subway", "Item2Pic"))
		self.Item3Pic.setText(_translate("Subway", "Item3Pic"))
		self.Item0Pic.setPixmap(QtGui.QPixmap(SubwayMenuTuple[0][2]))
		self.Item1Pic.setPixmap(QtGui.QPixmap(SubwayMenuTuple[1][2]))
		self.Item2Pic.setPixmap(QtGui.QPixmap(SubwayMenuTuple[2][2]))
		self.Item3Pic.setPixmap(QtGui.QPixmap(SubwayMenuTuple[3][2]))

		self.Item0Name.setText(_translate("Subway", SubwayMenuTuple[0][0]))
		self.Item1Name.setText(_translate("Subway", SubwayMenuTuple[1][0]))
		self.Item2Name.setText(_translate("Subway", SubwayMenuTuple[2][0]))
		self.Item3Name.setText(_translate("Subway", SubwayMenuTuple[3][0]))
		#self.label_4.setText(_translate("Subway", "TextLabel"))

	def retranslateUi_MY(self,MYMenuTuple):
		_translate = QtCore.QCoreApplication.translate
		self.setWindowTitle(_translate("MalayStall", "Malay Stall"))

		self.item0_price.setText(_translate("MalayStall", MYMenuTuple[0][1]))
		self.item1_price.setText(_translate("MalayStall", MYMenuTuple[1][1]))
		self.item2_price.setText(_translate("MalayStall", MYMenuTuple[2][1]))
		self.item3_price.setText(_translate("MalayStall", MYMenuTuple[3][1]))
		#self.MYBG.setText(_translate("MalayStall", "MY Stall"))

		self.item0_Pic.setPixmap(QtGui.QPixmap(MYMenuTuple[0][2]))
		self.item1_Pic.setPixmap(QtGui.QPixmap(MYMenuTuple[1][2]))
		self.item2_Pic.setPixmap(QtGui.QPixmap(MYMenuTuple[2][2]))
		self.item3_Pic.setPixmap(QtGui.QPixmap(MYMenuTuple[3][2]))

		self.item0_Name.setText(_translate("MalayStall", MYMenuTuple[0][0]))
		self.item1_Name.setText(_translate("MalayStall", MYMenuTuple[1][0]))
		self.item2_Name.setText(_translate("MalayStall", MYMenuTuple[2][0]))
		self.item3_Name.setText(_translate("MalayStall", MYMenuTuple[3][0]))
		#self.OpTime.setText(_translate('Subway','12AM-12PM'))
		#self.OkButton.setText(_translate("Subway",'Ok'))

		
	
	def SubwayMenu(self,SelectedTime):
		#BreakfastTuple = ('Egg & Cheese','S$6.8'),('Chicken Bacon','S$7.5'),('Chicken Ham','S$5.6'),('Chicken Sausage','S$6.9')
		#LunchTuple = ('Chicken Tariyaki','S$7.9'),('Roast Beef','S$10.5'),('Egg Mayo','S$5.6'),('Veggie Delite','S$5.9')
		BreakfastTuple = [
						('Egg & Cheese','S$6.8','./Pictures/Subway/EggCheese.png'),
						('Chicken Bacon','S$7.5','./Pictures/Subway/ChickenBacon.png'),
						('Chicken Ham','S$5.6','./Pictures/Subway/ChickenHam.png'),
						('Chicken Sausage','S$6.9','./Pictures/Subway/ChickenSausage.png'),
						('Subway Melt','S$5.6','./Pictures/Subway/SubwayMelt.png')]
		LunchTuple = [
						('Chicken Tariyaki','S$7.9','./Pictures/Subway/ChickenTeriyaki.png'),
						('Roast Beef','S$10.5','./Pictures/Subway/RoastBeef.png'),
						('Egg Mayo','S$5.6','./Pictures/Subway/EggMayo.png'),
						('Veggie Delite','S$5.9','./Pictures/Subway/VeggieDelite.png'),
						('Turkey','S$5.6','./Pictures/Subway/Turkey.png')]
		if SelectedTime < 11:
			MenuTuple = BreakfastTuple
		else:
			MenuTuple = LunchTuple
		return MenuTuple
	def MYMenu(self,SelectedDate):
		#EvenDayMenuTuple = ('Laksa','S$5'),('Nasi Lemak','S$6'),('Nasi Briyani','S$6'),('Mee Soto','S$5.5')
		#OddDayMenuTuple = ('Nasi Kerabu','S$5.5'),('Nasi Kandar','S$5.5'),('Rojak','S$4'),('Mee Goreng Mamak','S$6.5')
		EvenDayMenuTuple = [
							('Laksa','S$5','./Pictures/MalayFood/EvenDays/Laksa.png'),
							('Nasi Lemak','S$6','./Pictures/MalayFood/EvenDays/NasiLemak.png'),
							('Nasi Briyani','S$6','./Pictures/MalayFood/EvenDays/NasiBriyani.png'),
							('Mee Soto','S$5.5','./Pictures/MalayFood/EvenDays/MeeSoto.png'),
							('Nasi Kerabu','S$5.5','./Pictures/MalayFood/EvenDays/NasiKerabu.png')]
		OddDayMenuTuple = [
							('Nasi Kerabu','S$5.5','./Pictures/MalayFood/EvenDays/NasiKerabu.png'),
							('Mee Siam','S$5.5','./Pictures/MalayFood/OddDays/MeeSiam.png'),
							('Rojak','S$4','./Pictures/MalayFood/OddDays/Rojak.png'),
							('Mee Rebus','S$6.5','./Pictures/MalayFood/OddDays/MeeRebus.png'),
							('Nasi Lemak','S$6','./Pictures/MalayFood/EvenDays/NasiLemak.png')]

		#Date = current_time.weekday() + 1
		if SelectedDate % 2 == 0:
			print('Even days menu')
			MenuTuple = EvenDayMenuTuple
		else:
			print('Odd days menu')
			MenuTuple = OddDayMenuTuple
		return MenuTuple 



		self.BlueButton_2.setObjectName("BlueButton_2")
		self.BlueButton_2.raise_()
		self.BlueButton_2.setText("back")






#####################################################
Stylesheet = '''
QLabel {
	color: white;
}
'''
##########################################################




class View_Menu(QtWidgets.QWidget):
	def __init__(self,parent=None):
		super(View_Menu,self).__init__(parent)
		self.resize(800,600)
		self.setWindowOpacity(0.9)

		self.stackedwidget = QtWidgets.QStackedWidget(self)
		self.stackedwidget.setGeometry(QtCore.QRect(0,0 , 800, 600))
		self.stackedwidget.setObjectName("stackwidget")
		self.add_first_page()

	def add_first_page(self):
		self.first_page = View_Menu_First_Page()
		self.stackedwidget.addWidget(self.first_page)
		self.stackedwidget.setCurrentIndex(0)
		print (str(self.first_page.Subway_link_click())+"HAHAHAHAHHAHAHAHAHAHHAHAHA")

		self.first_page.SubButton.clicked.connect(lambda:self.add_second_page(self.first_page.Subway_link_click())) #only can use lambda: to make use of return value form functions
		self.first_page.MYButton.clicked.connect(lambda:self.add_second_page(self.first_page.MY_link_click())) #only can use lambda: to make use of return value form functions
		self.first_page.McButton.clicked.connect(lambda:self.add_second_page(self.first_page.Mc_link_click())) #only can use lambda: to make use of return value form functions
		self.first_page.KFCButton.clicked.connect(lambda:self.add_second_page(self.first_page.KFC_link_click()))#only can use lambda: to make use of return value form functions

	def add_second_page(self,store):
		print('add_second_page')
		self.second_page = View_Menu_Second_Page(store)
		self.stackedwidget.addWidget(self.second_page)
		self.stackedwidget.setCurrentIndex(1)
		if 'Subway' in self.second_page.Logo.text():
			print('Logo')
			self.second_page.BlueButton.clicked.connect(lambda:self.add_third_page(self.first_page.Subway_link_click(),self.second_page.SearchMenu()))
		elif 'Malay' in self.second_page.Logo.text():
			print('Malay logo')
			self.second_page.BlueButton.clicked.connect(lambda:self.add_third_page(self.first_page.MY_link_click(),self.second_page.SearchMenu()))
		elif 'Mcdonalds' in self.second_page.Logo.text():
			print('Mcdonalds Logo')
			self.second_page.BlueButton.clicked.connect(lambda:self.add_third_page(self.first_page.Mc_link_click(),self.second_page.SearchMenu()))
		elif 'KFC' in self.second_page.Logo.text():
			print('KFC Logo')
			self.second_page.BlueButton.clicked.connect(lambda:self.add_third_page(self.first_page.KFC_link_click(),self.second_page.SearchMenu()))


	def add_third_page(self,store,DatetimeList):
		self.third_page = View_Menu_Third_Page(store,DatetimeList)
		self.stackedwidget.addWidget(self.third_page)
		self.stackedwidget.setCurrentIndex(2)
		self.third_page.BlueButton_2.clicked.connect(self.go_back)

	def go_back(self):
		self.stackedwidget.setCurrentIndex(0)
		self.stackedwidget.removeWidget(self.second_page)
		self.stackedwidget.removeWidget(self.third_page)


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	app.setStyleSheet(Stylesheet)
	#Form = QtWidgets.QWidget()
	ui = View_Menu()
	#ui.setupUi(Form)
	ui.show()

	sys.exit(app.exec_())