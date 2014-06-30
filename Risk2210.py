#!/usr/bin/env python

"""
#OS X 10.9.3
#using PySide 1.2.1
#using Qt 4.8.6
#chmod +x this file, then cd [wherever this is], ./Risk2210.py
"""
territoryNames = ["Northwestern Oil Emirate","Alberta","Mexico","American Republic","Exiled States of America","Nunavut","Canada","Republique du Quebec","Continental Biospheres","New Avalon","Iceland GRC","Warsaw Republic","Jotenheim","Imperial Balkania","Ukrayina","Andorra","Argentina","Amazon Desert","Andean Nations","Nuevo Timoto","Zaire Military Zone","Ministry of Djibouti","Egypt","Madagascar","Saharan Empire","Lesotho","Afghanistan","Hong Kong","United Indiastan","Alden","Japan","Pevek","Middle East","Khan Industrial State","Angkhor Wat","Siberia","Enclave of the Bear","Sakha","Australian Testing Ground","Java Cartel","New Guinea","Aboriginal League","Poseidon","Hawaiian Preserve","New Atlantis","Ivory Reef","Neo Paulo","Nova Brasilia","New York","Western Ireland","South Ceylon","Microcorp","Akara","Sung Tzu","Neo Tokyo","Free Afrikaans Republic","Independent Kansas","Shackleton","Southern Anarchist Control Zone"]

territoryBorders = [[1,5,31],[0,5,6,9],[3,8,19],[2,6,7,8],[5,7,10],[0,1,4,6],[1,3,5,8],[3,4,6],[1,2,3,6], [10,11,12,15],[4,9,12],[9,12,13,14,15],[9,10,11,14],[11,14,15,22,32],[11,12,13,26,32,36], [9,11,14,24],[17,18,46,57],[16,18,19,24,47],[16,17,19],[2,17,18],[21,24,25], [20,22,23,24,25,32],[13,21,24,32],[21,25,51],[17,13,15,20,21,22],[20,21,23,45,55], [14,27,28,32,36],[26,28,33,34,35,36,54],[26,27,32,34,50],[31,33,35,37],[31,33,54], [0,29,30,33,37],[14,21,22,26,28],[27,29,30,31,35],[27,28,39],[27,29,33,36,37], [14,26,27,35],[29,31,35],[40,41],[34,40,41,53],[38,39,41],[38,39,40],[8,43],[42,44], [43,54],[25,46],[16,45],[17,48],[47,49],[9,48],[28,51],[23,50,52],[41,51,56],[39,54], [27,30,44,53],[25,56,57,58],[52,55,58],[16,55,58],[55,56,57]]

territoryPositions = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[2,1],[2,2],[2,3],[2,4],[2,5],[2,6],[2,7],[16,9],[12,10],[13,9],[10,8],[3,3],[3,4],[3,5],[3,6],[3,7],[3,8],[3,9],[4,1],[4,2],[4,3],[4,4],[4,5],[4,6],[4,7],[4,8],[4,9],[5,1],[5,2],[5,3],[5,4],[5,5],[5,6],[5,7],[5,8],[5,9],[6,1],[6,2],[6,3],[6,4],[6,5],[11,27],[14,27],[15,30],[9,37],[7,38],[22,20],[23,35],[22,7],[23,20]]

territoryLabels = []

territories = []
players = []

class player:
	#change all fields to arrays
	spaceStations = 0
	cards = 0
	commanders = {"Diplomat":False,"Land":False,"Water":False,"Space":False,"Nuke":False,"Tech":False}
	energy = 3
	name = "player"
	
	def __init__(self, inputName):
		self.name = inputName

class uPlayer:
	#should be singleton, don't know how to do those
	currentPlayer = 0
	colors = ["red", "green", "blue", "yellow", "brown"]
	
	def getCurrentColor():
		return colors[currentPlayer]
	
	def getCurrentPlayer(self): #self needed for button hooked methods of an object
		print players[self.currentPlayer].name
		
	def changePlayer(self):
		self.currentPlayer += 1
		if self.currentPlayer == len(players) or players[self.currentPlayer] == -1:
			self.currentPlayer = 0
			
	def getCommanders(self):
		print players[self.currentPlayer].commanders
		
	def hasCommander(type):
		return players[self.currentPlayer].commanders[type]

class territory:
	armies = 0
	qlabel = "none"
	owner = "none"
	type = "mars"
	name = "none"
	borders = []
	hasSpaceStation = False
	
	def changeLabel():
		qlabel.setText("<font color='red'>0</font>")
	
	def __init__(self, inputNumber):
		name = territoryNames[inputNumber]
		borders = territoryBorders[inputNumber]
		#qlabel = territoryLabels[inputNumber]
		#self.changeLabel()
		
		if inputNumber < 42:
			type = "land"
		elif inputNumber < 55:
			type = "water"
		elif inputNumber < 59:
			type = "land"
		else:
			type = "moon"
	
	



