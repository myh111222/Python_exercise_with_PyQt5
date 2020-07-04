def buttonstyles(buttonname,colors):
    buttonname ='#'+buttonname 
    return (	buttonname +" {\n"
                        "	 background-color: #"+colors[0]+";\n"
                        "	 min-width: 200px;\n"
                        "	 max-width: 200px;\n"
                        "	 min-height: 170px;\n"
                        "	 max-height: 170px;\n"
                        "	 border-radius: 50px; \n"
                        "	 color: #"+colors[1]+";}\n"
                        + buttonname +
                        ":hover {\n"
                        "	 background-color: #"+colors[1]+";\n"
                        "	 color: #"+colors[2]+";}\n"
                        + buttonname +
                        ":pressed {\n"
                        "	 background-color: #"+colors[3]+";\n"
                        "	 color: #000000;}\n"
                        )



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

