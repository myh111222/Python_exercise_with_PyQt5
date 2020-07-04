#this file is self writing component template from pyqt5,
#easier to create new lables, background, text, buttons,font, txtbox
# ==========================================================================================================
# ==========================================================================================================

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QSize 



#Global Parameters:
WindowSize = QtCore.QSize(900, 600)
SizeQListWidget = QSize(111110, 55)
geometrysize = QtCore.QRect(0,0 , 800, 600)
totalitems = {}
WidgetSize = QtCore.QSize(800, 600)
startcoords1 = (60, 40)
Gefont = QtGui.QFont("Arial", 15, QtGui.QFont.Bold)
button = {'ABC':"Test"}
lable = {}
txtbox = {}
txt = {}
font = {}
style2 = {"size":15, 'bold':True, 'weight':90, 'colorbgd':'#FFB350', 'colorpress':'#AF267E', 'colorhover':'#54079f', 'w':'90', 'h':'90'}



# ==========================================================================================================

#set txt color for html format
def setcolor(txt, color):
	return("<font color=%s>%s</font>" %(color, txt))

#set txt size color for html format
def setcolorsize(txt, size, color):
	return("<font color=%s size=%s>%s</font>" %(color, size, txt))


#background template
def Set_Background(widgetss, backgroundpath):
	setBackpic = QtWidgets.QLabel(widgetss)
	setBackpic.setPixmap(QtGui.QPixmap(backgroundpath))
	setBackpic.setGeometry(geometrysize)
	setBackpic.setScaledContents(True)

#font template
def setfont(fontname, size, weight, bold):
	font[fontname] = QtGui.QFont()
	font[fontname].setFamily("Arial")
	font[fontname].setPointSize(size)
	font[fontname].setBold(bold)
	font[fontname].setWeight(weight)

setfont('general', 14, 30, True)

#text lable template
def settext(widgetss, txtename, font, position, inpttext):
	txt[txtename] = QtWidgets.QLabel(widgetss)
	txt[txtename].setGeometry(QtCore.QRect(position[0], position[1], position[2], position[3]))
	txt[txtename].setAlignment(QtCore.Qt.AlignCenter)
	txt[txtename].setText(inpttext)
	if (font != None):
		txt[txtename].setFont(font)

#image lable template
def setlable(widgetss, lablename, position, impath, scalable):
	lable[lablename] = QtWidgets.QLabel(widgetss)
	lable[lablename] .setGeometry(QtCore.QRect(position[0], position[1], position[2], position[3]))
	lable[lablename] .setPixmap(QtGui.QPixmap(impath))
	lable[lablename] .setScaledContents(scalable)

#txt box template
def setTXbox(widgetss, boxname, position, txt):
	txtbox[boxname] = QtWidgets.QLineEdit(widgetss)
	txtbox[boxname].setText(txt)
	txtbox[boxname].setGeometry(QtCore.QRect(position[0], position[1], position[2], position[3]))


#button template
#need to write the setStyleSheet in the menu_data.py under buttons
def buttonFullStyle(wedgetsss, func, **style):

	setfont('buttonFullStyle', style['size'], style['weight'], style['bold'])
	button[style['butname']] = QtWidgets.QPushButton(wedgetsss)
	button[style['butname']].setGeometry(style['position'][0], style['position'][1], style['position'][2], style['position'][3])
	button[style['butname']].setFont(font['buttonFullStyle'])
	button[style['butname']].setObjectName(style['butname'])
	button[style['butname']].setStyleSheet(style['butstyle'])
	#print (style['butstyle'])
	button[style['butname']].setText(style['buttxt'])
	#print ("the button's vaiable name is : "+ getattr(self.button[butname]))
	#click interaction
	if (func != None):
		button[style['butname']].clicked.connect(func)




#button template, simply giving the required inputs can create button, without lookup for a stylesheet 
def newbuttonfunction(wedgetsss, butname, position, buttext, func, **style):

	setfont('newbutfunc', style['size'], style['weight'], style['bold'])

	button[butname] = QtWidgets.QPushButton(wedgetsss)
	button[butname].setGeometry(position[0], position[1], position[2], position[3])
	button[butname].setFont(font['newbutfunc'])
	buttonname='#' + butname
	button[butname].setStyleSheet(
							buttonname +" {\n"
							"    background: "+ style['colorbgd'] + ";\n"
							"    color: #FFFFFF;\n"
							"    min-width: "+ style['w']+ "px;\n"
							"    max-width: "+ style['w']+ "px;\n"
							"    min-height: "+ style['h']+ "px;\n"
							"    max-height: "+ style['h']+ "px;\n"
							"    border-radius: 35px; \n"
							"}\n"+
							buttonname +":hover {\n"
							"    background-color: "+ style['colorhover'] + ";\n"
							"}\n"+
							buttonname + ":pressed {\n"
							"    background-color: "+ style['colorpress'] + ";\n"
							"}"
							)
	button[butname].setText(buttext)
	button[butname].setObjectName(butname)
	#click interaction
	if (func != None):
		button[butname].clicked.connect(func)
