import sys
import os
import random
from PySide import *


#MacBook panel is 1440x900
width = 1400
height = 860
gfxOff = 40


UniversalPlayer = uPlayer() #never make another uPlayer



currentPath = []
def isContiguous(start, end): #pass in territory objects from territories
	global currentPath
	if start is end:
		currentPath = list()
		return True
	currentPath.append(start)
	for new in start.borders:
		if new in currentPath:
			continue
		if new.owner is not UniversalPlayer.getCurrentPlayer():
			continue
		if isContiguous(new, end):
			return True
	currentPath.pop()
	return False



class boardGUI(QtGui.QWidget): #cannot be QtGui.QMainWindow or button layout fails

	def generateTerritories(self):
		global territories
		for i in range(len(territoryNames)):
			territories.append(territory(i))

	def assignPlayers(self):
		text,ok = QtGui.QInputDialog.getText(self,'Enter Player Names','Comma Separated:')
		if ok:
			global players #must declare, otherwise creates new "players" list
			names = text.replace(" ","").split(',')
			for a in names:
				players.append(player(a))
		else:
			exit()
	
	def __init__(self):
		super(boardGUI, self).__init__()
		self.initUI()
		
	
	def buttonSetup(self):
	
		vertSpace = QtGui.QSpacerItem(1,730)
		horiSpace = QtGui.QSpacerItem(1200,1)
		#,QtGui.QSizePolicy.Minimum)#,QtGui.QSizePolicy.Expanding)
		
		playerbtn = QtGui.QPushButton('Current Player', self)
		changebtn = QtGui.QPushButton('Change Player', self)
		quitbtn = QtGui.QPushButton('Quit', self)
		commandersbtn = QtGui.QPushButton('Commanders', self)
		
		
		buttons = QtGui.QGridLayout()
		buttons.setVerticalSpacing(2)
		buttons.addItem(vertSpace, 0, 1)			#all these are row,column
		buttons.addItem(horiSpace, 1, 0)
		buttons.addWidget(playerbtn, 1, 0)
		buttons.addWidget(changebtn, 2, 0)
		buttons.addWidget(quitbtn, 1, 1)
		buttons.addWidget(commandersbtn, 2, 1)
		
		
		territoryMarks = QtGui.QGridLayout()
		territoryMarks.setSpacing(0)
		
		#blank = QtGui.QSpacerItem(1,1)
		global territoryLabels
		for i in range(40):
			territoryMarks.addItem(QtGui.QSpacerItem(30,30), 0, i)
		for k in range(25):
			territoryMarks.addItem(QtGui.QSpacerItem(30,30), k, 0)
		for a in range(len(territoryPositions)):
			label = QtGui.QLabel("<font color='red'>0</font>")
			label.setToolTip(territoryNames[a])
			territoryLabels.append(label)
			territoryMarks.addWidget(label, territoryPositions[a][0], territoryPositions[a][1]) #number rows, number cols
		
		buttons.addLayout(territoryMarks,0,0)
		
		
		self.setLayout(buttons)
		
	
		changebtn.clicked.connect(UniversalPlayer.changePlayer)
		playerbtn.clicked.connect(UniversalPlayer.getCurrentPlayer)
		commandersbtn.clicked.connect(UniversalPlayer.getCommanders)
		
		
		quitbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
	
	
		
	def mapUnderlay(self):
		earth = QtGui.QLabel(self)
		earth.setGeometry(0, 0, 1227, 756)
		#use full ABSOLUTE path to the image, not relative
		earth.setPixmap(QtGui.QPixmap(os.getcwd() + "/earthw.png"))
		#earth.setPixmap(QtGui.QPixmap(os.getcwd() + "earth.png"))
		
		
	def initUI(self):
	
		#tooltip stuff
		#QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
		#self.setToolTip('This is a <b>QWidget</b> widget')
		#btn.setToolTip('This is a <b>QPushButton</b> widget')
		
		self.assignPlayers()
		
		self.mapUnderlay()
		
		self.buttonSetup()
		
		self.generateTerritories()
		
		
		
		
		self.setGeometry(gfxOff, gfxOff, width, height)
		self.setWindowTitle('Risk 2210')
		#self.setWindowIcon(QtGui.QIcon('web.png'))		this for title bar
	
		self.show()



def main():
	app = QtGui.QApplication(sys.argv)
	ex = boardGUI()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()

























