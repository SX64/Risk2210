#!/usr/bin/env python

"""
#OS X 10.9.3
#using PySide 1.2.1
#using Qt 4.8.6
#chmod +x this file, then cd [wherever this is], ./Risk2210.py
"""


players = [6,7,-1,-1,-1]

class player:
	#change all fields to arrays
	spaceStations = 0
	cards = 0
	commanders = 0

class uPlayer:
	#should be singleton, don't know how to do those
	currentPlayer = 0
	
	def getCurrentPlayer(self): #self needed for button hooked methods of an object
		print players[self.currentPlayer]
		
	def changePlayer(self):
		self.currentPlayer += 1
		if self.currentPlayer == len(players) or players[self.currentPlayer] == -1:
			self.currentPlayer = 0
			

import sys
import os
import random
from PySide import *


#MacBook panel is 1440x900
width = 1400
height = 860
gfxOff = 40


player = uPlayer() #never make another uPlayer









    






class boardGUI(QtGui.QWidget): #cannot be QtGui.QMainWindow or button layout fails



    def assignPlayers(self):
		text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
		if ok:
			#print text
			players = text.split(',') #does not actually assign
		else:
			exit()
	
	
	
    def __init__(self):
        super(boardGUI, self).__init__()
        
        self.initUI()
        
    
    def buttonSetup(self):
    	
    	space = QtGui.QSpacerItem(1,730)
    	#,QtGui.QSizePolicy.Minimum)#,QtGui.QSizePolicy.Expanding)
    	
    	playerbtn = QtGui.QPushButton('Current Player', self)
        changebtn = QtGui.QPushButton('Change Player', self)
    	quitbtn = QtGui.QPushButton('Quit', self)
    	
    	
        changebtn.resize(changebtn.sizeHint())
        quitbtn.resize(quitbtn.sizeHint())
    	playerbtn.resize(playerbtn.sizeHint())
    	
    	buttons = QtGui.QGridLayout()
    	buttons.setVerticalSpacing(2)
    	buttons.addItem(space, 0, 0)
    	buttons.addWidget(playerbtn, 1, 0)
    	buttons.addWidget(changebtn, 2, 0)
    	buttons.addWidget(quitbtn, 1, 1)
    	self.setLayout(buttons)
    	
    
        changebtn.clicked.connect(player.changePlayer)
        quitbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
    	playerbtn.clicked.connect(player.getCurrentPlayer)
    
    
    	
    def mapUnderlay(self):
        earth = QtGui.QLabel(self)
        earth.setGeometry(0, 0, 1227, 756)
        #use full ABSOLUTE path to the image, not relative
        earth.setPixmap(QtGui.QPixmap(os.getcwd() + "/earth.png"))
        
        
    def initUI(self):
    
    	#tooltip stuff
    	#QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        #self.setToolTip('This is a <b>QWidget</b> widget')
        #btn.setToolTip('This is a <b>QPushButton</b> widget')

        
        self.buttonSetup()
        
                
        self.mapUnderlay()
        
        #self.assignPlayers()
        
        self.setGeometry(gfxOff, gfxOff, width, height)
        self.setWindowTitle('Risk 2210')
        #self.setWindowIcon(QtGui.QIcon('web.png'))        this for title bar
    
        self.show()
        

        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = boardGUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

























