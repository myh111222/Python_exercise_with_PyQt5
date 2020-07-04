# -*- coding: utf-8 -*-
import sys
import PyQt5
#from PyQt5.QtCore import Qt
#from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QStackedWidget, QHBoxLayout, QListWidgetItem
from data import menu_data
import Cover_page
import stalls
import PayCart
import AddMenu
import DeletMenu
import LoadMenu
import New_viewMenu
from Functional import Component as cpn
from Functional import sql

Qt = PyQt5.QtCore.Qt
QIcon = PyQt5.QtGui.QIcon


class LeftTabWidget(QWidget):
	#initialisation
	def __init__(self, *args, **kwargs):
		super(LeftTabWidget, self).__init__(*args, **kwargs)
		layout = QHBoxLayout(self, spacing=0)
		layout.setContentsMargins(0, 0, 0, 0)
		self.listWidget = QListWidget(self)
		layout.addWidget(self.listWidget)
		self.stackedWidget = QStackedWidget(self)
		layout.addWidget(self.stackedWidget)
		self.initAllUi()
		self.setMinimumSize(cpn.WindowSize)
		self.setMaximumSize(cpn.WindowSize)

	'''
	#test code for xtract from Database to get a list
	def xtractDatabase(self):
		def dict_factory(cursor, row):
			return dict((col[0], row[idx]) for idx, col in enumerate(cursor.description))
		conn = sqlite3.connect('./data/stallData.db')
		#c.execute("""CREATE TABLE PayCart (itemName TEXT,quantity INTERGER,unitprice REAL)""")
		conn.row_factory=dict_factory
		s = conn.cursor()
		s.execute( "SELECT * FROM stallTable")
		self.listss=s.fetchall()
		#print (self.listss)
	'''

	#===============================================================================================
	# start of main code
	#===============================================================================================
	def initAllUi(self):
		self.setWindowTitle("Canteen")
		# core feature, connect row change with the stack widget and display
		self.listWidget.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)
		self.listWidget.setFrameShape(QListWidget.NoFrame)
		self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		# add left side list widgets from list
		for sidebar in menu_data.sidebar_list:
			item = QListWidgetItem(QIcon(sidebar['icon']), str(sidebar['PageName']), self.listWidget)
			item.setSizeHint(cpn.SizeQListWidget)

		#Main page
		main_window = Cover_page.SlippedImgWidget('./Pictures/bg.jpg', './Pictures/fg_1.png')
		self.stackedWidget.addWidget(main_window)
		#stalls page
		#used data base conver it to similar format
		for stall in sql.getfromDB():
			self.stackedWidget.addWidget(stalls.stalls_window(stall))
			#print (stall)

		#View_Menu
		self.stackedWidget.addWidget(New_viewMenu.View_Menu())
		#Pay Cart
		self.stackedWidget.addWidget(PayCart.Cart_Pay())
		#Add Menu
		self.stackedWidget.addWidget(AddMenu.AddMenu())
		#Delete Menu
		self.stackedWidget.addWidget(DeletMenu.DeleteMenu())
		#Load Menu
		self.stackedWidget.addWidget(LoadMenu.LoadMenu())





Stylesheet = """

QListWidget, QListView, QTreeWidget, QTreeView {
	outline: 5px;
}
QListWidget {
	min-width: 120px;
	max-width: 120px;
	color: white;
	background: rgb(42, 12, 12);
}
QListWidget::item:selected {
	background: rgb(52, 32, 32);
	border-left: 3px solid rgb(99, 87, 197);
}

HistoryPanel::item:hover {
	background: rgb(52, 52, 52);
}

QStackedWidget {
	background: rgb(42, 12, 12);
}
"""

if __name__ == '__main__':

	APP = QApplication(sys.argv)
	APP.setStyleSheet(Stylesheet)
	W = LeftTabWidget()
	W.show()
	sys.exit(APP.exec_())
