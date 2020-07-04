# -*- coding: utf-8 -*-

import sys
import pytz
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize 
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from datetime import datetime
from PyQt5.QtWidgets import QWidget, QListWidget, QStackedWidget, QHBoxLayout, QListWidgetItem, QLabel, QMessageBox
import CartPay
import McDonalds
import Cover_page
import ViewPageCombination
import kfcCombine
import Subway
import MYStall

class LeftTabWidget(QWidget):
    #initialisation
    def __init__(self, *args, **kwargs):
        super(LeftTabWidget, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        layout = QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self)
        layout.addWidget(self.listWidget)
        self.stackedWidget = QStackedWidget(self)
        layout.addWidget(self.stackedWidget)
        self.initUi()
        self.setMinimumSize(QtCore.QSize(900, 600))
        self.setMaximumSize(QtCore.QSize(900, 600))



    #===============================================================================================
    # start of main code
    #===============================================================================================
    def initUi(self):
        self.setWindowTitle("Canteen")
        self.listWidget.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)  #core feature, connect row change with the stack widget and display
        self.listWidget.setFrameShape(QListWidget.NoFrame)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #add left side list widgets
        item = QListWidgetItem(QIcon(''), str('Main Page'), self.listWidget)
        item.setSizeHint(QSize(16777215, 80))
        item.setTextAlignment(Qt.AlignCenter)
        item = QListWidgetItem(QIcon('./Logo/McDonald.ico'), str('McDonalds'), self.listWidget)
        item.setSizeHint(QSize(16777215, 80))
        item.setTextAlignment(Qt.AlignCenter)
        item = QListWidgetItem(QIcon('./Logo/Subway.ico'), str('Subway'), self.listWidget)
        item.setSizeHint(QSize(16777215, 80))
        item.setTextAlignment(Qt.AlignCenter)
        item = QListWidgetItem(QIcon('./Logo/Malay_food.ico'), str('Malay'), self.listWidget)
        item.setSizeHint(QSize(16777215, 80))
        item.setTextAlignment(Qt.AlignCenter)
        item = QListWidgetItem(QIcon('./Logo/KFC.ico'), str('KFC'), self.listWidget)
        item.setSizeHint(QSize(16777215, 80))
        item.setTextAlignment(Qt.AlignCenter)
        item = QListWidgetItem( str('View menu'), self.listWidget)
        item.setSizeHint(QSize(16777215, 80))
        item.setTextAlignment(Qt.AlignCenter)
        item = QListWidgetItem( str('Cart and pay'), self.listWidget)
        item.setSizeHint(QSize(16777215, 80))
        item.setTextAlignment(Qt.AlignCenter)
    #------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------
    #add right side stack widget
        #get time
        time_zone = pytz.timezone('Asia/Singapore') 
        current_time = datetime.now(time_zone)

        # Main page
        main_window=Cover_page.SlippedImgWidget('./Pictures/bg.jpg', './Pictures/fg_1.png')

        self.stackedWidget.addWidget(main_window)


        #===============================================================================================
        # select stalls from left list 
        #===============================================================================================
        #Mcdonalds Page
        if current_time.hour <= 12:
            McDonalds_window = McDonalds.Breakfast_Mcdonald()
        elif current_time.hour >12:
            McDonalds_window = McDonalds.Lunch_Mcdonald()  
        self.stackedWidget.addWidget(McDonalds_window)

        #Subway Page
        Subway_Window = Subway.SubwayStall()
        self.stackedWidget.addWidget(Subway_Window)
        #Malay Page
        MY_Window = MYStall.MalayStall()
        self.stackedWidget.addWidget(MY_Window)


        #KFC Page
        if current_time.hour <= 12:
            kfc_window = kfcCombine.KFC_breakfast_window()
        elif current_time.hour >12:
            kfc_window = kfcCombine.KFC_daily_window()  
        self.stackedWidget.addWidget(kfc_window)

        #view menu page
        view_menu_window = ViewPageCombination.View_Menu()
        self.stackedWidget.addWidget(view_menu_window)
        #pay and cart page
        pay_and_cart_window = CartPay.Cart_Pay()
        self.stackedWidget.addWidget(pay_and_cart_window)
Stylesheet = """

QListWidget, QListView, QTreeWidget, QTreeView {
    outline: 0px;
}

QListWidget {
    min-width: 120px;
    max-width: 120px;
    color: white;
    background: black;
}

QListWidget::item:selected {
    background: rgb(52, 52, 52);
    border-left: 2px solid rgb(9, 187, 7);
}

HistoryPanel::item:hover {
    background: rgb(52, 52, 52);
}


QStackedWidget {
    background: rgb(30, 30, 30);
}

QLabel {
    color: white;
}
"""

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyleSheet(Stylesheet)
    w = LeftTabWidget()
    w.show()
    sys.exit(app.exec_())
