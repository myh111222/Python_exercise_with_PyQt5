import sqlite3
import json
import os


class PayCart:
	def __init__(self, itemName, quantity, unitprice):
		self.itemName = itemName
		self.quantity = quantity
		self.unitprice = unitprice

	@property
	def totalPrice(self):
		return (self.quantity * self.unitprice)



def conn_PayCart():

	conn = sqlite3.connect('./data/PayCart.db')
	return conn



class Input_stallData:
	num_of_stall=0
	def __init__(self, stallName, backGround, icon,menuBackground,PageName):
		self.stallName = stallName
		self.backGround = backGround
		self.icon = icon
		self.menuBackground = menuBackground
		self.PageName = PageName
		self.listOfStalls=[]
		self.listOfdishes=[]

		#print ("   "+self.stallName, self.backGround, self.PageName + "  ====== ===== ====")
	def getStall(self):
		constallDB = sqlite3.connect('./data/stallData.db')
		c=constallDB.cursor()
		c.execute('SELECT stallName FROM stallTable')
		lista=[]
		for item in c.fetchall():
			lista.append(item[0])
		#print (lista)
		return lista

	def add_stall(self,stall):
		self.listOfStalls.append(stall)
	def rm_stall(self,stall):
		self.listOfStalls.remove(stall)
	def add_dish(self,dish):
		self.listOfdishes.append(dish)
	def rm_dish(self,dish):
		self.listOfdishes.remove(dish)


# ==========================================================================================================
# same as the name
class Input_menuData:
	num_of_dish=0
	def __init__(self, stallName,itemName, logo=None, price=None, mealType=None, orderNum=None):
		self.stallName = stallName
		self.itemName = itemName
		self.logo = logo
		self.price = price
		self.mealType = mealType
		self.orderNum = orderNum
		self.listOfdishes=[]
		#print ("   "+stallName, self.itemName, self.price + "  ====== ===== ====")
	
	def convertToBinaryData(self,filename):
		#Convert digital data to binary format
		with open(filename, 'rb') as file:
			blobData = file.read()
		return blobData

		
	def DBsetup(self):
		self.constallDB = sqlite3.connect('./data/stallData.db')
		self.c=self.constallDB.cursor()

	def detail(self):
		return (self.stallName,self.itemName, self.logo, self.price, self.mealType, self.orderNum)

	def add_dish_DB(self):
		constallDB = sqlite3.connect('./data/stallData.db')
		c=constallDB.cursor()
		print("Connected to SQLite")
		logoimage= self.convertToBinaryData(self.logo)
		with constallDB:
			c.execute(
				'''
				INSERT INTO menuTable (stallName,itemName, logo, price, mealType, orderNum) 
						VALUES (?,?,?,?,?,?)''', 
			(self.stallName,self.itemName, logoimage, self.price, self.mealType, self.orderNum))

	def del_dish_DB(self):
		constallDB = sqlite3.connect('./data/stallData.db')
		c=constallDB.cursor()
		with constallDB:
			c.execute('''DELETE FROM menuTable WHERE  stallName=? and itemName=? ''',(self.stallName,self.itemName))
		lista=c.fetchall()
		return  (lista)




#print (Input_menuData.del_dish_DB )
abc=Input_menuData('KFC','Test1')
print (abc.del_dish_DB())
#Input_menuData.del_dish_DB


'''
CREATE TABLE "stallTable" (
	"stallName"	TEXT UNIQUE,
	"backGround"	TEXT,
	"icon"	BLOB,
	"menuBackground"	BLOB,
	"PageName"	TEXT,
	FOREIGN KEY("stallName") REFERENCES "menuTable"("stallName"),
	PRIMARY KEY("stallName")
);

CREATE TABLE "menuTable" (
	"stallName"	TEXT,
	"itemName"	TEXT UNIQUE,
	"logo"	TEXT,
	"price"	REAL,
	"mealType"	TEXT,
	"orderNum"	INTEGER,
	PRIMARY KEY("stallName","itemName")
);
'''


def dict_factory(cursor, row):
	return dict((col[0], row[idx]) for idx, col in enumerate(cursor.description))

def add_item(item):
	conn = sqlite3.connect('./data/PayCart.db')
	c = conn.cursor()
	with conn:
		c.execute("INSERT INTO PayCart VALUES (:itemName, :quantity, :unitprice)", {'itemName': item.itemName, 'quantity': item.quantity, 'unitprice': item.unitprice})
		#c.execute("INSERT INTO PayCart VALUES (itemName, quantity, unitprice) VALUES (?, ?, ?)",  (item.itemName, item.quantity,item.unitprice))



# ==========================================================================================================
#  
# read from the database to get menu data and stall data
#  

def writeTofile(data, filename):
	# Convert binary data to proper format and write it on Hard Disk
	with open(filename, 'wb') as file:
		file.write(data)
	print("Stored blob data into: ", filename, "\n")


def getfromDB():
	conn = sqlite3.connect('./data/stallData.db')
	conn.row_factory=dict_factory
	s = conn.cursor()
	
	stall={}
	liststall=[]
	s.execute( "SELECT stallName  FROM stallTable")
	haha=s.fetchall()
	#print (haha)
	for astallName in haha:
		astallname=astallName
		#print(astallname['stallName'])
		s.execute( "SELECT *  FROM stallTable where stallName=?",(astallname['stallName'],))
		stallTable=s.fetchall()
		#print (stallTable[0])
		for i in stallTable[0]:
	#        print (stallTable[0][i])
			#print (i)
			stall.update({ i: stallTable[0][i]})
		s.execute( "SELECT *  FROM menuTable where stallName=?",(astallname['stallName'],))
		listss=s.fetchall()
		#photoPath = "./" + listss['itemName'] + ".png"
		#writeTofile(listss['logo'], photoPath)
		print ("==========================================")
		print (listss)
		print ("=====+++++++++++++========================")
		stall.update({"stallMenu":listss})

	#    print ("\n \n")
	#    print (json.dumps(stall,indent=2))
		liststall.append(stall)
		stall={}
	
	#print (json.dumps(liststall,indent=2))
	return liststall

